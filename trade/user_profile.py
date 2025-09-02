# trade/user_profile.py
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class UserProfile(models.Model):
    """Estensione del profilo utente per informazioni aggiuntive"""
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='trade_profile_extended'
    )
    phone_number = models.CharField(
        max_length=20, 
        blank=True, 
        null=True,
        verbose_name="Numero di Telefono",
        help_text="Numero di telefono per contatti diretti negli scambi"
    )
    show_phone_in_trades = models.BooleanField(
        default=False,
        verbose_name="Mostra telefono negli scambi",
        help_text="Permetti di mostrare il tuo numero agli altri utenti negli scambi accettati"
    )
    
    # Altri campi utili
    location = models.CharField(
        max_length=100, 
        blank=True, 
        null=True,
        verbose_name="Città/Zona",
        help_text="La tua zona per facilitare gli incontri"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Profilo Utente"
        verbose_name_plural = "Profili Utente"
    
    def __str__(self):
        return f"Profilo di {self.user.username}"
    
    @classmethod
    def get_or_create_for_user(cls, user):
        """Utility per ottenere o creare il profilo di un utente"""
        profile, created = cls.objects.get_or_create(user=user)
        return profile