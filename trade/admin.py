from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TradeProposal, TradeFeedback

# Aggiungi questo al file trade/admin.py

from .user_profile import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'show_phone_in_trades', 'location', 'created_at')
    list_filter = ('show_phone_in_trades', 'created_at')
    search_fields = ('user__username', 'phone_number', 'location')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(TradeProposal)
class TradeProposalAdmin(admin.ModelAdmin):
    list_display = ("id", "from_user", "to_user", "offer_item", "want_item", "state", "created_at")
    list_filter = ("state",)
    search_fields = ("from_user__username", "to_user__username")

@admin.register(TradeFeedback)
class TradeFeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "trade", "rater", "ratee", "rating", "created_at")
    list_filter = ("rating",)
