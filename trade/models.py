from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from django_fsm import FSMField
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

    # USIAMO CharField INVECE DI FSMField
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default=STATE_SENT)

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

    def cancel_competing_proposals(self):
        """
        Quando una proposta viene accettata, annulla automaticamente 
        tutte le altre proposte pendenti per gli stessi annunci
        """
        print(f"🔥 CANCEL_COMPETING: Cercando proposte concorrenti per Trade {self.id}")
        
        # Trova proposte concorrenti per l'annuncio offerto
        competing_for_offer = list(TradeProposal.objects.filter(
            want_item=self.offer_item,
            state=self.STATE_SENT
        ).exclude(pk=self.pk))
        
        # Trova proposte concorrenti per l'annuncio richiesto
        competing_for_want = list(TradeProposal.objects.filter(
            want_item=self.want_item,
            state=self.STATE_SENT
        ).exclude(pk=self.pk))
        
        # Combina le liste (invece di union)
        all_competing = competing_for_offer + competing_for_want
        # Rimuovi duplicati se ce ne sono
        seen_ids = set()
        unique_competing = []
        for proposal in all_competing:
            if proposal.id not in seen_ids:
                unique_competing.append(proposal)
                seen_ids.add(proposal.id)
        
        print(f"🔥 CANCEL_COMPETING: Trovate {len(unique_competing)} proposte da annullare")
        
        for proposal in unique_competing:
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

    # METODI MANUALI (NON PIÙ FSM) CON LOGICA COMPLETA
    def accept(self):
        """Accetta la proposta e disattiva gli annunci"""
        print(f"🔥🔥🔥 ACCEPT MANUALE CHIAMATO! Trade {self.id} 🔥🔥🔥")
        
        # Verifica stato
        if self.state != self.STATE_SENT:
            raise ValidationError(f"Non puoi accettare una proposta in stato '{self.state}'")
        
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
            
            # CAMBIA STATO PRIMA DI TUTTO
            self.state = self.STATE_ACCEPTED
            print(f"🔥 Stato cambiato in: {self.state}")
            
            # DISATTIVA GLI ANNUNCI COINVOLTI (RISERVATI)
            self.offer_item.is_active = False
            self.offer_item.save(update_fields=['is_active'])
            print(f"🔥 offer_item disattivato")
            
            self.want_item.is_active = False  
            self.want_item.save(update_fields=['is_active'])
            print(f"🔥 want_item disattivato")
            
            # Verifica che le modifiche siano state applicate
            self.offer_item.refresh_from_db()
            self.want_item.refresh_from_db()
            
            print(f"🔥 DOPO la modifica (refresh dal DB):")
            print(f"   - offer_item({self.offer_item.id}).is_active = {self.offer_item.is_active}")
            print(f"   - want_item({self.want_item.id}).is_active = {self.want_item.is_active}")
            
            # ANNULLA PROPOSTE CONCORRENTI
            self.cancel_competing_proposals()
            
            logger.info(f"Trade {self.id}: Annunci {self.offer_item.id} e {self.want_item.id} disattivati (riservati)")
            print(f"🔥 ACCEPT completato con successo per Trade {self.id}")
            
        except Exception as e:
            print(f"🔥🔥🔥 ERRORE CRITICO in accept(): {e} 🔥🔥🔥")
            print(f"🔥 Tipo errore: {type(e).__name__}")
            import traceback
            print(f"🔥 Traceback: {traceback.format_exc()}")
            logger.error(f"ERRORE in Trade.accept(): {e}")
            raise

    def decline(self):
        """Rifiuta la proposta"""
        print(f"🔥 DECLINE chiamato per Trade {self.id}")
        
        if self.state != self.STATE_SENT:
            raise ValidationError(f"Non puoi rifiutare una proposta in stato '{self.state}'")
        
        self.state = self.STATE_DECLINED
        logger.info(f"Trade {self.id}: {self.to_user} ha rifiutato proposta da {self.from_user}")
        print(f"🔥 DECLINE completato per Trade {self.id}")

    def cancel(self):
        """Annulla la proposta"""
        print(f"🔥 CANCEL chiamato per Trade {self.id}, stato attuale: {self.state}")
        
        if self.state not in [self.STATE_SENT, self.STATE_ACCEPTED]:
            raise ValidationError(f"Non puoi annullare una proposta in stato '{self.state}'")
        
        try:
            old_state = self.state
            self.state = self.STATE_CANCELLED
            
            # RIATTIVA GLI ANNUNCI SE ERANO STATI DISATTIVATI
            if old_state == self.STATE_ACCEPTED:
                print(f"🔥 Stato era ACCEPTED, riattivando annunci")
                
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
                print(f"🔥 Stato non era ACCEPTED, annunci non riattivati")
                
            logger.info(f"Trade {self.id}: Proposta annullata")
                
        except Exception as e:
            print(f"🔥🔥🔥 ERRORE in cancel(): {e} 🔥🔥🔥")
            logger.error(f"ERRORE in Trade.cancel(): {e}")
            raise

    def complete(self):
        """Completa lo scambio"""
        print(f"🔥 COMPLETE chiamato per Trade {self.id}")
        
        if self.state != self.STATE_ACCEPTED:
            raise ValidationError(f"Non puoi completare una proposta in stato '{self.state}'")
        
        self.state = self.STATE_COMPLETED
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


class TradeMessage(models.Model):
    """Sistema di messaggistica interna per gli scambi CON supporto immagini"""
    trade = models.ForeignKey(TradeProposal, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sent_trade_messages")
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="received_trade_messages")
    
    message = models.TextField(
        max_length=1000, 
        blank=True,  # Ora può essere vuoto se c'è un'immagine
        help_text="Messaggio per organizzare lo scambio"
    )
    
    # Campo per l'immagine allegata
    image = models.ImageField(
        upload_to='trade_messages/%Y/%m/%d/',
        blank=True,
        null=True,
        help_text="Immagine allegata al messaggio"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=["trade", "created_at"]),
            models.Index(fields=["sender", "created_at"]),
            models.Index(fields=["recipient", "is_read"]),
        ]

    def __str__(self):
        if self.message:
            preview = self.message[:50] + "..." if len(self.message) > 50 else self.message
            return f"{self.sender.username}: {preview}"
        elif self.image:
            return f"{self.sender.username}: [Immagine allegata]"
        else:
            return f"{self.sender.username}: [Messaggio vuoto]"
    
    def clean(self):
        """Validazione: deve esserci almeno un messaggio o un'immagine"""
        if not self.message and not self.image:
            raise ValidationError("È necessario inserire un messaggio o allegare un'immagine.")
    
    def save(self, *args, **kwargs):
        # Auto-imposta il recipient come l'altro utente nello scambio
        if not self.recipient:
            self.recipient = self.trade.to_user if self.sender == self.trade.from_user else self.trade.from_user
        super().save(*args, **kwargs)
    
    def get_image_thumbnail_url(self):
        """Genera URL per thumbnail dell'immagine (se supportato)"""
        if self.image:
            try:
                from sorl.thumbnail import get_thumbnail
                thumbnail = get_thumbnail(self.image, '300x200', crop='center', quality=85)
                return thumbnail.url
            except ImportError:
                # Se sorl.thumbnail non è disponibile, usa l'immagine originale
                return self.image.url
            except Exception:
                # Fallback per altri errori
                return self.image.url
        return None
    
    def get_file_size_display(self):
        """Mostra dimensione file in formato leggibile"""
        if self.image and hasattr(self.image, 'size'):
            size = self.image.size
            if size < 1024:
                return f"{size} B"
            elif size < 1024 * 1024:
                return f"{size // 1024} KB"
            else:
                return f"{size // (1024 * 1024)} MB"
        return None


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
    
    # Informazioni di contatto (NUOVO)
    phone_number = models.CharField(
        max_length=20, 
        blank=True, 
        help_text="Numero di telefono per organizzare scambi"
    )
    show_phone_in_trades = models.BooleanField(
        default=False,
        help_text="Mostra il numero negli scambi accettati"
    )
    location = models.CharField(
        max_length=100,
        blank=True,
        help_text="Città o zona di preferenza per gli scambi"
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
        help_text="Breve descrizione del profilo"
    )
    
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
    
    def get_contact_info_for_user(self, requesting_user, trade=None):
        """
        Restituisce informazioni di contatto se appropriate.
        Solo negli scambi accettati/completati tra gli utenti coinvolti.
        """
        if not trade or requesting_user not in [trade.from_user, trade.to_user]:
            return None
            
        if trade.state not in [TradeProposal.STATE_ACCEPTED, TradeProposal.STATE_COMPLETED]:
            return None
            
        contact_info = {}
        if self.show_phone_in_trades and self.phone_number:
            contact_info['phone'] = self.phone_number
        if self.location:
            contact_info['location'] = self.location
            
        return contact_info if contact_info else None


# SIGNAL PER CREARE PROFILO AUTOMATICO
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_trade_profile(sender, instance, created, **kwargs):
    if created:
        UserTradeProfile.objects.get_or_create(user=instance)