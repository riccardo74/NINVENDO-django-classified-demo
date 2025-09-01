# Generated migration file
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, help_text='Numero di telefono per contatti diretti negli scambi', max_length=20, null=True, verbose_name='Numero di Telefono')),
                ('show_phone_in_trades', models.BooleanField(default=False, help_text='Permetti di mostrare il tuo numero agli altri utenti negli scambi accettati', verbose_name='Mostra telefono negli scambi')),
                ('location', models.CharField(blank=True, help_text='La tua zona per facilitare gli incontri', max_length=100, null=True, verbose_name='Città/Zona')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='trade_profile_extended', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profilo Utente',
                'verbose_name_plural': 'Profili Utente',
            },
        ),
    ]