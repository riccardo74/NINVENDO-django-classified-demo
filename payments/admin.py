from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils import timezone

from .models import PaymentTransaction, SellerProfile, PurchaseRequest


@admin.register(PaymentTransaction)
class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = [
        'uuid_short', 'buyer', 'seller', 'item_title', 'total_amount_euros',
        'status', 'created_at', 'payment_link'
    ]
    list_filter = ['status', 'currency', 'created_at']
    search_fields = ['uuid', 'buyer__username', 'seller__username', 'item__title', 'stripe_payment_intent_id']
    readonly_fields = [
        'uuid', 'stripe_payment_intent_id', 'stripe_checkout_session_id',
        'created_at', 'updated_at', 'completed_at'
    ]
    
    fieldsets = [
        ('Informazioni Base', {
            'fields': ['uuid', 'status', 'created_at', 'updated_at', 'completed_at']
        }),
        ('Partecipanti', {
            'fields': ['buyer', 'seller', 'item']
        }),
        ('Importi', {
            'fields': [
                'item_price_cents', 'platform_fee_cents', 'stripe_fee_cents',
                'total_amount_cents', 'currency'
            ]
        }),
        ('Dati Stripe', {
            'fields': ['stripe_payment_intent_id', 'stripe_checkout_session_id']
        }),
        ('Dettagli Acquirente', {
            'fields': ['buyer_email', 'buyer_name', 'shipping_address', 'notes']
        }),
    ]
    
    def uuid_short(self, obj):
        return obj.uuid.hex[:8]
    uuid_short.short_description = 'UUID'
    
    def item_title(self, obj):
        return obj.item.title[:50] + ('...' if len(obj.item.title) > 50 else '')
    item_title.short_description = 'Articolo'
    
    def payment_link(self, obj):
        if obj.stripe_payment_intent_id:
            stripe_url = f"https://dashboard.stripe.com/payments/{obj.stripe_payment_intent_id}"
            return format_html('<a href="{}" target="_blank">Vedi su Stripe</a>', stripe_url)
        return '-'
    payment_link.short_description = 'Stripe'
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('buyer', 'seller', 'item')


@admin.register(PurchaseRequest)
class PurchaseRequestAdmin(admin.ModelAdmin):
    list_display = [
        'uuid_short', 'buyer', 'seller', 'item_title', 'status',
        'delivery_method', 'created_at', 'expires_at', 'is_expired_status'
    ]
    list_filter = ['status', 'delivery_method', 'created_at']
    search_fields = ['uuid', 'buyer__username', 'seller__username', 'item__title']
    readonly_fields = ['uuid', 'created_at', 'updated_at', 'is_expired_status']
    
    fieldsets = [
        ('Informazioni Base', {
            'fields': ['uuid', 'status', 'created_at', 'updated_at', 'expires_at']
        }),
        ('Partecipanti', {
            'fields': ['buyer', 'seller', 'item']
        }),
        ('Dettagli Richiesta', {
            'fields': ['message', 'delivery_method', 'shipping_address']
        }),
        ('Pagamento Collegato', {
            'fields': ['payment_transaction']
        }),
    ]
    
    def uuid_short(self, obj):
        return obj.uuid.hex[:8]
    uuid_short.short_description = 'UUID'
    
    def item_title(self, obj):
        return obj.item.title[:50] + ('...' if len(obj.item.title) > 50 else '')
    item_title.short_description = 'Articolo'
    
    def is_expired_status(self, obj):
        if obj.is_expired():
            return format_html('<span style="color: red;">Scaduta</span>')
        elif obj.status == PurchaseRequest.STATUS_PENDING:
            remaining = obj.expires_at - timezone.now()
            hours_remaining = int(remaining.total_seconds() / 3600)
            return format_html('<span style="color: orange;">Scade tra {}h</span>', hours_remaining)
        return 'N/A'
    is_expired_status.short_description = 'Scadenza'
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('buyer', 'seller', 'item', 'payment_transaction')


@admin.register(SellerProfile)
class SellerProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'accepts_payments', 'stripe_onboarding_completed',
        'total_sales', 'total_revenue_euros', 'average_rating'
    ]
    list_filter = ['accepts_payments', 'auto_accept_payments', 'stripe_onboarding_completed']
    search_fields = ['user__username', 'stripe_account_id']
    readonly_fields = [
        'total_sales', 'total_revenue_cents', 'average_rating',
        'created_at', 'updated_at'
    ]
    
    fieldsets = [
        ('Utente', {
            'fields': ['user']
        }),
        ('Configurazione Stripe', {
            'fields': ['stripe_account_id', 'stripe_onboarding_completed']
        }),
        ('Impostazioni Vendita', {
            'fields': ['accepts_payments', 'auto_accept_payments']
        }),
        ('Statistiche', {
            'fields': ['total_sales', 'total_revenue_cents', 'average_rating']
        }),
        ('Timestamp', {
            'fields': ['created_at', 'updated_at']
        }),
    ]
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
    
    actions = ['update_seller_stats']
    
    def update_seller_stats(self, request, queryset):
        """Action per aggiornare le statistiche dei venditori selezionati"""
        count = 0
        for profile in queryset:
            profile.update_stats()
            count += 1
        
        self.message_user(
            request,
            f'Statistiche aggiornate per {count} venditori.'
        )
    update_seller_stats.short_description = 'Aggiorna statistiche venditori'