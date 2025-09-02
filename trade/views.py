from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.views.generic import ListView, DetailView, View
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied

from django_classified.models import Item
from .models import TradeProposal, TradeFeedback, UserTradeProfile, TradeMessage
from .forms import (
    TradeProposalForm,
    TradeResponseForm,
    TradeFeedbackForm,
    TradeMessageForm,
    UserProfileForm,  # Aggiungiamo anche questo import
)

# 🔥 Import del nuovo modello UserProfile
from .user_profile import UserProfile


def _get_user_phone(u):
    """
    Cerca un numero di telefono in attributi/profili comuni.
    """
    candidates = [
        getattr(u, "phone", None),
        getattr(getattr(u, "profile", None), "phone", None),
        getattr(getattr(u, "userprofile", None), "phone", None),
        getattr(getattr(u, "django_classified_profile", None), "phone", None),
        getattr(getattr(u, "trade_profile", None), "phone", None),
        # 🔥 Aggiungiamo il nuovo related_name
        getattr(getattr(u, "trade_profile_extended", None), "phone_number", None),
    ]
    for v in candidates:
        if v:
            return v
    return None


class InboxTradesView(LoginRequiredMixin, ListView):
    """Lista scambi ricevuti (inbox)"""
    template_name = "trade/inbox.html"
    context_object_name = "trades"
    paginate_by = 10

    def get_queryset(self):
        return (
            TradeProposal.objects.filter(to_user=self.request.user)
            .select_related("from_user", "offer_item", "want_item")
            .order_by("-created_at")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pending_count"] = self.get_queryset().filter(
            state=TradeProposal.STATE_SENT
        ).count()
        context["view_type"] = "inbox"
        return context


class SentTradesView(LoginRequiredMixin, ListView):
    """Lista scambi inviati"""
    template_name = "trade/sent.html"
    context_object_name = "trades"
    paginate_by = 10

    def get_queryset(self):
        return (
            TradeProposal.objects.filter(from_user=self.request.user)
            .select_related("to_user", "offer_item", "want_item")
            .order_by("-created_at")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pending_count"] = self.get_queryset().filter(
            state=TradeProposal.STATE_SENT
        ).count()
        context["view_type"] = "sent"
        return context


class TradeDetailView(LoginRequiredMixin, DetailView):
    """Dettaglio singolo scambio"""
    model = TradeProposal
    template_name = "trade/detail.html"
    context_object_name = "trade"

    def get_object(self):
        trade = super().get_object()
        # Solo utenti coinvolti nello scambio possono visualizzare
        if self.request.user not in [trade.from_user, trade.to_user]:
            raise PermissionDenied("Non autorizzato")
        return trade

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trade = self.get_object()
        user = self.request.user

        # 🔥 Assicurati che i profili utente estesi esistano
        from_profile, _ = UserProfile.objects.get_or_create(user=trade.from_user)
        to_profile, _ = UserProfile.objects.get_or_create(user=trade.to_user)

        # Permessi per azioni
        context["can_accept"] = trade.can_accept(user)
        context["can_decline"] = trade.can_decline(user)
        context["can_cancel"] = trade.can_cancel(user)
        context["can_complete"] = trade.can_complete(user)

        # Form risposta (se è il destinatario e proposta pendente)
        if user == trade.to_user and trade.state == TradeProposal.STATE_SENT:
            context["response_form"] = TradeResponseForm(user, trade)

        # 🔥 Messaggistica interna (accettato o completato) per i soli partecipanti
        if trade.state in [TradeProposal.STATE_ACCEPTED, TradeProposal.STATE_COMPLETED] and \
           user in (trade.from_user, trade.to_user):

            # Carica thread in ordine cronologico
            msgs_qs = trade.messages.select_related("sender", "recipient").order_by("created_at")
            context["trade_messages"] = msgs_qs

            # Segna come letti i messaggi ricevuti
            msgs_qs.filter(recipient=user, is_read=False).update(is_read=True)

            # Form per nuovo messaggio
            context["message_form"] = TradeMessageForm(trade, user)

            # Controparte + telefono (se disponibile)
            counterparty = trade.to_user if user == trade.from_user else trade.from_user
            context["counterparty"] = counterparty
            context["counterparty_phone"] = _get_user_phone(counterparty)

        # Feedback (solo quando 'completed')
        if trade.state == TradeProposal.STATE_COMPLETED:
            try:
                context["my_feedback"] = TradeFeedback.objects.get(trade=trade, rater=user)
            except TradeFeedback.DoesNotExist:
                context["feedback_form"] = TradeFeedbackForm(trade, user)

        return context


class ProposeTradeView(LoginRequiredMixin, View):
    """Proponi uno scambio per un annuncio specifico"""
    template_name = "trade/propose.html"

    def get(self, request, item_id):
        want_item = get_object_or_404(Item, pk=item_id, is_active=True)

        # Non puoi scambiare con te stesso
        if want_item.user == request.user:
            messages.error(request, "Non puoi proporre scambi per i tuoi annunci.")
            return redirect(want_item.get_absolute_url())

        # Doppio check: attivo?
        if not want_item.is_active:
            messages.error(request, "Questo annuncio non è più disponibile per scambi.")
            return redirect("django_classified:index")

        # Hai già una proposta pendente per questo annuncio?
        existing_proposal = TradeProposal.objects.filter(
            from_user=request.user, want_item=want_item, state=TradeProposal.STATE_SENT
        ).first()
        if existing_proposal:
            messages.warning(request, "Hai già una proposta pendente per questo annuncio.")
            return redirect("trade:detail", pk=existing_proposal.pk)

        form = TradeProposalForm(request.user, want_item)

        # Annunci offerta disponibili dell'utente
        available_items = (
            Item.objects.filter(user=request.user, is_active=True)
            .exclude(pk=item_id)
        )

        context = {
            "want_item": want_item,
            "form": form,
            "available_items": available_items,
            "has_items": available_items.exists(),
        }
        return render(request, self.template_name, context)

    def post(self, request, item_id):
        want_item = get_object_or_404(Item, pk=item_id, is_active=True)

        if want_item.user == request.user:
            return HttpResponseForbidden()

        if not want_item.is_active:
            messages.error(request, "Questo annuncio non è più disponibile.")
            return redirect("django_classified:index")

        form = TradeProposalForm(request.user, want_item, request.POST)

        if form.is_valid():
            offer_item = form.cleaned_data["offer_item"]

            if not offer_item.is_active:
                messages.error(request, "L'annuncio che vuoi offrire non è più disponibile.")
                return redirect("trade:sent")

            proposal = form.save(commit=False)
            proposal.from_user = request.user
            proposal.to_user = want_item.user
            proposal.want_item = want_item
            proposal.save()

            messages.success(request, f"Proposta inviata a {want_item.user.username}!")
            return redirect("trade:sent")

        context = {"want_item": want_item, "form": form}
        return render(request, self.template_name, context)


class TradeActionView(LoginRequiredMixin, View):
    """Azioni su scambi (accept/decline/cancel/complete)"""

    def post(self, request, pk, action):
        print("🔥🔥🔥 TRADEACTIONVIEW CHIAMATA 🔥🔥🔥")
        print(f"🔥 pk={pk}, action={action}, user={request.user}")

        trade = get_object_or_404(TradeProposal, pk=pk)
        user = request.user

        print(f"🔥 Trade trovato: {trade}")
        print(f"🔥 Trade.state attuale: {trade.state}")
        print(f"🔥 Trade.from_user: {trade.from_user}")
        print(f"🔥 Trade.to_user: {trade.to_user}")

        # Permessi base
        if not trade.can_user_act(user):
            print("🔥 ERRORE: Utente non autorizzato ad agire")
            return HttpResponseForbidden("Non autorizzato")

        print(f"🔥 Permessi OK, eseguendo azione: {action}")

        try:
            if action == "accept" and trade.can_accept(user):
                print("🔥 Condizione ACCEPT soddisfatta")
                trade.accept()
                trade.save()
                messages.success(request, "Proposta accettata!")
                # Dopo l'accettazione porta subito al dettaglio per chattare
                print("🔥 Redirect detail (scambio accettato)")
                return redirect("trade:detail", pk=trade.pk)

            elif action == "decline" and trade.can_decline(user):
                print("🔥 CHIAMANDO trade.decline()")
                trade.decline()
                trade.save()
                messages.info(request, "Proposta rifiutata.")

            elif action == "cancel" and trade.can_cancel(user):
                print("🔥 CHIAMANDO trade.cancel()")
                trade.cancel()
                trade.save()
                messages.warning(request, "Proposta annullata.")

            elif action == "complete" and trade.can_complete(user):
                print("🔥 CHIAMANDO trade.complete()")
                trade.complete()
                trade.save()
                messages.success(request, "Scambio completato! Lascia un feedback.")

            else:
                print("🔥 NESSUNA CONDIZIONE SODDISFATTA!")
                print(f"🔥 action='{action}'")
                print(f"🔥 can_accept={trade.can_accept(user)}")
                print(f"🔥 can_decline={trade.can_decline(user)}")
                print(f"🔥 can_cancel={trade.can_cancel(user)}")
                print(f"🔥 can_complete={trade.can_complete(user)}")
                messages.error(request, "Azione non permessa.")

        except Exception as e:
            print(f"🔥🔥🔥 ERRORE NELLA VIEW: {e} 🔥🔥🔥")
            import traceback
            print(f"🔥 Traceback completo: {traceback.format_exc()}")
            messages.error(request, f"Errore: {str(e)}")

        # Redirect "di comodo"
        if user == trade.to_user:
            print("🔥 Redirect inbox")
            return redirect("trade:inbox")
        else:
            print("🔥 Redirect sent")
            return redirect("trade:sent")



# Sostituisci la classe SendTradeMessageView esistente in trade/views.py

@method_decorator(login_required, name="dispatch")
class SendTradeMessageView(View):
    """Invia un messaggio nel thread dello scambio con supporto immagini"""

    def post(self, request, pk):
        trade = get_object_or_404(TradeProposal, pk=pk)
        user = request.user

        # Solo partecipanti
        if user not in [trade.from_user, trade.to_user]:
            return HttpResponseForbidden("Non autorizzato")

        # Stato ammesso: accepted/completed
        if trade.state not in [TradeProposal.STATE_ACCEPTED, TradeProposal.STATE_COMPLETED]:
            messages.error(request, "Non puoi inviare messaggi per questo scambio.")
            return redirect("trade:detail", pk=pk)

        # Include files nel form
        form = TradeMessageForm(trade, user, request.POST, request.FILES)
        
        if form.is_valid():
            message = form.save()
            
            # Messaggio di conferma diverso in base al contenuto
            if message.image and message.message:
                messages.success(request, "Messaggio con immagine inviato!")
            elif message.image:
                messages.success(request, "Immagine inviata!")
            else:
                messages.success(request, "Messaggio inviato!")
                
        else:
            # Mostra errori specifici del form
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Errore nel campo {field}: {error}")

        return redirect("trade:detail", pk=pk)
@method_decorator(login_required, name="dispatch")
class SubmitFeedbackView(View):
    """Submit feedback per uno scambio completato"""

    def post(self, request, pk):
        trade = get_object_or_404(
            TradeProposal, pk=pk, state=TradeProposal.STATE_COMPLETED
        )

        # Solo partecipanti
        if request.user not in [trade.from_user, trade.to_user]:
            return HttpResponseForbidden()

        # Evita doppio feedback dallo stesso rater
        if TradeFeedback.objects.filter(trade=trade, rater=request.user).exists():
            messages.warning(request, "Hai già lasciato un feedback per questo scambio.")
            return redirect("trade:detail", pk=pk)

        # Il form pre-assegna trade/rater/ratee sull'istanza
        form = TradeFeedbackForm(trade, request.user, request.POST)
        if form.is_valid():
            feedback = form.save()

            # Aggiorna statistiche del ratee
            profile, _ = UserTradeProfile.objects.get_or_create(user=feedback.ratee)
            profile.update_stats()

            messages.success(
                request, f"Feedback inviato a {feedback.ratee.username}!"
            )
        else:
            messages.error(request, "Errore nel form del feedback.")

        return redirect("trade:detail", pk=pk)


# 🔥 NUOVA VIEW PER GESTIRE IL PROFILO UTENTE ESTESO
class UserProfileView(LoginRequiredMixin, View):
    """View per modificare il profilo utente esteso (telefono, zona, etc.)"""
    template_name = "trade/user_profile.html"
    
    def get(self, request):
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        form = UserProfileForm(instance=profile)
        return render(request, self.template_name, {'form': form, 'profile': profile})
    
    def post(self, request):
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        form = UserProfileForm(request.POST, instance=profile)
        
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Profilo aggiornato con successo!")
            return redirect('trade:profile')
        
        return render(request, self.template_name, {'form': form, 'profile': profile})


class UserTradeStatsView(LoginRequiredMixin, DetailView):
    """Statistiche scambi di un utente"""
    template_name = "trade/user_stats.html"
    context_object_name = "target_user"

    def get_object(self):
        from django.contrib.auth import get_user_model
        User = get_user_model()
        return get_object_or_404(User, username=self.kwargs["username"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        target_user = self.get_object()

        # Crea profilo se non esiste
        profile, created = UserTradeProfile.objects.get_or_create(user=target_user)
        if created:
            profile.update_stats()

        context["trade_profile"] = profile

        # Statistiche aggiuntive
        context["recent_trades"] = (
            TradeProposal.objects.filter(
                Q(from_user=target_user) | Q(to_user=target_user),
                state=TradeProposal.STATE_COMPLETED,
            )
            .select_related("from_user", "to_user", "offer_item", "want_item")[:5]
        )

        context["recent_feedbacks"] = (
            TradeFeedback.objects.filter(ratee=target_user)
            .select_related("rater", "trade")[:10]
        )
        return context