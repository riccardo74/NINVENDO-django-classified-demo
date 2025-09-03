# -*- coding: utf-8 -*-
import json
import logging

import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView

from django_classified.models import Item
from .forms import PurchaseRequestForm, SellerOnboardingForm
from .models import PaymentTransaction, SellerProfile, PurchaseRequest

logger = logging.getLogger(__name__)
stripe.api_key = settings.STRIPE_SECRET_KEY


# ----------------------------
# RICHIESTE DEL VENDITORE
# ----------------------------
class SellerRequestsView(LoginRequiredMixin, ListView):
    """Lista delle richieste di acquisto ricevute dal venditore"""
    model = PurchaseRequest
    template_name = 'payments/seller_requests.html'
    context_object_name = 'requests'
    paginate_by = 20

    def get_queryset(self):
        return (PurchaseRequest.objects
                .filter(seller=self.request.user)
                .select_related('buyer', 'item')
                .order_by('-created_at'))

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['pending_count'] = self.get_queryset().filter(
            status=PurchaseRequest.STATUS_PENDING
        ).count()
        return ctx


# ----------------------------
# RICHIESTA DI ACQUISTO (BUYER)
# ----------------------------
class RequestPurchaseView(LoginRequiredMixin, View):
    """Crea una richiesta di acquisto per un annuncio"""
    template_name = 'payments/request_purchase.html'

    def get(self, request, item_id):
        item = get_object_or_404(Item, pk=item_id, is_active=True)

        # Non puoi comprare un tuo annuncio
        if item.user == request.user:
            messages.error(request, "Non puoi acquistare i tuoi stessi annunci.")
            return redirect(item.get_absolute_url())

        # Verifica che il venditore accetti pagamenti
        seller_profile, _ = SellerProfile.objects.get_or_create(user=item.user)
        if not seller_profile.accepts_payments:
            messages.error(request, "Questo venditore non accetta pagamenti online.")
            return redirect(item.get_absolute_url())

        # Evita duplicati pendenti sullo stesso item
        existing = PurchaseRequest.objects.filter(
            buyer=request.user,
            item=item,
            status=PurchaseRequest.STATUS_PENDING
        ).first()
        if existing:
            messages.info(request, "Hai già una richiesta di acquisto pendente per questo annuncio.")
            return redirect('payments:request_detail', uuid=existing.uuid)

        # Calcola anteprima commissioni
        fees = PaymentTransaction.calculate_fees(float(item.price))

        form = PurchaseRequestForm(item=item)
        ctx = {
            'item': item,
            'seller_profile': seller_profile,
            'form': form,
            'fees': fees,
            'total_euros': fees['total_amount_cents'] / 100,
        }
        return render(request, self.template_name, ctx)

    def post(self, request, item_id):
        item = get_object_or_404(Item, pk=item_id, is_active=True)
        if item.user == request.user:
            return HttpResponseForbidden()

        form = PurchaseRequestForm(item=item, data=request.POST)
        if form.is_valid():
            pr = form.save(commit=False)
            pr.buyer = request.user
            pr.seller = item.user
            pr.item = item
            pr.save()

            messages.success(request, f"Richiesta di acquisto inviata a {item.user.username}!")
            return redirect('payments:request_detail', uuid=pr.uuid)

        fees = PaymentTransaction.calculate_fees(float(item.price))
        ctx = {
            'item': item,
            'form': form,
            'fees': fees,
            'total_euros': fees['total_amount_cents'] / 100,
        }
        return render(request, self.template_name, ctx)


class PurchaseRequestDetailView(LoginRequiredMixin, DetailView):
    """Dettaglio richiesta di acquisto"""
    model = PurchaseRequest
    template_name = 'payments/request_detail.html'
    context_object_name = 'purchase_request'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get_object(self):
        obj = super().get_object()
        if self.request.user not in [obj.buyer, obj.seller]:
            raise PermissionDenied("Non autorizzato")
        return obj

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        pr = self.get_object()

        # Commissioni in euro (non centesimi)
        fees = PaymentTransaction.calculate_fees(float(pr.item.price))
        ctx['fees'] = {
            'item_price_euros': fees['item_price_cents'] / 100,
            'platform_fee_euros': fees['platform_fee_cents'] / 100,
            'stripe_fee_euros': fees['stripe_fee_cents'] / 100,
            'total_amount_euros': fees['total_amount_cents'] / 100,
        }

        user = self.request.user
        ctx['is_seller'] = (user == pr.seller)
        ctx['is_buyer'] = (user == pr.buyer)
        ctx['can_approve'] = (
            user == pr.seller and
            pr.status == PurchaseRequest.STATUS_PENDING and
            not pr.is_expired()
        )
        return ctx


@method_decorator(login_required, name='dispatch')
class ProcessPurchaseRequestView(View):
    """Approva o rifiuta una richiesta di acquisto (solo venditore)"""
    def post(self, request, uuid, action):
        pr = get_object_or_404(PurchaseRequest, uuid=uuid)
        if request.user != pr.seller:
            return HttpResponseForbidden()

        if action == 'approve':
            if pr.status == PurchaseRequest.STATUS_PENDING:
                pr.status = PurchaseRequest.STATUS_APPROVED
                pr.save()
                messages.success(request, "Richiesta approvata! Ora l'acquirente può procedere al pagamento.")
            else:
                messages.error(request, "Questa richiesta non può essere approvata.")
        elif action == 'reject':
            if pr.status == PurchaseRequest.STATUS_PENDING:
                pr.status = PurchaseRequest.STATUS_REJECTED
                pr.save()
                messages.info(request, "Richiesta rifiutata.")
            else:
                messages.error(request, "Questa richiesta non può essere rifiutata.")
        return redirect('payments:request_detail', uuid=uuid)


# ----------------------------
# CHECKOUT / STRIPE
# ----------------------------
class CreateCheckoutSessionView(LoginRequiredMixin, View):
    """
    Crea (una sola volta) la sessione Stripe Checkout per una PurchaseRequest approvata.
    - Evita doppi pagamenti: se esiste già una transazione PROCESSING/SUCCEEDED, non ne crea un'altra.
    - Se PROCESSING con sessione checkout esistente, prova a recuperare l'URL e reindirizza lì.
    """
    def post(self, request, uuid):
        pr = get_object_or_404(PurchaseRequest, uuid=uuid)

        # 1) Solo il buyer può procedere
        if request.user != pr.buyer:
            return HttpResponseForbidden()

        # 2) La richiesta deve essere APPROVATA
        if pr.status != PurchaseRequest.STATUS_APPROVED:
            messages.error(request, "La richiesta deve essere approvata dal venditore prima di procedere al pagamento.")
            return redirect('payments:request_detail', uuid=uuid)

        # 3) L'annuncio deve essere ancora disponibile
        if not pr.item.is_active:
            messages.error(request, "Questo annuncio non è più disponibile.")
            return redirect('payments:request_detail', uuid=uuid)

        # 4) Se esiste già una transazione collegata in stato PROCESSING o SUCCEEDED, NON duplicare
        existing_tx = getattr(pr, "payment_transaction", None)
        if existing_tx and existing_tx.status in (
            PaymentTransaction.STATUS_PROCESSING,
            PaymentTransaction.STATUS_SUCCEEDED,
        ):
            # 4a) Se già pagata → success page
            if existing_tx.status == PaymentTransaction.STATUS_SUCCEEDED:
                return redirect('payments:payment_success', uuid=existing_tx.uuid)

            # 4b) Se in corso → prova a recuperare l'URL della Checkout Session; altrimenti vai al dettaglio
            if existing_tx.stripe_checkout_session_id:
                try:
                    session = stripe.checkout.Session.retrieve(existing_tx.stripe_checkout_session_id)
                    # Se la sessione non è completata, ha (di norma) ancora un URL valido
                    if getattr(session, "url", None):
                        messages.info(request, "Pagamento già avviato per questa richiesta. Ti reindirizzo alla cassa Stripe.")
                        return redirect(session.url)
                except Exception as e:
                    logger.warning(f"Impossibile recuperare Checkout Session {existing_tx.stripe_checkout_session_id}: {e}")

            messages.info(request, "Pagamento già avviato per questa richiesta.")
            return redirect('payments:payment_success', uuid=existing_tx.uuid)

        # 5) Crea NUOVA transazione + Checkout Session
        try:
            fees = PaymentTransaction.calculate_fees(float(pr.item.price))

            # 5a) Crea la transazione locale
            tx = PaymentTransaction.objects.create(
                buyer=request.user,
                seller=pr.seller,
                item=pr.item,
                buyer_email=request.user.email,
                buyer_name=request.user.get_full_name() or request.user.username,
                shipping_address=pr.shipping_address,
                **fees
            )

            # 5b) Collega la richiesta alla transazione
            pr.payment_transaction = tx
            pr.save(update_fields=['payment_transaction'])

            # 5c) Crea la sessione Stripe Checkout
            checkout = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {
                            'name': f"{pr.item.title}",
                            'description': f"Acquisto da {pr.seller.username} su NINVENDO",
                        },
                        'unit_amount': fees['total_amount_cents'],
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri(
                    reverse('payments:payment_success', kwargs={'uuid': tx.uuid})
                ),
                cancel_url=request.build_absolute_uri(
                    reverse('payments:payment_cancelled', kwargs={'uuid': tx.uuid})
                ),
                metadata={
                    'transaction_uuid': str(tx.uuid),
                    'buyer_id': str(request.user.id),
                    'seller_id': str(pr.seller.id),
                    'item_id': str(pr.item.id),
                    'request_uuid': str(pr.uuid),
                }
            )

            # 5d) Aggiorna stato transazione
            tx.stripe_checkout_session_id = checkout.id
            tx.status = PaymentTransaction.STATUS_PROCESSING
            tx.save(update_fields=['stripe_checkout_session_id', 'status'])

            # 5e) Vai alla cassa Stripe
            return redirect(checkout.url)

        except Exception as e:
            logger.error(f"Errore creazione sessione Stripe: {e}")
            messages.error(request, "Si è verificato un errore durante la creazione del pagamento.")
            return redirect('payments:request_detail', uuid=uuid)


# ----------------------------
# DETTAGLI TRANSAZIONE / SUCCESS / CANCEL
# ----------------------------
class PaymentTransactionDetailView(LoginRequiredMixin, DetailView):
    """Dettaglio di una transazione di pagamento"""
    model = PaymentTransaction
    template_name = 'payments/transaction_detail.html'
    context_object_name = 'transaction'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get_object(self):
        obj = super().get_object()
        if self.request.user not in [obj.buyer, obj.seller]:
            raise PermissionDenied("Non autorizzato")
        return obj

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        tx = self.get_object()
        # collega richiesta se presente
        try:
            ctx['purchase_request'] = tx.purchase_request
        except Exception:
            pass
        ctx['is_buyer'] = (self.request.user == tx.buyer)
        ctx['is_seller'] = (self.request.user == tx.seller)
        return ctx


class PaymentSuccessView(LoginRequiredMixin, DetailView):
    """Pagina di successo dopo il pagamento"""
    model = PaymentTransaction
    template_name = 'payments/payment_success.html'
    context_object_name = 'transaction'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get_object(self):
        obj = super().get_object()
        if self.request.user not in [obj.buyer, obj.seller]:
            raise PermissionDenied("Non autorizzato")
        return obj


class PaymentCancelledView(LoginRequiredMixin, DetailView):
    """Pagina quando il pagamento viene annullato"""
    model = PaymentTransaction
    template_name = 'payments/payment_cancelled.html'
    context_object_name = 'transaction'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get_object(self):
        obj = super().get_object()
        if self.request.user not in [obj.buyer, obj.seller]:
            raise PermissionDenied("Non autorizzato")
        return obj


# ----------------------------
# CRONOLOGIE - CORREZIONE CRITICA
# ----------------------------
class PurchaseHistoryView(LoginRequiredMixin, ListView):
    """
    Cronologia acquisti dell'utente (come acquirente).
    - Stat card coerenti
    - Tab: Richieste attive (pending/approved), Acquisti completati
    """
    model = PaymentTransaction
    template_name = 'payments/purchase_history.html'
    context_object_name = 'transactions'
    paginate_by = 20

    def get_queryset(self):
        return (PaymentTransaction.objects
                .filter(buyer=self.request.user)
                .select_related('seller', 'item')
                .order_by('-created_at'))

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # --- TRANSAZIONI COMPLETATE ---
        all_tx = self.get_queryset()
        # CORREZIONE: Usa stringhe invece di costanti
        completed_qs = all_tx.filter(status='succeeded')  # Era: PaymentTransaction.STATUS_SUCCEEDED
        processing_qs = all_tx.filter(status='processing')  # Era: PaymentTransaction.STATUS_PROCESSING

        ctx['total_transactions'] = all_tx.count()
        ctx['completed_purchases'] = completed_qs.count()
        ctx['total_spent'] = sum(t.total_amount_euros for t in completed_qs)

        # --- RICHIESTE ATTIVE (CORREZIONE CRITICA) ---
        # PROBLEMA RISOLTO: Escludere le richieste con transazioni completate
        active_reqs = (
            PurchaseRequest.objects
            .filter(
                buyer=self.request.user,
                # CORREZIONE: Usa stringhe invece di costanti  
                status__in=['pending', 'approved'],  # Era: PurchaseRequest.STATUS_PENDING, etc.
            )
            # AGGIUNTO: Esclude richieste con transazioni completate
            .exclude(payment_transaction__status='succeeded')
            .select_related('seller', 'item', 'payment_transaction')
            .order_by('-created_at')
        )
        
        ctx['active_requests'] = active_reqs
        ctx['pending_requests_count'] = active_reqs.filter(status='pending').count()
        ctx['approved_requests_count'] = active_reqs.filter(status='approved').count()

        # Liste pronte per le tabelle/tab
        ctx['completed_transactions'] = completed_qs
        ctx['processing_transactions'] = processing_qs

        return ctx

class SalesHistoryView(LoginRequiredMixin, ListView):
    """Cronologia vendite dell'utente (come venditore)."""
    model = PaymentTransaction
    template_name = 'payments/sales_history.html'
    context_object_name = 'transactions'
    paginate_by = 20

    def get_queryset(self):
        return (PaymentTransaction.objects
                .filter(seller=self.request.user)
                .select_related('buyer', 'item')
                .order_by('-created_at'))

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        all_tx = self.get_queryset()
        completed_qs = all_tx.filter(status=PaymentTransaction.STATUS_SUCCEEDED)
        ctx['total_transactions'] = all_tx.count()
        ctx['completed_sales'] = completed_qs.count()
        ctx['total_revenue'] = sum(t.item_price_euros for t in completed_qs)
        return ctx


# ----------------------------
# ONBOARDING/SETUP VENDITORE
# ----------------------------
class SellerSetupView(LoginRequiredMixin, View):
    """Configurazione impostazioni venditore"""
    template_name = 'payments/seller_setup.html'

    def get(self, request):
        profile, created = SellerProfile.objects.get_or_create(user=request.user)
        form = SellerOnboardingForm(instance=profile)
        ctx = {
            'form': form,
            'profile': profile,
            'is_new_seller': created,
        }
        return render(request, self.template_name, ctx)

    def post(self, request):
        profile, _ = SellerProfile.objects.get_or_create(user=request.user)
        form = SellerOnboardingForm(instance=profile, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Configurazione venditore aggiornata.")
            return redirect('payments:seller_setup')
        ctx = {'form': form, 'profile': profile, 'is_new_seller': False}
        return render(request, self.template_name, ctx)


# ----------------------------
# WEBHOOK STRIPE (CORREZIONE CRITICA)
# ----------------------------
@csrf_exempt
@require_POST
def stripe_webhook(request):
    """Gestione webhook Stripe - VERSIONE CORRETTA"""
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
        logger.info(f"Webhook ricevuto: {event['type']}")
    except Exception as e:
        logger.error(f"Webhook signature error: {e}")
        return HttpResponse(status=400)

    # GESTIONE CHECKOUT COMPLETATO
    if event['type'] == 'checkout.session.completed':
        data = event['data']['object']
        session_id = data.get('id')
        tx_uuid = data.get('metadata', {}).get('transaction_uuid')
        
        logger.info(f"Checkout completato - Session: {session_id}, TX UUID: {tx_uuid}")
        
        if tx_uuid:
            try:
                # Trova la transazione
                tx = PaymentTransaction.objects.select_related('item').get(uuid=tx_uuid)
                
                # Aggiorna Payment Intent ID se disponibile
                if data.get('payment_intent'):
                    tx.stripe_payment_intent_id = data['payment_intent']
                
                # CORREZIONE: Usa il metodo mark_as_succeeded che hai già nel model
                tx.mark_as_succeeded()
                
                logger.info(f"Transazione {tx.uuid} marcata come succeeded")
                
                # CORREZIONE CRITICA: Aggiorna anche la PurchaseRequest
                try:
                    pr = getattr(tx, "purchase_request", None)
                    if pr and hasattr(PurchaseRequest, "STATUS_COMPLETED"):
                        pr.status = PurchaseRequest.STATUS_COMPLETED
                        pr.save(update_fields=['status'])
                        logger.info(f"PurchaseRequest {pr.uuid} marcata come completed")
                except Exception as e:
                    logger.error(f"Errore aggiornamento PurchaseRequest: {e}")

            except PaymentTransaction.DoesNotExist:
                logger.warning(f"Transazione non trovata per uuid {tx_uuid}")
        else:
            # Fallback: cerca per session_id
            try:
                tx = PaymentTransaction.objects.select_related('item').get(
                    stripe_checkout_session_id=session_id
                )
                tx.stripe_payment_intent_id = data.get('payment_intent')
                tx.mark_as_succeeded()
                logger.info(f"Transazione trovata per session_id e marcata come succeeded")
            except PaymentTransaction.DoesNotExist:
                logger.error(f"Nessuna transazione trovata per session {session_id}")

    # GESTIONE PAYMENT INTENT COMPLETATO (backup)
    elif event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        pi_id = payment_intent.get('id')
        
        try:
            tx = PaymentTransaction.objects.get(stripe_payment_intent_id=pi_id)
            if tx.status != PaymentTransaction.STATUS_SUCCEEDED:
                tx.mark_as_succeeded()
                logger.info(f"Transazione {tx.uuid} completata via payment_intent.succeeded")
        except PaymentTransaction.DoesNotExist:
            logger.warning(f"Transazione non trovata per payment_intent {pi_id}")

    return HttpResponse(status=200)