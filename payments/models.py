from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from decimal import Decimal
import uuid

from django_classified.models import Item


class PaymentTransaction(models.Model):
    """Transazione di pagamento per l'acquisto di un annuncio"""
    
    STATUS_PENDING = 'pending'
    STATUS_PROCESSING = 'processing'
    STATUS_SUCCEEDED = 'succeeded'
    STATUS_FAILED = 'failed'
    STATUS_CANCELLED = 'cancelled'
    STATUS_REFUNDED = 'refunded'
    
    STATUS_CHOICES = [
        (STATUS_PENDING, 'In Attesa'),
        (STATUS_PROCESSING, 'In Elaborazione'),
        (STATUS_SUCCEEDED, 'Completato'),
        (STATUS_FAILED, 'Fallito'),
        (STATUS_CANCELLED, 'Annullato'),
        (STATUS_REFUNDED, 'Rimborsato'),
    ]
    
    # Identificatori
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    stripe_payment_intent_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    stripe_checkout_session_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    
    # Partecipanti
    buyer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='purchases_made'
    )
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='sales_made'
    )
    
    # Prodotto
    item = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        related_name='payment_transactions'
    )
    
    # Importi (in centesimi per evitare problemi floating point)
    item_price_cents = models.PositiveIntegerField(help_text="Prezzo dell'annuncio in centesimi")
    platform_fee_cents = models.PositiveIntegerField(default=0, help_text="Commissione piattaforma in centesimi")
    stripe_fee_cents = models.PositiveIntegerField(default=0, help_text="Commissione Stripe in centesimi")
    total_amount_cents = models.PositiveIntegerField(help_text="Importo totale in centesimi")
    
    # Metadati transazione
    currency = models.CharField(max_length=3, default='EUR')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    
    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    # Dati aggiuntivi
    buyer_email = models.EmailField()
    buyer_name = models.CharField(max_length=255, blank=True)
    shipping_address = models.TextField(blank=True, help_text="Indirizzo di spedizione se necessario")
    notes = models.TextField(blank=True, help_text="Note aggiuntive")
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['buyer', 'status']),
            models.Index(fields=['seller', 'status']),
            models.Index(fields=['status', 'created_at']),
            models.Index(fields=['stripe_payment_intent_id']),
        ]
    
    def __str__(self):
        return f"Transazione {self.uuid.hex[:8]} - {self.buyer.username} → {self.seller.username} | {self.item.title} | {self.status}"
    
    def get_absolute_url(self):
        return reverse('payments:transaction_detail', kwargs={'uuid': self.uuid})
    
    # Proprietà per gestire importi in euro
    @property
    def item_price_euros(self):
        return Decimal(self.item_price_cents) / 100
    
    @property
    def platform_fee_euros(self):
        return Decimal(self.platform_fee_cents) / 100
    
    @property
    def stripe_fee_euros(self):
        return Decimal(self.stripe_fee_cents) / 100
    
    @property
    def total_amount_euros(self):
        return Decimal(self.total_amount_cents) / 100
    
    @classmethod
    def calculate_fees(cls, item_price_euros):
        """Calcola le commissioni per un determinato prezzo"""
        item_price_cents = int(item_price_euros * 100)
        
        # Commissione piattaforma: 3% dell'importo
        platform_fee_cents = int(item_price_cents * 0.03)
        
        # Commissione Stripe: 1.4% + €0.25 per transazione in Europa
        stripe_fee_cents = int(item_price_cents * 0.014) + 25  # 25 centesimi
        
        total_cents = item_price_cents + platform_fee_cents + stripe_fee_cents
        
        return {
            'item_price_cents': item_price_cents,
            'platform_fee_cents': platform_fee_cents,
            'stripe_fee_cents': stripe_fee_cents,
            'total_amount_cents': total_cents,
        }
    
# In payments/models.py, nel modello PaymentTransaction:

def mark_as_succeeded(self):
    """Segna la transazione come completata"""
    from django.utils import timezone
    
    if self.status != self.STATUS_SUCCEEDED:
        self.status = self.STATUS_SUCCEEDED
        self.completed_at = timezone.now()
        
        # Disattiva l'annuncio (venduto)
        if self.item and self.item.is_active:
            self.item.is_active = False
            self.item.save(update_fields=['is_active'])
        
        # Aggiorna PurchaseRequest collegata
        if hasattr(self, 'purchase_request') and self.purchase_request:
            self.purchase_request.status = PurchaseRequest.STATUS_COMPLETED
            self.purchase_request.save(update_fields=['status'])
        
        self.save(update_fields=['status', 'completed_at'])

def mark_as_failed(self):
    """Segna la transazione come fallita"""
    self.status = self.STATUS_FAILED
    self.save(update_fields=['status'])

class SellerProfile(models.Model):
    """Profilo esteso per i venditori"""
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='seller_profile'
    )
    
    # Dati Stripe Connect (per i pagamenti ai venditori)
    stripe_account_id = models.CharField(max_length=255, blank=True, null=True)
    stripe_onboarding_completed = models.BooleanField(default=False)
    
    # Statistiche
    total_sales = models.PositiveIntegerField(default=0)
    total_revenue_cents = models.PositiveIntegerField(default=0)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    
    # Configurazione
    accepts_payments = models.BooleanField(default=True, help_text="Accetta pagamenti per i propri annunci")
    auto_accept_payments = models.BooleanField(default=True, help_text="Accetta automaticamente i pagamenti")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Venditore: {self.user.username}"
    
    @property
    def total_revenue_euros(self):
        return Decimal(self.total_revenue_cents) / 100
    
    def update_stats(self):
        """Aggiorna le statistiche del venditore"""
        completed_transactions = PaymentTransaction.objects.filter(
            seller=self.user,
            status=PaymentTransaction.STATUS_SUCCEEDED
        )
        
        self.total_sales = completed_transactions.count()
        self.total_revenue_cents = sum(
            t.item_price_cents for t in completed_transactions
        )
        
        # TODO: Implementare sistema di rating per gli acquisti
        # Per ora manteniamo il rating del sistema di scambi se presente
        if hasattr(self.user, 'trade_profile'):
            self.average_rating = self.user.trade_profile.average_rating
        
        self.save(update_fields=['total_sales', 'total_revenue_cents', 'average_rating'])


class PurchaseRequest(models.Model):
    """Richiesta di acquisto - step intermedio prima del pagamento"""
    
    STATUS_PENDING = 'pending'
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'
    STATUS_EXPIRED = 'expired'
    STATUS_COMPLETED = 'completed'  # Collegato a una transazione completata
    
    STATUS_CHOICES = [
        (STATUS_PENDING, 'In Attesa'),
        (STATUS_APPROVED, 'Approvata'),
        (STATUS_REJECTED, 'Rifiutata'),
        (STATUS_EXPIRED, 'Scaduta'),
        (STATUS_COMPLETED, 'Completata'),
    ]
    
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    
    buyer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='purchase_requests_made'
    )
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='purchase_requests_received'
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='purchase_requests'
    )
    
    # Messaggio dell'acquirente
    message = models.TextField(
        blank=True,
        help_text="Messaggio opzionale per il venditore"
    )
    
    # Dettagli di spedizione/ritiro
    delivery_method = models.CharField(
        max_length=50,
        choices=[
            ('pickup', 'Ritiro di persona'),
            ('shipping', 'Spedizione'),
            ('both', 'Entrambi disponibili'),
        ],
        default='both'
    )
    shipping_address = models.TextField(blank=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    
    # Collegamenti
    payment_transaction = models.OneToOneField(
        PaymentTransaction,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='purchase_request'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField(help_text="Scadenza automatica della richiesta")
    
    def save(self, *args, **kwargs):
        # Auto-imposta scadenza a 48 ore se non specificata
        if not self.expires_at:
            self.expires_at = timezone.now() + timezone.timedelta(hours=48)
        super().save(*args, **kwargs)
    
    def is_expired(self):
        return timezone.now() > self.expires_at and self.status == self.STATUS_PENDING
    
    def __str__(self):
        return f"Richiesta {self.uuid.hex[:8]} - {self.buyer.username} vuole acquistare {self.item.title}"