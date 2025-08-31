from django.urls import path
from . import views

app_name = "trade"

urlpatterns = [
    path("inbox/", views.InboxTradesView.as_view(), name="inbox"),
    path("sent/", views.SentTradesView.as_view(), name="sent"),
    path("propose/<int:item_id>/", views.ProposeTradeView.as_view(), name="propose"),
    path("<int:pk>/accept/", views.AcceptTradeView.as_view(), name="accept"),
    path("<int:pk>/decline/", views.DeclineTradeView.as_view(), name="decline"),
    path("<int:pk>/cancel/", views.CancelTradeView.as_view(), name="cancel"),
    path("<int:pk>/complete/", views.CompleteTradeView.as_view(), name="complete"),
]
