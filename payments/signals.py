from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import SellerProfile


@receiver(post_save, sender=User)
def create_seller_profile(sender, instance, created, **kwargs):
    """
    Crea automaticamente un profilo venditore per ogni nuovo utente
    """
    if created:
        SellerProfile.objects.create(user=instance)


@receiver(post_save, sender=User)  
def save_seller_profile(sender, instance, **kwargs):
    """
    Salva il profilo venditore quando l'utente viene salvato
    """
    try:
        instance.seller_profile.save()
    except SellerProfile.DoesNotExist:
        SellerProfile.objects.create(user=instance)