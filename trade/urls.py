from django.urls import path
from . import views

app_name = "trade"

urlpatterns = [
    # Liste scambi
    path("inbox/", views.InboxTradesView.as_view(), name="inbox"),
    path("sent/", views.SentTradesView.as_view(), name="sent"),
    
    # Statistiche utente (deve essere prima di <int:pk>/)
    path("user/<str:username>/stats/", views.UserTradeStatsView.as_view(), name="user_stats"),
    
    # Dettaglio e proposta
    path("propose/<int:item_id>/", views.ProposeTradeView.as_view(), name="propose"),
    
    # Feedback e messaggi (DEVONO essere prima di <str:action> per evitare conflitti)
    path("<int:pk>/feedback/", views.SubmitFeedbackView.as_view(), name="feedback"),
    path("<int:pk>/message/", views.SendTradeMessageView.as_view(), name="send_message"),
    
    # Azioni sui scambi (pattern generico, deve essere dopo quelli specifici)
    path("<int:pk>/<str:action>/", views.TradeActionView.as_view(), name="action"),
    
    # Dettaglio (pattern generico, deve essere ultimo)
    path("<int:pk>/", views.TradeDetailView.as_view(), name="detail"),

    # Profilo utente
    path("profile/", views.UserProfileView.as_view(), name="profile"),
    
    
]
