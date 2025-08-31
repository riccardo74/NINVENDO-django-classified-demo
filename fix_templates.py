#!/usr/bin/env python3
"""
Script per configurare il nome del sito NINVENDO usando le configurazioni Django standard
"""

import os
from pathlib import Path

def setup_django_site_configuration():
    """Configura il nome del sito usando approcci Django standard"""
    
    project_root = Path(".").resolve()
    
    print("🎮 Configurazione nome sito NINVENDO")
    print("=" * 50)
    
    # Opzione 1: Configurazione via settings.py
    setup_settings_configuration(project_root)
    
    # Opzione 2: Context processor personalizzato
    create_context_processor(project_root)
    
    # Opzione 3: Template tags personalizzati
    create_template_tags(project_root)
    
    # Opzione 4: Script per Sites framework
    create_site_management_script(project_root)
    
    print("\n✅ Configurazione completata!")
    print("\n📋 Scegli quale approccio usare:")
    print("1. Settings.py + Context Processor (RACCOMANDATO)")
    print("2. Sites framework Django")
    print("3. Template tags personalizzati")

def setup_settings_configuration(project_root):
    """Aggiunge configurazioni in settings.py"""
    
    settings_file = project_root / "project" / "settings.py"
    
    settings_additions = '''

# ==========================================
# NINVENDO SITE CONFIGURATION
# ==========================================

# Nome del sito e configurazioni
SITE_NAME = "NINVENDO"
SITE_DESCRIPTION = "A swap and market place for nintendo lovers"
SITE_TAGLINE = "Your Nintendo Gaming Community"
SITE_URL = "http://127.0.0.1:8000"  # Cambia in produzione

# Per il framework Sites di Django
SITE_ID = 1
'''
    
    try:
        with open(settings_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Controlla se le configurazioni esistono già
        if 'SITE_NAME' not in content:
            with open(settings_file, 'a', encoding='utf-8') as f:
                f.write(settings_additions)
            print("✓ Aggiunte configurazioni in settings.py")
        else:
            print("ℹ️  Configurazioni già presenti in settings.py")
            
    except Exception as e:
        print(f"❌ Errore nell'aggiornare settings.py: {e}")

def create_context_processor(project_root):
    """Crea un context processor per rendere disponibili le configurazioni nei template"""
    
    # Crea il file context_processors.py
    context_processors_dir = project_root / "project"
    context_processors_file = context_processors_dir / "context_processors.py"
    
    context_processor_code = '''"""
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
'''
    
    try:
        with open(context_processors_file, 'w', encoding='utf-8') as f:
            f.write(context_processor_code)
        
        print("✓ Creato context_processors.py")
        
        # Suggerimenti per settings.py
        print("\n⚠️  IMPORTANTE: Aggiungi questo in settings.py nella sezione TEMPLATES:")
        print("""
TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                # ... altri context processors ...
                'project.context_processors.site_config',
            ],
        },
    },
]
""")
        
    except Exception as e:
        print(f"❌ Errore nella creazione del context processor: {e}")

def create_template_tags(project_root):
    """Crea template tags personalizzati"""
    
    # Crea la struttura per template tags
    templatetags_dir = project_root / "project" / "templatetags"
    templatetags_dir.mkdir(exist_ok=True)
    
    # File __init__.py
    init_file = templatetags_dir / "__init__.py"
    init_file.touch()
    
    # File site_tags.py
    site_tags_file = templatetags_dir / "site_tags.py"
    
    template_tags_code = '''"""
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
'''
    
    try:
        with open(site_tags_file, 'w', encoding='utf-8') as f:
            f.write(template_tags_code)
        
        print("✓ Creati template tags in project/templatetags/site_tags.py")
        
    except Exception as e:
        print(f"❌ Errore nella creazione dei template tags: {e}")

def create_site_management_script(project_root):
    """Crea script per gestire il Sites framework Django"""
    
    management_script = project_root / "setup_site.py"
    
    script_code = '''#!/usr/bin/env python3
"""
Script per configurare il sito usando Django Sites framework
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
sys.path.append('.')

django.setup()

def setup_site():
    """Configura il sito nel database usando Sites framework"""
    try:
        from django.contrib.sites.models import Site
        from django.conf import settings
        
        # Ottieni o crea il sito principale
        site, created = Site.objects.get_or_create(
            id=getattr(settings, 'SITE_ID', 1),
            defaults={
                'domain': 'ninvendo.local',  # Cambia per la produzione
                'name': 'NINVENDO - A swap and market place for nintendo lovers'
            }
        )
        
        if not created:
            # Aggiorna il sito esistente
            site.domain = 'ninvendo.local'
            site.name = 'NINVENDO - A swap and market place for nintendo lovers'
            site.save()
            print(f"✓ Aggiornato sito esistente: {site}")
        else:
            print(f"✓ Creato nuovo sito: {site}")
            
        # Verifica che django.contrib.sites sia in INSTALLED_APPS
        if 'django.contrib.sites' not in settings.INSTALLED_APPS:
            print("⚠️  ATTENZIONE: Aggiungi 'django.contrib.sites' in INSTALLED_APPS")
            
        return True
        
    except Exception as e:
        print(f"❌ Errore: {e}")
        return False

if __name__ == "__main__":
    print("🎮 Setup Django Sites framework per NINVENDO")
    success = setup_site()
    
    if success:
        print("\\n✅ Configurazione Sites completata!")
        print("\\nNei template usa:")
        print("{% load sites %}")
        print("{% get_current_site as current_site %}")
        print("{{ current_site.name }}")
    else:
        print("\\n❌ Configurazione fallita")
'''
    
    try:
        with open(management_script, 'w', encoding='utf-8') as f:
            f.write(script_code)
        
        print("✓ Creato setup_site.py")
        
    except Exception as e:
        print(f"❌ Errore nella creazione dello script di setup: {e}")

def update_templates_for_dynamic_config():
    """Aggiorna i template per usare configurazioni dinamiche"""
    
    project_root = Path(".").resolve()
    templates_dir = project_root / "templates" / "django_classified"
    
    if not templates_dir.exists():
        print("⚠️  Template directory non trovata")
        return
    
    print("\\n🔄 Aggiornamento template per configurazioni dinamiche...")
    
    # Template di esempio per _base.html
    base_template_example = '''
<!-- Esempio di aggiornamento per _base.html -->
<!-- Sostituisci le parti hardcoded con: -->

<title>{% block title %}{{ SITE_NAME }}{% endblock %}</title>
<meta name="description" content="{{ SITE_DESCRIPTION }}">

<h1>{{ SITE_NAME }}</h1>
<p class="lead">{{ SITE_DESCRIPTION }}</p>

<!-- Oppure usando template tags: -->
{% load site_tags %}
<title>{% block title %}{% site_name %}{% endblock %}</title>
<h1>{% site_name %}</h1>
<p class="lead">{% site_description %}</p>
'''
    
    print("📝 Esempio di aggiornamento template:")
    print(base_template_example)

if __name__ == "__main__":
    setup_django_site_configuration()
    update_templates_for_dynamic_config()