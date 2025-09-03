"""
Context processors per NINVENDO
Rende disponibili le configurazioni del sito in tutti i template
"""

from django.conf import settings


def site_config(request):
    """
    Context processor per le configurazioni del sito
    Uso nei template: {{ SITE_NAME }}, {{ SITE_DESCRIPTION }}, etc.
    """
    return {
        'SITE_NAME': getattr(settings, 'SITE_NAME', 'NINVENDO'),
        'SITE_DESCRIPTION': getattr(settings, 'SITE_DESCRIPTION', 'A swap and market place for nintendo lovers'),
        'SITE_TAGLINE': getattr(settings, 'SITE_TAGLINE', 'Your Nintendo Gaming Community'),
        'SITE_URL': getattr(settings, 'SITE_URL', 'http://127.0.0.1:8000'),
    }


def cloudinary_context(request):
    """
    Aggiunge informazioni Cloudinary disponibili in tutti i template
    Uso nei template: {{ CLOUDINARY_CONFIGURED }}, {{ CLOUDINARY_ACTIVE }}, etc.
    """
    
    # Verifica se Cloudinary è configurato
    cloudinary_configured = (
        hasattr(settings, 'CLOUDINARY_STORAGE') and
        settings.CLOUDINARY_STORAGE.get('CLOUD_NAME', 'your_cloud_name') != 'your_cloud_name' and
        settings.CLOUDINARY_STORAGE.get('API_KEY', 'your_api_key') != 'your_api_key'
    )
    
    # Verifica se è attivo (basato su storage backend)
    cloudinary_active = (
        cloudinary_configured and 
        getattr(settings, 'DEFAULT_FILE_STORAGE', '').endswith('MediaCloudinaryStorage')
    )
    
    return {
        'CLOUDINARY_CONFIGURED': cloudinary_configured,
        'CLOUDINARY_ACTIVE': cloudinary_active,
        'CLOUDINARY_TRANSFORMATIONS': getattr(settings, 'CLOUDINARY_TRANSFORMATIONS', {}),
        'USE_CLOUDINARY_IN_DEV': getattr(settings, 'USE_CLOUDINARY_IN_DEV', False),
        'DEBUG': settings.DEBUG,
    }