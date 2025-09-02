from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from django_fsm import FSMField, transition
from django.core.exceptions import ValidationError

# Logging per tracciare azioni
import logging
logger = logging.getLogger(__name__)

# NB: il modello degli annunci del pacchetto django_classified si chiama "Item"
from django_classified.models import Item

class TradeProposal(models.Model):
    STATE_SENT = "sent"
    STATE_ACCEPTED = "accepted"
    STATE_DECLINED = "declined"
    STATE_CANCELLED = "cancelled"
    STATE_COMPLETED = "completed"

    STATE_CHOICES = [
        (STATE_SENT, "Inviata"),
        (STATE_ACCEPTED, "Accettata"),
        (STATE_DECLINED, "Rifiutata"),
        (STATE_CANCELLED, "Annullata"),
        (STATE_COMPLETED, "Completata"),
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

    message = models.TextField(blank=True, help_text="Messaggio opzionale per la proposta")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # NUOVI CAMPI
    expires_at = models.DateTimeField(null=True, blank=True, help_text="Scadenza automatica proposta")
    is_counter_offer = models.BooleanField(default=False)
    parent_proposal = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

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
            models.Index(fields=["created_at"]),
            models.Index(fields=["expires_at"]),
        ]
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.from_user} → {self.to_user} | {self.offer_item.title} ↔ {self.want_item.title} [{self.get_state_display()}]"

    def save(self, *args, **kwargs):
        # Auto-imposta scadenza a 7 giorni se non specificata
        if not self.expires_at and self.state == self.STATE_SENT:
            self.expires_at = timezone.now() + timedelta(days=7)
        super().save(*args, **kwargs)
        
        # GESTIONE PROPOSTE MULTIPLE: Se accetto una proposta, rifiuto automaticamente le altre
        if self.state == self.STATE_ACCEPTED and self.pk:
            print(f"🔥 SAVE: Stato è ACCEPTED, chiamando cancel_competing_proposals()")
            self.cancel_competing_proposals()

    def cancel_competing_proposals(self):
        """
        Quando una proposta viene accettata, annulla automaticamente 
        tutte le altre proposte pendenti per gli stessi annunci
        """
        print(f"🔥 CANCEL_COMPETING: Cercando proposte concorrenti")
        
        # Trova proposte concorrenti per l'annuncio offerto
        competing_for_offer = TradeProposal.objects.filter(
            want_item=self.offer_item,
            state=self.STATE_SENT
        ).exclude(pk=self.pk)
        
        # Trova proposte concorrenti per l'annuncio richiesto
        competing_for_want = TradeProposal.objects.filter(
            want_item=self.want_item,
            state=self.STATE_SENT
        ).exclude(pk=self.pk)
        
        # Annulla tutte le proposte concorrenti
        all_competing = competing_for_offer.union(competing_for_want)
        
        print(f"🔥 CANCEL_COMPETING: Trovate {all_competing.count()} proposte da annullare")
        
        for proposal in all_competing:
            proposal.state = self.STATE_CANCELLED
            proposal.save(update_fields=['state'])
            logger.info(f"Trade {proposal.id}: Automaticamente annullata per conflitto con Trade {self.id}")
            print(f"🔥 CANCEL_COMPETING: Annullata proposta {proposal.id}")

    def get_absolute_url(self):
        return reverse('trade:detail', kwargs={'pk': self.pk})
    
    def is_expired(self):
        """Controlla se la proposta è scaduta"""
        if not self.expires_at:
            return False
        return timezone.now() > self.expires_at and self.state == self.STATE_SENT
    
    def can_user_act(self, user):
        """Verifica se l'utente può agire su questa proposta"""
        return user in [self.from_user, self.to_user]
    
    def can_accept(self, user):
        """Solo il destinatario può accettare"""
        return user == self.to_user and self.state == self.STATE_SENT and not self.is_expired()
    
    def can_decline(self, user):
        """Solo il destinatario può rifiutare"""
        return user == self.to_user and self.state == self.STATE_SENT
    
    def can_cancel(self, user):
        """Entrambi possono annullare"""
        return user in [self.from_user, self.to_user] and self.state in [self.STATE_SENT, self.STATE_ACCEPTED]
    
    def can_complete(self, user):
        """Entrambi possono completare se accettata"""
        return user in [self.from_user, self.to_user] and self.state == self.STATE_ACCEPTED

    # TRANSIZIONI FSM CON DEBUG E GESTIONE AUTOMATICA DEGLI ITEM
    @transition(field=state, source=STATE_SENT, target=STATE_ACCEPTED)
    def accept(self):
        print(f"🔥🔥🔥 ACCEPT CHIAMATO! Trade {self.id} 🔥🔥🔥")
        
        try:
            # Log dell'azione
            logger.info(f"Trade {self.id}: {self.to_user} ha accettato proposta da {self.from_user}")
            print(f"🔥 Log scritto per Trade {self.id}")
            
            # Refresh degli oggetti dal database per sicurezza
            self.offer_item.refresh_from_db()
            self.want_item.refresh_from_db()
            
            print(f"🔥 PRIMA della modifica:")
            print(f"   - offer_item({self.offer_item.id}).is_active = {self.offer_item.is_active}")
            print(f"   - want_item({self.want_item.id}).is_active = {self.want_item.is_active}")
            
            # DISATTIVA GLI ANNUNCI COINVOLTI (RISERVATI)
            self.offer_item.is_active = False
            saved_offer = self.offer_item.save(update_fields=['is_active'])
            print(f"🔥 offer_item.save() completato. Risultato: {saved_offer}")
            
            self.want_item.is_active = False  
            saved_want = self.want_item.save(update_fields=['is_active'])
            print(f"🔥 want_item.save() completato. Risultato: {saved_want}")
            
            # Verifica che le modifiche siano state applicate
            self.offer_item.refresh_from_db()
            self.want_item.refresh_from_db()
            
            print(f"🔥 DOPO la modifica (refresh dal DB):")
            print(f"   - offer_item({self.offer_item.id}).is_active = {self.offer_item.is_active}")
            print(f"   - want_item({self.want_item.id}).is_active = {self.want_item.is_active}")
            
            logger.info(f"Trade {self.id}: Annunci {self.offer_item.id} e {self.want_item.id} disattivati (riservati)")
            print(f"🔥 ACCEPT completato con successo per Trade {self.id}")
            
        except Exception as e:
            print(f"🔥🔥🔥 ERRORE CRITICO in accept(): {e} 🔥🔥🔥")
            print(f"🔥 Tipo errore: {type(e).__name__}")
            import traceback
            print(f"🔥 Traceback: {traceback.format_exc()}")
            logger.error(f"ERRORE in Trade.accept(): {e}")
            raise

    @transition(field=state, source=STATE_SENT, target=STATE_DECLINED)
    def decline(self):
        print(f"🔥 DECLINE chiamato per Trade {self.id}")
        logger.info(f"Trade {self.id}: {self.to_user} ha rifiutato proposta da {self.from_user}")
        # Gli annunci rimangono attivi
        print(f"🔥 DECLINE completato per Trade {self.id}")

    @transition(field=state, source=[STATE_SENT, STATE_ACCEPTED], target=STATE_CANCELLED)
    def cancel(self):
        print(f"🔥 CANCEL chiamato per Trade {self.id}, stato attuale: {self.state}")
        logger.info(f"Trade {self.id}: Proposta annullata")
        
        try:
            # RIATTIVA GLI ANNUNCI SE ERANO STATI DISATTIVATI
            if self.state == self.STATE_ACCEPTED:
                print(f"🔥 Stato è ACCEPTED, riattivando annunci")
                
                self.offer_item.refresh_from_db()
                self.want_item.refresh_from_db()
                
                print(f"🔥 PRIMA del cancel (is_active): offer={self.offer_item.is_active}, want={self.want_item.is_active}")
                
                # Solo se erano stati disattivati per questo scambio
                self.offer_item.is_active = True
                self.offer_item.save(update_fields=['is_active'])
                
                self.want_item.is_active = True
                self.want_item.save(update_fields=['is_active'])
                
                self.offer_item.refresh_from_db()
                self.want_item.refresh_from_db()
                
                print(f"🔥 DOPO il cancel (is_active): offer={self.offer_item.is_active}, want={self.want_item.is_active}")
                
                logger.info(f"Trade {self.id}: Annunci {self.offer_item.id} e {self.want_item.id} riattivati")
            else:
                print(f"🔥 Stato non è ACCEPTED, annunci non riattivati")
                
        except Exception as e:
            print(f"🔥🔥🔥 ERRORE in cancel(): {e} 🔥🔥🔥")
            logger.error(f"ERRORE in Trade.cancel(): {e}")
            raise

    @transition(field=state, source=STATE_ACCEPTED, target=STATE_COMPLETED)
    def complete(self):
        print(f"🔥 COMPLETE chiamato per Trade {self.id}")
        logger.info(f"Trade {self.id}: Scambio completato tra {self.from_user} e {self.to_user}")
        
        # GLI ANNUNCI RIMANGONO DISATTIVATI (SCAMBIATI DEFINITIVAMENTE)
        print(f"🔥 Annunci rimangono disattivati (scambio completato)")
        
        # Aggiorna statistiche utenti
        try:
            self.from_user.trade_profile.update_stats()
            self.to_user.trade_profile.update_stats()
            print(f"🔥 Statistiche aggiornate per entrambi gli utenti")
        except UserTradeProfile.DoesNotExist:
            print(f"🔥 UserTradeProfile non esiste, saltando aggiornamento statistiche")
            pass
        
        print(f"🔥 COMPLETE completato per Trade {self.id}")


class TradeFeedback(models.Model):
    """Sistema di rating post-scambio"""
    trade = models.ForeignKey(TradeProposal, on_delete=models.CASCADE, related_name="feedbacks")
    rater = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="feedbacks_given")
    ratee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="feedbacks_received")
    
    rating = models.PositiveSmallIntegerField(
        choices=[(i, f"{i} ⭐") for i in range(1, 6)],
        help_text="Valutazione da 1 a 5 stelle"
    )
    comment = models.TextField(blank=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = [('trade', 'rater')]  # Un solo feedback per utente per scambio
        indexes = [
            models.Index(fields=["ratee", "rating"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return f"{self.rater} → {self.ratee} | {self.rating}⭐ (Scambio #{self.trade.id})"

    def clean(self):
        # Validazione: puoi votare solo se hai partecipato allo scambio
        if self.rater not in [self.trade.from_user, self.trade.to_user]:
            raise ValidationError("Puoi votare solo negli scambi a cui hai partecipato.")
        
        # Non puoi votare te stesso
        if self.rater == self.ratee:
            raise ValidationError("Non puoi votare te stesso.")
        
        # Scambio deve essere completato
        if self.trade.state != TradeProposal.STATE_COMPLETED:
            raise ValidationError("Puoi votare solo scambi completati.")


# MODELLO PER PROFILO UTENTE ESTESO
class UserTradeProfile(models.Model):
    """Statistiche e profilo trading dell'utente"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='trade_profile')
    
    # Statistiche
    total_trades_completed = models.PositiveIntegerField(default=0)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    total_ratings = models.PositiveIntegerField(default=0)
    
    # Preferenze
    auto_accept_counters = models.BooleanField(default=False, help_text="Accetta automaticamente le contro-proposte")
    email_notifications = models.BooleanField(default=True)
    
    # Badge/Achievements
    is_verified_trader = models.BooleanField(default=False)
    join_trade_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Profilo di {self.user.username} ({self.total_trades_completed} scambi, {self.avg_rating}⭐)"
    
    def update_stats(self):
        """Aggiorna statistiche dal database"""
        completed_trades = TradeFeedback.objects.filter(ratee=self.user)
        self.total_ratings = completed_trades.count()
        if self.total_ratings > 0:
            self.avg_rating = completed_trades.aggregate(
                avg=models.Avg('rating')
            )['avg'] or 0.0
        
        # Conta scambi completati
        self.total_trades_completed = TradeProposal.objects.filter(
            models.Q(from_user=self.user) | models.Q(to_user=self.user),
            state=TradeProposal.STATE_COMPLETED
        ).count()
        
        # Badge automatici
        if self.total_trades_completed >= 10 and self.avg_rating >= 4.0:
            self.is_verified_trader = True
        
        self.save()

# SIGNAL PER CREARE PROFILO AUTOMATICO
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_trade_profile(sender, instance, created, **kwargs):
    if created:
        UserTradeProfile.objects.get_or_create(user=instance)