from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from trade.user_profile import UserProfile

User = get_user_model()

class Command(BaseCommand):
    help = 'Crea profili utente per tutti gli utenti esistenti'

    def handle(self, *args, **options):
        users_without_profile = User.objects.filter(profile__isnull=True)
        created_count = 0
        
        for user in users_without_profile:
            profile, created = UserProfile.objects.get_or_create(user=user)
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Creato profilo per {user.username}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Completato! Creati {created_count} nuovi profili utente.'
            )
        )