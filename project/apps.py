from django.apps import AppConfig


class ProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project'
    verbose_name = 'NINVENDO Project Core'
    
    def ready(self):
        """
        Codice da eseguire quando l'app è pronta
        """
        # Import dei signal handlers Cloudinary (solo in produzione)
        from django.conf import settings
        
        if not getattr(settings, 'DEBUG', True):
            try:
                import project.cloudinary_signals
                print("📷 Cloudinary signals registrati")
            except ImportError as e:
                print(f"⚠️ Impossibile registrare Cloudinary signals: {e}")