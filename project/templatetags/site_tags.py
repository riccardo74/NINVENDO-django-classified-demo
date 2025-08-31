"""
Template tags per NINVENDO
Uso nei template: {% load site_tags %} {% site_name %}
"""

from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def site_name():
    """Restituisce il nome del sito"""
    return getattr(settings, 'SITE_NAME', 'NINVENDO')

@register.simple_tag
def site_description():
    """Restituisce la descrizione del sito"""
    return getattr(settings, 'SITE_DESCRIPTION', 'A swap and market place for nintendo lovers')

@register.simple_tag
def site_tagline():
    """Restituisce il tagline del sito"""
    return getattr(settings, 'SITE_TAGLINE', 'Your Nintendo Gaming Community')

@register.inclusion_tag('project/site_header.html')
def site_header():
    """Template tag per l'header del sito"""
    return {
        'site_name': site_name(),
        'site_description': site_description(),
    }
