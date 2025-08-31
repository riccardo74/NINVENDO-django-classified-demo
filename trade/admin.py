from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TradeProposal, TradeFeedback

@admin.register(TradeProposal)
class TradeProposalAdmin(admin.ModelAdmin):
    list_display = ("id", "from_user", "to_user", "offer_item", "want_item", "state", "created_at")
    list_filter = ("state",)
    search_fields = ("from_user__username", "to_user__username")

@admin.register(TradeFeedback)
class TradeFeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "trade", "rater", "ratee", "rating", "created_at")
    list_filter = ("rating",)
