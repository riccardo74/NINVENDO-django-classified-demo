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
