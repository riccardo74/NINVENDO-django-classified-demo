#!/usr/bin/env python3
"""
Script per personalizzare i template di django-classified con il branding NINVENDO
Copia i template originali e li modifica automaticamente
"""

import os
import shutil
import re
from pathlib import Path

class NinvendoTemplateCustomizer:
    def __init__(self, project_root="."):
        self.project_root = Path(project_root).resolve()
        self.venv_path = self.project_root / ".venv"
        self.source_templates = self.venv_path / "Lib/site-packages/django_classified/templates/django_classified"
        self.dest_templates = self.project_root / "templates/django_classified"
        
        # Configurazioni per le sostituzioni
        self.replacements = {
            # Sostituzioni nel title
            r'<title>([^<]*)</title>': r'<title>NINVENDO</title>',
            r'{% block title %}[^{]*{% endblock %}': r'{% block title %}NINVENDO{% endblock %}',
            r'{% block title %}[^{]*{% endblock title %}': r'{% block title %}NINVENDO{% endblock title %}',
            
            # Sostituzioni nel brand/navbar
            r'django[_\s\-]?classified': 'NINVENDO',
            r'Django[_\s\-]?Classified': 'NINVENDO',
            r'DJANGO[_\s\-]?CLASSIFIED': 'NINVENDO',
            
            # Sostituzioni descrizioni
            r'Classified\s+ads?\s+site': 'A swap and market place for nintendo lovers',
            r'classified\s+ads?\s+site': 'A swap and market place for nintendo lovers',
            r'Demo\s+site': 'A swap and market place for nintendo lovers',
            r'demo\s+site': 'A swap and market place for nintendo lovers',
            
            # Sostituzioni nel footer e meta
            r'<meta\s+name=["\']description["\']\s+content=["\'][^"\']*["\']': 
                r'<meta name="description" content="NINVENDO - A swap and market place for nintendo lovers">',
        }
        
        # Template da copiare e modificare
        self.template_files = [
            "_base.html",
            "item_list.html", 
            "item_detail.html",
            "item_form.html",
            "search.html",
            "section_list.html",
            "profile.html"
        ]

    def create_directory_structure(self):
        """Crea la struttura di directory per i template personalizzati"""
        print(f"Creando directory: {self.dest_templates}")
        self.dest_templates.mkdir(parents=True, exist_ok=True)

    def copy_and_customize_template(self, filename):
        """Copia e personalizza un singolo template"""
        source_file = self.source_templates / filename
        dest_file = self.dest_templates / filename
        
        if not source_file.exists():
            print(f"ATTENZIONE: File sorgente non trovato: {source_file}")
            return False
            
        try:
            # Leggi il contenuto originale
            with open(source_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Applica le sostituzioni
            modified_content = self.apply_replacements(content, filename)
            
            # Scrivi il file modificato
            with open(dest_file, 'w', encoding='utf-8') as f:
                f.write(modified_content)
                
            print(f"✓ Copiato e personalizzato: {filename}")
            return True
            
        except Exception as e:
            print(f"ERRORE durante la copia di {filename}: {e}")
            return False

    def apply_replacements(self, content, filename):
        """Applica le sostituzioni di testo al contenuto"""
        modified = content
        
        # Sostituzioni generiche
        for pattern, replacement in self.replacements.items():
            modified = re.sub(pattern, replacement, modified, flags=re.IGNORECASE)
        
        # Sostituzioni specifiche per _base.html
        if filename == "_base.html":
            modified = self.customize_base_template(modified)
            
        return modified

    def customize_base_template(self, content):
        """Personalizzazioni specifiche per il template base"""
        
        # Aggiungi/modifica il tag title nel head
        if '<title>' not in content:
            head_pattern = r'(<head[^>]*>)'
            content = re.sub(head_pattern, r'\1\n    <title>NINVENDO - A swap and market place for nintendo lovers</title>', content)
        
        # Cerca e sostituisci navbar brand
        navbar_patterns = [
            r'(<a[^>]*class[^>]*navbar-brand[^>]*>)[^<]*(</a>)',
            r'(<span[^>]*class[^>]*navbar-brand[^>]*>)[^<]*(</span>)',
            r'(<div[^>]*class[^>]*navbar-brand[^>]*>)[^<]*(</div>)'
        ]
        
        for pattern in navbar_patterns:
            content = re.sub(pattern, r'\1<strong>NINVENDO</strong>\2', content, flags=re.IGNORECASE)
        
        # Aggiungi meta description se non presente
        if 'meta name="description"' not in content:
            head_end = content.find('</head>')
            if head_end != -1:
                meta_tag = '    <meta name="description" content="NINVENDO - A swap and market place for nintendo lovers">\n'
                content = content[:head_end] + meta_tag + content[head_end:]
        
        # Sostituisci eventuali header principali
        h1_pattern = r'<h1[^>]*>([^<]*(?:classified|demo)[^<]*)</h1>'
        content = re.sub(h1_pattern, r'<h1>NINVENDO</h1>', content, flags=re.IGNORECASE)
        
        # Aggiungi sottotitolo se c'è un h1 NINVENDO senza sottotitolo
        if '<h1>NINVENDO</h1>' in content and 'nintendo lovers' not in content.lower():
            content = content.replace('<h1>NINVENDO</h1>', 
                                    '<h1>NINVENDO</h1>\n    <p class="lead">A swap and market place for nintendo lovers</p>')
        
        return content

    def update_settings_check(self):
        """Verifica e suggerisce modifiche per settings.py"""
        settings_file = self.project_root / "project" / "settings.py"
        
        if settings_file.exists():
            with open(settings_file, 'r', encoding='utf-8') as f:
                settings_content = f.read()
            
            # Verifica se TEMPLATES ha la configurazione corretta
            if "'DIRS': []" in settings_content or "os.path.join(BASE_DIR, 'templates')" not in settings_content:
                print("\n⚠️  ATTENZIONE: Potrebbe essere necessario aggiornare settings.py")
                print("Aggiungi questa configurazione in TEMPLATES['DIRS']:")
                print("    'DIRS': [os.path.join(BASE_DIR, 'templates')],")
        else:
            print(f"\n⚠️  File settings.py non trovato in: {settings_file}")

    def run(self):
        """Esegue la personalizzazione completa"""
        print("🎮 Iniziando personalizzazione template NINVENDO...")
        print(f"Directory progetto: {self.project_root}")
        print(f"Template sorgente: {self.source_templates}")
        print(f"Template destinazione: {self.dest_templates}")
        
        # Verifica che la directory sorgente esista
        if not self.source_templates.exists():
            print(f"❌ ERRORE: Directory template sorgente non trovata: {self.source_templates}")
            return False
        
        # Crea la struttura delle directory
        self.create_directory_structure()
        
        # Copia e personalizza ogni template
        success_count = 0
        for template_file in self.template_files:
            if self.copy_and_customize_template(template_file):
                success_count += 1
        
        # Verifica settings.py
        self.update_settings_check()
        
        print(f"\n✅ Personalizzazione completata!")
        print(f"   Template personalizzati: {success_count}/{len(self.template_files)}")
        print(f"   Template salvati in: {self.dest_templates}")
        print("\n📋 Prossimi passi:")
        print("   1. Verifica le modifiche ai template")
        print("   2. Controlla la configurazione in settings.py")
        print("   3. Esegui: python manage.py collectstatic --no-input")
        print("   4. Esegui: python manage.py runserver")
        
        return success_count == len(self.template_files)

def main():
    """Funzione principale"""
    customizer = NinvendoTemplateCustomizer()
    success = customizer.run()
    
    if success:
        print("\n🎉 Tutti i template sono stati personalizzati con successo!")
    else:
        print("\n⚠️  Alcuni template potrebbero non essere stati personalizzati correttamente.")
    
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())