# payments/urls.py - VERSIONE CORRETTA COMPLETA

from django.urls import path
from . import views

app_name = "payments"

urlpatterns = [
    # Richiesta di acquisto
    path('request/<int:item_id>/', views.RequestPurchaseView.as_view(), name='request_purchase'),
    path('request/<uuid:uuid>/', views.PurchaseRequestDetailView.as_view(), name='request_detail'),
    path('request/<uuid:uuid>/<str:action>/', views.ProcessPurchaseRequestView.as_view(), name='process_request'),
    
    # Pagamento
    path('checkout/<uuid:uuid>/', views.CreateCheckoutSessionView.as_view(), name='create_checkout'),
    path('success/<uuid:uuid>/', views.PaymentSuccessView.as_view(), name='payment_success'),
    path('cancelled/<uuid:uuid>/', views.PaymentCancelledView.as_view(), name='payment_cancelled'),
    
    # 🔥 AGGIUNGI QUESTI URL MANCANTI:
    path('transaction/<uuid:uuid>/', views.PaymentTransactionDetailView.as_view(), name='transaction_detail'),
    
    # Cronologie
    path('purchases/', views.PurchaseHistoryView.as_view(), name='purchase_history'),
    path('sales/', views.SalesHistoryView.as_view(), name='sales_history'),
    
    # 🔥 AGGIUNGI QUESTO URL PER I VENDITORI:
    path('seller/requests/', views.SellerRequestsView.as_view(), name='seller_requests'),
    
    # Configurazione venditore
    path('seller/setup/', views.SellerSetupView.as_view(), name='seller_setup'),
    
    # Webhook Stripe
    path('stripe/webhook/', views.stripe_webhook, name='stripe_webhook'),

    # In payments/urls.py, aggiungi:
    path('transaction/<uuid:uuid>/', views.PaymentTransactionDetailView.as_view(), name='transaction_detail'),
]