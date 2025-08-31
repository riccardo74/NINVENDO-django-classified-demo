from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django_fsm import FSMField, transition

# NB: il modello degli annunci del pacchetto django_classified si chiama "Item"
from django_classified.models import Item

class TradeProposal(models.Model):
    STATE_SENT = "sent"
    STATE_ACCEPTED = "accepted"
    STATE_DECLINED = "declined"
    STATE_CANCELLED = "cancelled"
    STATE_COMPLETED = "completed"

    STATE_CHOICES = [
        (STATE_SENT, "Sent"),
        (STATE_ACCEPTED, "Accepted"),
        (STATE_DECLINED, "Declined"),
        (STATE_CANCELLED, "Cancelled"),
        (STATE_COMPLETED, "Completed"),
    ]

    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="proposals_sent"
    )
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="proposals_received"
    )

    offer_item = models.ForeignKey(
        Item, on_delete=models.PROTECT, related_name="trade_offers"
    )  # annuncio dell'offerente
    want_item = models.ForeignKey(
        Item, on_delete=models.PROTECT, related_name="trade_targets"
    )  # annuncio del destinatario

    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    state = FSMField(default=STATE_SENT, choices=STATE_CHOICES, protected=True)

    class Meta:
        constraints = [
            # Non puoi proporre uno scambio a te stesso
            models.CheckConstraint(
                check=~models.Q(from_user=models.F("to_user")), name="tp_users_distinct"
            ),
            # Non puoi scambiare lo stesso annuncio con se stesso
            models.CheckConstraint(
                check=~models.Q(offer_item=models.F("want_item")), name="tp_items_distinct"
            ),
        ]
        indexes = [
            models.Index(fields=["to_user", "state"]),
            models.Index(fields=["from_user", "state"]),
        ]

    def __str__(self):
        return f"{self.from_user} → {self.to_user} | {self.offer_item_id} ↔ {self.want_item_id} [{self.state}]"

    # Transizioni (i permessi/ownership li verifichiamo nelle view)
    @transition(field=state, source=STATE_SENT, target=STATE_ACCEPTED)
    def accept(self): pass

    @transition(field=state, source=STATE_SENT, target=STATE_DECLINED)
    def decline(self): pass

    @transition(field=state, source=[STATE_SENT, STATE_ACCEPTED], target=STATE_CANCELLED)
    def cancel(self): pass

    @transition(field=state, source=STATE_ACCEPTED, target=STATE_COMPLETED)
    def complete(self): pass


class TradeFeedback(models.Model):
    trade = models.OneToOneField(TradeProposal, on_delete=models.CASCADE, related_name="feedback")
    rater = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ratee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ratings_received")
    rating = models.PositiveSmallIntegerField()  # 1..5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
