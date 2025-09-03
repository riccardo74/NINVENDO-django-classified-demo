
from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payments'
    verbose_name = 'Sistema Pagamenti'
    
    def ready(self):
        """
        Codice da eseguire quando l'app è pronta
        """
        try:
            # Import dei signal handlers se necessario
            import payments.signals
        except ImportError:
            pass