from django.urls import path
from . import views

app_name = "trade"

urlpatterns = [
    # Liste scambi
    path("inbox/", views.InboxTradesView.as_view(), name="inbox"),
    path("sent/", views.SentTradesView.as_view(), name="sent"),
    
    # Dettaglio e proposta
    path("<int:pk>/", views.TradeDetailView.as_view(), name="detail"),
    path("propose/<int:item_id>/", views.ProposeTradeView.as_view(), name="propose"),
    
    # Azioni sui scambi
    path("<int:pk>/<str:action>/", views.TradeActionView.as_view(), name="action"),
    
    # Feedback
    path("<int:pk>/feedback/", views.SubmitFeedbackView.as_view(), name="feedback"),
    
    # Statistiche utente
    path("user/<str:username>/stats/", views.UserTradeStatsView.as_view(), name="user_stats"),
]