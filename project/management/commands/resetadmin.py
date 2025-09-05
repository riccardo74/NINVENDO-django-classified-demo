from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    def handle(self, *args, **options):
        username = os.environ.get('ADMIN_USERNAME', 'admin')
        password = os.environ.get('ADMIN_PASSWORD', 'admin123')
        
        try:
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            self.stdout.write(f'Password updated for {username}')
        except User.DoesNotExist:
            User.objects.create_superuser(username, 'admin@example.com', password)
            self.stdout.write(f'Superuser {username} created')