import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView
import json
import logging

from django_classified.models import Item
from .models import PaymentTransaction, SellerProfile, PurchaseRequest
from .forms import PurchaseRequestForm, SellerOnboardingForm

# Configura Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

logger = logging.getLogger(__name__)

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    
    # Statistiche esistenti...
    completed_transactions = self.get_queryset().filter(status='succeeded')
    context['total_transactions'] = self.get_queryset().count()
    context['completed_purchases'] = completed_transactions.count()
    context['total_spent'] = sum(t.total_amount_euros for t in completed_transactions)
    
    # AGGIUNGI QUESTO: Richieste pendenti/approvate
    context['pending_requests'] = PurchaseRequest.objects.filter(
        buyer=self.request.user,
        status__in=['pending', 'approved']
    ).select_related('seller', 'item')
    
    return context
class SellerRequestsView(LoginRequiredMixin, ListView):
    """Lista delle richieste di acquisto ricevute dal venditore"""
    model = PurchaseRequest
    template_name = 'payments/seller_requests.html'
    context_object_name = 'requests'
    paginate_by = 20
    
    def get_queryset(self):
        return PurchaseRequest.objects.filter(
            seller=self.request.user
        ).select_related('buyer', 'item').order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pending_count'] = self.get_queryset().filter(
            status=PurchaseRequest.STATUS_PENDING
        ).count()
        return context


class RequestPurchaseView(LoginRequiredMixin, View):
    """Richiesta di acquisto per un annuncio"""
    template_name = 'payments/request_purchase.html'
    
    def get(self, request, item_id):
        item = get_object_or_404(Item, pk=item_id, is_active=True)
        
        # Non puoi comprare da te stesso
        if item.user == request.user:
            messages.error(request, "Non puoi acquistare i tuoi stessi annunci.")
            return redirect(item.get_absolute_url())
        
        # Verifica che il venditore accetti pagamenti
        seller_profile, _ = SellerProfile.objects.get_or_create(user=item.user)
        if not seller_profile.accepts_payments:
            messages.error(request, "Questo venditore non accetta pagamenti online.")
            return redirect(item.get_absolute_url())
        
        # Controlla se c'è già una richiesta pendente
        existing_request = PurchaseRequest.objects.filter(
            buyer=request.user,
            item=item,
            status=PurchaseRequest.STATUS_PENDING
        ).first()
        
        if existing_request:
            messages.info(request, "Hai già una richiesta di acquisto pendente per questo annuncio.")
            return redirect('payments:request_detail', uuid=existing_request.uuid)
        
        # Calcola commissioni
        fees = PaymentTransaction.calculate_fees(float(item.price))
        
        form = PurchaseRequestForm(item=item)
        
        context = {
            'item': item,
            'seller_profile': seller_profile,
            'form': form,
            'fees': fees,
            'total_euros': fees['total_amount_cents'] / 100,
        }
        
        return render(request, self.template_name, context)
    
    def post(self, request, item_id):
        item = get_object_or_404(Item, pk=item_id, is_active=True)
        
        if item.user == request.user:
            return HttpResponseForbidden()
        
        form = PurchaseRequestForm(item=item, data=request.POST)
        
        if form.is_valid():
            purchase_request = form.save(commit=False)
            purchase_request.buyer = request.user
            purchase_request.seller = item.user
            purchase_request.item = item
            purchase_request.save()
            
            messages.success(
                request,
                f"Richiesta di acquisto inviata a {item.user.username}!"
            )
            return redirect('payments:request_detail', uuid=purchase_request.uuid)
        
        # Errori nel form
        fees = PaymentTransaction.calculate_fees(float(item.price))
        context = {
            'item': item,
            'form': form,
            'fees': fees,
            'total_euros': fees['total_amount_cents'] / 100,
        }
        
        return render(request, self.template_name, context)


class PurchaseRequestDetailView(LoginRequiredMixin, DetailView):
    """Dettaglio richiesta di acquisto"""
    model = PurchaseRequest
    template_name = 'payments/request_detail.html'
    context_object_name = 'purchase_request'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
    
    def get_object(self):
        obj = super().get_object()
        # Solo buyer o seller possono vedere
        if self.request.user not in [obj.buyer, obj.seller]:
            raise PermissionDenied("Non autorizzato")
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.get_object()
        user = self.request.user
        
        # Calcola commissioni in euro (non centesimi)
        fees = PaymentTransaction.calculate_fees(float(request.item.price))
        context['fees'] = {
            'item_price_euros': fees['item_price_cents'] / 100,
            'platform_fee_euros': fees['platform_fee_cents'] / 100,
            'stripe_fee_euros': fees['stripe_fee_cents'] / 100,
            'total_amount_euros': fees['total_amount_cents'] / 100,
        }
        
        # Permessi
        context['is_seller'] = user == request.seller
        context['is_buyer'] = user == request.buyer
        context['can_approve'] = (
            user == request.seller and 
            request.status == PurchaseRequest.STATUS_PENDING and 
            not request.is_expired()
        )
        
        return context


@method_decorator(login_required, name='dispatch')
class ProcessPurchaseRequestView(View):
    """Approva o rifiuta una richiesta di acquisto"""
    
    def post(self, request, uuid, action):
        purchase_request = get_object_or_404(PurchaseRequest, uuid=uuid)
        
        # Solo il venditore può approvare/rifiutare
        if request.user != purchase_request.seller:
            return HttpResponseForbidden()
        
        if action == 'approve':
            if purchase_request.status == PurchaseRequest.STATUS_PENDING:
                purchase_request.status = PurchaseRequest.STATUS_APPROVED
                purchase_request.save()
                messages.success(request, "Richiesta approvata! Ora l'acquirente può procedere al pagamento.")
            else:
                messages.error(request, "Questa richiesta non può essere approvata.")
                
        elif action == 'reject':
            if purchase_request.status == PurchaseRequest.STATUS_PENDING:
                purchase_request.status = PurchaseRequest.STATUS_REJECTED
                purchase_request.save()
                messages.info(request, "Richiesta rifiutata.")
            else:
                messages.error(request, "Questa richiesta non può essere rifiutata.")
        
        return redirect('payments:request_detail', uuid=uuid)


class CreateCheckoutSessionView(LoginRequiredMixin, View):
    """Crea una sessione Stripe Checkout"""
    
    def post(self, request, uuid):
        purchase_request = get_object_or_404(PurchaseRequest, uuid=uuid)
        
        # Solo il buyer può procedere al pagamento
        if request.user != purchase_request.buyer:
            return HttpResponseForbidden()
        
        # La richiesta deve essere approvata
        if purchase_request.status != PurchaseRequest.STATUS_APPROVED:
            messages.error(request, "La richiesta deve essere approvata dal venditore prima di procedere al pagamento.")
            return redirect('payments:request_detail', uuid=uuid)
        
        # Verifica che l'annuncio sia ancora disponibile
        if not purchase_request.item.is_active:
            messages.error(request, "Questo annuncio non è più disponibile.")
            return redirect('payments:request_detail', uuid=uuid)
        
        try:
            # Calcola importi
            fees = PaymentTransaction.calculate_fees(float(purchase_request.item.price))
            
            # Crea la transazione nel database
            transaction = PaymentTransaction.objects.create(
                buyer=request.user,
                seller=purchase_request.seller,
                item=purchase_request.item,
                buyer_email=request.user.email,
                buyer_name=request.user.get_full_name() or request.user.username,
                shipping_address=purchase_request.shipping_address,
                **fees
            )
            
            # Collega la transazione alla richiesta
            purchase_request.payment_transaction = transaction
            purchase_request.save()
            
            # Crea sessione Stripe Checkout
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {
                            'name': f"{purchase_request.item.title}",
                            'description': f"Acquisto da {purchase_request.seller.username} su NINVENDO",
                        },
                        'unit_amount': fees['total_amount_cents'],
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri(
                    reverse('payments:payment_success', kwargs={'uuid': transaction.uuid})
                ),
                cancel_url=request.build_absolute_uri(
                    reverse('payments:payment_cancelled', kwargs={'uuid': transaction.uuid})
                ),
                metadata={
                    'transaction_uuid': str(transaction.uuid),
                    'buyer_id': str(request.user.id),
                    'seller_id': str(purchase_request.seller.id),
                    'item_id': str(purchase_request.item.id),
                }
            )
            
            # Salva l'ID della sessione
            transaction.stripe_checkout_session_id = checkout_session.id
            transaction.status = PaymentTransaction.STATUS_PROCESSING
            transaction.save()
            
            # Redirect a Stripe Checkout
            return redirect(checkout_session.url)
            
        except Exception as e:
            logger.error(f"Errore creazione sessione Stripe: {e}")
            messages.error(request, "Si è verificato un errore durante la creazione del pagamento.")
            return redirect('payments:request_detail', uuid=uuid)


class PaymentTransactionDetailView(LoginRequiredMixin, DetailView):
    """Dettaglio di una transazione di pagamento"""
    model = PaymentTransaction
    template_name = 'payments/transaction_detail.html'
    context_object_name = 'transaction'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
    
    def get_object(self):
        obj = super().get_object()
        # Solo buyer o seller possono vedere
        if self.request.user not in [obj.buyer, obj.seller]:
            raise PermissionDenied("Non autorizzato")
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transaction = self.get_object()
        
        # Aggiungi info sulla richiesta collegata
        try:
            context['purchase_request'] = transaction.purchase_request
        except:
            pass
            
        # Info per l'utente corrente
        context['is_buyer'] = self.request.user == transaction.buyer
        context['is_seller'] = self.request.user == transaction.seller
        
        return context


class PaymentSuccessView(LoginRequiredMixin, DetailView):
    """Pagina di successo dopo il pagamento"""
    model = PaymentTransaction
    template_name = 'payments/payment_success.html'
    context_object_name = 'transaction'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
    
    def get_object(self):
        obj = super().get_object()
        # Solo buyer o seller possono vedere
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


# ============================================================================
# CORREZIONE: PurchaseHistoryView in payments/views.py
# ============================================================================

class PurchaseHistoryView(LoginRequiredMixin, ListView):
    """Cronologia acquisti dell'utente CON richieste attive"""
    model = PaymentTransaction
    template_name = 'payments/purchase_history.html'
    context_object_name = 'transactions'
    paginate_by = 20
    
    def get_queryset(self):
        return PaymentTransaction.objects.filter(
            buyer=self.request.user
        ).select_related('seller', 'item').order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Statistiche esistenti per transazioni completate
        completed_transactions = self.get_queryset().filter(status='succeeded')
        context['total_transactions'] = self.get_queryset().count()
        context['completed_purchases'] = completed_transactions.count()
        context['total_spent'] = sum(t.total_amount_euros for t in completed_transactions)
        
        # AGGIUNTO: Richieste di acquisto attive (pendenti/approvate)
        context['active_requests'] = PurchaseRequest.objects.filter(
            buyer=self.request.user,
            status__in=['pending', 'approved']
        ).select_related('seller', 'item').order_by('-created_at')
        
        # Conta richieste per stato
        context['pending_requests_count'] = context['active_requests'].filter(status='pending').count()
        context['approved_requests_count'] = context['active_requests'].filter(status='approved').count()
        
        return context
class SalesHistoryView(LoginRequiredMixin, ListView):
    """Cronologia vendite dell'utente"""
    model = PaymentTransaction
    template_name = 'payments/sales_history.html'
    context_object_name = 'transactions'
    paginate_by = 20
    
    def get_queryset(self):
        return PaymentTransaction.objects.filter(
            seller=self.request.user
        ).select_related('buyer', 'item').order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Statistiche corrette per vendite
        completed_transactions = self.get_queryset().filter(status='succeeded')
        context['total_transactions'] = self.get_queryset().count()
        context['completed_sales'] = completed_transactions.count()
        context['total_revenue'] = sum(t.item_price_euros for t in completed_transactions)
        
        return context


class SellerSetupView(LoginRequiredMixin, View):
    """Configurazione impostazioni venditore"""
    template_name = 'payments/seller_setup.html'
    
    def get(self, request):
        profile, created = SellerProfile.objects.get_or_create(user=request.user)
        form = SellerOnboardingForm(instance=profile)
        
        context = {
            'form': form,
            'profile': profile,
            'is_new_seller': created,
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        profile, created = SellerProfile.objects.get_or_create(user=request.user)
        form = SellerOnboardingForm(instance=profile, data=request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Impostazioni venditore aggiornate!")
            return redirect('payments:seller_setup')
        
        context = {
            'form': form,
            'profile': profile,
            'is_new_seller': created,
        }
        return render(request, self.template_name, context)


@csrf_exempt
def stripe_webhook(request):
    """Gestione webhook Stripe per aggiornamenti stato pagamento"""
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
    
    logger.info(f"Webhook ricevuto: {len(payload)} bytes")
    
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
        logger.info(f"Event type: {event['type']}")
    except ValueError as e:
        logger.error(f"Invalid payload: {e}")
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        logger.error(f"Invalid signature: {e}")
        return HttpResponse(status=400)
    
    # Gestisci l'evento
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        logger.info(f"Checkout completed - Session: {session['id']}")
        handle_successful_payment(session)
        
    elif event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        logger.info(f"Payment succeeded - PI: {payment_intent['id']}")
        handle_successful_payment_by_intent(payment_intent)
        
    elif event['type'] == 'payment_intent.payment_failed':
        payment_intent = event['data']['object']
        logger.error(f"Payment failed - PI: {payment_intent['id']}")
        handle_failed_payment(payment_intent)
    
    else:
        logger.info(f"Unhandled event type: {event['type']}")
    
    return HttpResponse(status=200)


def handle_successful_payment(session):
    """Gestisce un pagamento completato con successo tramite session"""
    try:
        logger.info(f"Cercando transazione per session: {session['id']}")
        
        # Trova la transazione tramite session ID
        transaction = PaymentTransaction.objects.get(
            stripe_checkout_session_id=session['id']
        )
        
        logger.info(f"Transazione trovata: {transaction.uuid}")
        
        # Aggiorna lo stato
        transaction.stripe_payment_intent_id = session.get('payment_intent')
        transaction.mark_as_succeeded()
        
        # Aggiorna la richiesta di acquisto
        try:
            purchase_request = transaction.purchase_request
            purchase_request.status = PurchaseRequest.STATUS_COMPLETED
            purchase_request.save()
            logger.info(f"PurchaseRequest {purchase_request.uuid} completata")
        except:
            logger.warning("Nessuna PurchaseRequest collegata")
        
        # Aggiorna statistiche venditore
        seller_profile, _ = SellerProfile.objects.get_or_create(user=transaction.seller)
        seller_profile.update_stats()
        
        logger.info(f"Payment successful for transaction {transaction.uuid}")
        
    except PaymentTransaction.DoesNotExist:
        logger.error(f"Transaction not found for session {session['id']}")
        
        # Prova a trovare tramite metadata
        metadata = session.get('metadata', {})
        if metadata.get('transaction_uuid'):
            try:
                transaction = PaymentTransaction.objects.get(
                    uuid=metadata['transaction_uuid']
                )
                logger.info(f"Trovata tramite metadata: {transaction.uuid}")
                transaction.stripe_checkout_session_id = session['id']
                transaction.stripe_payment_intent_id = session.get('payment_intent')
                transaction.mark_as_succeeded()
            except PaymentTransaction.DoesNotExist:
                logger.error(f"Nemmeno metadata ha funzionato: {metadata.get('transaction_uuid')}")
    
    except Exception as e:
        logger.error(f"Error handling successful payment: {e}")


def handle_successful_payment_by_intent(payment_intent):
    """Gestisce pagamento tramite payment_intent.succeeded"""
    try:
        transaction = PaymentTransaction.objects.get(
            stripe_payment_intent_id=payment_intent['id']
        )
        
        transaction.mark_as_succeeded()
        logger.info(f"Payment intent succeeded for transaction {transaction.uuid}")
        
    except PaymentTransaction.DoesNotExist:
        logger.error(f"Transaction not found for payment_intent {payment_intent['id']}")
    except Exception as e:
        logger.error(f"Error handling payment intent: {e}")


def handle_failed_payment(payment_intent):
    """Gestisce un pagamento fallito"""
    try:
        transaction = PaymentTransaction.objects.get(
            stripe_payment_intent_id=payment_intent['id']
        )
        
        transaction.mark_as_failed()
        logger.info(f"Payment failed for transaction {transaction.uuid}")
        
    except PaymentTransaction.DoesNotExist:
        logger.error(f"Transaction not found for payment_intent {payment_intent['id']}")
    except Exception as e:
        logger.error(f"Error handling failed payment: {e}")