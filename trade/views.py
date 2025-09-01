from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden, JsonResponse
from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from django.db.models import Q, Count, Avg
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator

from django_classified.models import Item
from .models import TradeProposal, TradeFeedback, UserTradeProfile
from .forms import TradeProposalForm, TradeResponseForm, TradeFeedbackForm


class InboxTradesView(LoginRequiredMixin, ListView):
    """Lista scambi ricevuti (inbox)"""
    template_name = "trade/inbox.html"
    context_object_name = "trades"
    paginate_by = 10

    def get_queryset(self):
        return TradeProposal.objects.filter(
            to_user=self.request.user
        ).select_related(
            'from_user', 'offer_item', 'want_item'
        ).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pending_count'] = self.get_queryset().filter(
            state=TradeProposal.STATE_SENT
        ).count()
        context['view_type'] = 'inbox'
        return context


class SentTradesView(LoginRequiredMixin, ListView):
    """Lista scambi inviati"""
    template_name = "trade/sent.html"
    context_object_name = "trades"
    paginate_by = 10

    def get_queryset(self):
        return TradeProposal.objects.filter(
            from_user=self.request.user
        ).select_related(
            'to_user', 'offer_item', 'want_item'
        ).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pending_count'] = self.get_queryset().filter(
            state=TradeProposal.STATE_SENT
        ).count()
        context['view_type'] = 'sent'
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
            raise HttpResponseForbidden("Non autorizzato")
        return trade

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trade = self.get_object()
        user = self.request.user
        
        # Permessi per azioni
        context['can_accept'] = trade.can_accept(user)
        context['can_decline'] = trade.can_decline(user)
        context['can_cancel'] = trade.can_cancel(user)
        context['can_complete'] = trade.can_complete(user)
        
        # Form per rispondere (se è il destinatario)
        if user == trade.to_user and trade.state == TradeProposal.STATE_SENT:
            context['response_form'] = TradeResponseForm(user, trade)
        
        # Form feedback se completato e non ancora dato
        if trade.state == TradeProposal.STATE_COMPLETED:
            try:
                existing_feedback = TradeFeedback.objects.get(trade=trade, rater=user)
                context['my_feedback'] = existing_feedback
            except TradeFeedback.DoesNotExist:
                context['feedback_form'] = TradeFeedbackForm(trade, user)
        
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
        
        form = TradeProposalForm(request.user, want_item)
        
        # Controlla se ha annunci disponibili
        available_items = Item.objects.filter(
            user=request.user, 
            is_active=True
        ).exclude(pk=item_id)
        
        context = {
            'want_item': want_item,
            'form': form,
            'available_items': available_items,
            'has_items': available_items.exists()
        }
        
        return render(request, self.template_name, context)

    def post(self, request, item_id):
        want_item = get_object_or_404(Item, pk=item_id, is_active=True)
        
        if want_item.user == request.user:
            return HttpResponseForbidden()
        
        form = TradeProposalForm(request.user, want_item, request.POST)
        
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.from_user = request.user
            proposal.to_user = want_item.user
            proposal.want_item = want_item
            proposal.save()
            
            messages.success(
                request, 
                f"✅ Proposta inviata a {want_item.user.username}!"
            )
            return redirect('trade:sent')
        
        context = {
            'want_item': want_item,
            'form': form,
        }
        return render(request, self.template_name, context)


class TradeActionView(LoginRequiredMixin, View):
    """View unificata per azioni su scambi (accept/decline/cancel/complete)"""
    
    def post(self, request, pk, action):
        trade = get_object_or_404(TradeProposal, pk=pk)
        user = request.user
        
        # Verifica permessi base
        if not trade.can_user_act(user):
            return HttpResponseForbidden("Non autorizzato")
        
        # Esegui l'azione richiesta
        try:
            if action == 'accept' and trade.can_accept(user):
                trade.accept()
                trade.save()
                messages.success(request, "✅ Proposta accettata!")
                
            elif action == 'decline' and trade.can_decline(user):
                trade.decline()
                trade.save()
                messages.info(request, "❌ Proposta rifiutata.")
                
            elif action == 'cancel' and trade.can_cancel(user):
                trade.cancel()
                trade.save()
                messages.warning(request, "🚫 Proposta annullata.")
                
            elif action == 'complete' and trade.can_complete(user):
                trade.complete()
                trade.save()
                messages.success(request, "🎉 Scambio completato! Lascia un feedback.")
                
            else:
                messages.error(request, "Azione non permessa.")
                
        except Exception as e:
            messages.error(request, f"Errore: {str(e)}")
        
        # Redirect intelligente
        if user == trade.to_user:
            return redirect('trade:inbox')
        else:
            return redirect('trade:sent')


@method_decorator(login_required, name='dispatch')
class SubmitFeedbackView(View):
    """Submit feedback per uno scambio completato"""
    
    def post(self, request, pk):
        trade = get_object_or_404(
            TradeProposal, 
            pk=pk, 
            state=TradeProposal.STATE_COMPLETED
        )
        
        # Verifica che l'utente abbia partecipato allo scambio
        if request.user not in [trade.from_user, trade.to_user]:
            return HttpResponseForbidden()
        
        # Verifica che non abbia già lasciato feedback
        if TradeFeedback.objects.filter(trade=trade, rater=request.user).exists():
            messages.warning(request, "Hai già lasciato un feedback per questo scambio.")
            return redirect('trade:detail', pk=pk)
        
        form = TradeFeedbackForm(trade, request.user, request.POST)
        
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.trade = trade
            feedback.rater = request.user
            feedback.ratee = trade.to_user if request.user == trade.from_user else trade.from_user
            feedback.save()
            
            # Aggiorna stats dell'utente votato
            try:
                feedback.ratee.trade_profile.update_stats()
            except UserTradeProfile.DoesNotExist:
                UserTradeProfile.objects.create(user=feedback.ratee)
                feedback.ratee.trade_profile.update_stats()
            
            messages.success(request, f"⭐ Feedback inviato a {feedback.ratee.username}!")
            
        else:
            messages.error(request, "Errore nel form del feedback.")
        
        return redirect('trade:detail', pk=pk)


class UserTradeStatsView(LoginRequiredMixin, DetailView):
    """Statistiche scambi di un utente"""
    template_name = "trade/user_stats.html"
    context_object_name = "target_user"
    
    def get_object(self):
        from django.contrib.auth import get_user_model
        User = get_user_model()
        return get_object_or_404(User, username=self.kwargs['username'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        target_user = self.get_object()
        
        # Crea profilo se non esiste
        profile, created = UserTradeProfile.objects.get_or_create(user=target_user)
        if created:
            profile.update_stats()
        
        context['trade_profile'] = profile
        
        # Statistiche aggiuntive
        context['recent_trades'] = TradeProposal.objects.filter(
            Q(from_user=target_user) | Q(to_user=target_user),
            state=TradeProposal.STATE_COMPLETED
        ).select_related('from_user', 'to_user', 'offer_item', 'want_item')[:5]
        
        context['recent_feedbacks'] = TradeFeedback.objects.filter(
            ratee=target_user
        ).select_related('rater', 'trade')[:10]
        
        return context