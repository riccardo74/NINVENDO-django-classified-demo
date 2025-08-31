#!/usr/bin/env python3
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
        print("\n✅ Configurazione Sites completata!")
        print("\nNei template usa:")
        print("{% load sites %}")
        print("{% get_current_site as current_site %}")
        print("{{ current_site.name }}")
    else:
        print("\n❌ Configurazione fallita")
