"""
Management command per amministrare Cloudinary
Uso: python manage.py cloudinary_admin [comando] [opzioni]
"""
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db import transaction
import sys
import os

# Import delle utility Cloudinary
try:
    from project.cloudinary_utils import (
        is_cloudinary_configured,
        get_folder_stats,
        delete_cloudinary_image,
        upload_image_to_cloudinary
    )
    from project.cloudinary_signals import cleanup_orphaned_cloudinary_images
except ImportError as e:
    print(f"⚠️ Import error: {e}")
    # Fallback imports
    pass

from django_classified.models import Item
from trade.models import TradeMessage


class Command(BaseCommand):
    help = """
    Amministra Cloudinary per NINVENDO
    
    Comandi disponibili:
      status      - Mostra stato configurazione Cloudinary
      stats       - Statistiche utilizzo storage
      cleanup     - Rimuove immagini orfane
      migrate     - Migra immagini esistenti su Cloudinary
      test        - Testa configurazione con upload di prova
      backup      - Backup URLs immagini esistenti
    """
    
    def add_arguments(self, parser):
        parser.add_argument(
            'command',
            type=str,
            help='Comando da eseguire: status, stats, cleanup, migrate, test, backup'
        )
        
        parser.add_argument(
            '--force',
            action='store_true',
            help='Forza operazione senza conferma'
        )
        
        parser.add_argument(
            '--limit',
            type=int,
            default=100,
            help='Limite oggetti da processare (default: 100)'
        )
        
        parser.add_argument(
            '--folder',
            type=str,
            default='ninvendo',
            help='Cartella Cloudinary target (default: ninvendo)'
        )
        
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Simula operazione senza eseguirla'
        )
    
    def handle(self, *args, **options):
        command = options['command'].lower()
        
        # Dispatcher dei comandi
        command_map = {
            'status': self.handle_status,
            'stats': self.handle_stats,
            'cleanup': self.handle_cleanup,
            'migrate': self.handle_migrate,
            'test': self.handle_test,
            'backup': self.handle_backup,
        }
        
        if command not in command_map:
            raise CommandError(f"Comando non riconosciuto: {command}")
        
        try:
            command_map[command](options)
        except Exception as e:
            raise CommandError(f"Errore esecuzione comando '{command}': {e}")
    
    def handle_status(self, options):
        """Mostra stato configurazione Cloudinary"""
        self.stdout.write(self.style.HTTP_INFO("=== STATUS CLOUDINARY ==="))
        
        # Verifica configurazione
        configured = is_cloudinary_configured()
        status_icon = "✅" if configured else "❌"
        
        self.stdout.write(f"{status_icon} Configurazione: {'OK' if configured else 'MANCANTE'}")
        
        if configured:
            # Mostra dettagli configurazione (senza credenziali sensibili)
            cloudinary_settings = getattr(settings, 'CLOUDINARY_STORAGE', {})
            cloud_name = cloudinary_settings.get('CLOUD_NAME', 'N/A')
            
            self.stdout.write(f"🏷️  Cloud Name: {cloud_name}")
            self.stdout.write(f"🔐 API Key: {'***' + cloudinary_settings.get('API_KEY', '')[-4:] if cloudinary_settings.get('API_KEY') else 'N/A'}")
            self.stdout.write(f"🔧 Secure: {cloudinary_settings.get('SECURE', False)}")
            
            # Verifica storage backend
            storage_backend = getattr(settings, 'DEFAULT_FILE_STORAGE', 'N/A')
            self.stdout.write(f"💾 Storage Backend: {storage_backend}")
            
            # Debug mode
            debug_icon = "🛠️" if settings.DEBUG else "🚀"
            self.stdout.write(f"{debug_icon} Modalità: {'Sviluppo' if settings.DEBUG else 'Produzione'}")
            
        else:
            self.stdout.write(self.style.WARNING("⚠️  Cloudinary non configurato"))
            self.stdout.write("Imposta le variabili d'ambiente:")
            self.stdout.write("  CLOUDINARY_CLOUD_NAME=your_cloud_name")
            self.stdout.write("  CLOUDINARY_API_KEY=your_api_key") 
            self.stdout.write("  CLOUDINARY_API_SECRET=your_api_secret")
    
    def handle_stats(self, options):
        """Mostra statistiche utilizzo"""
        self.stdout.write(self.style.HTTP_INFO("=== STATISTICHE CLOUDINARY ==="))
        
        if not is_cloudinary_configured():
            self.stdout.write(self.style.ERROR("❌ Cloudinary non configurato"))
            return
        
        folder = options['folder']
        stats = get_folder_stats(folder)
        
        if not stats:
            self.stdout.write(self.style.WARNING("⚠️ Impossibile ottenere statistiche"))
            return
        
        self.stdout.write(f"📁 Cartella: {folder}")
        self.stdout.write(f"📷 Totale immagini: {stats['total_images']}")
        self.stdout.write(f"💾 Dimensione totale: {stats['total_size_mb']} MB")
        
        # Statistiche dettagliate per sottocartelle
        subcategories = {}
        for resource in stats['resources'][:20]:  # Primi 20 per non sovraccaricare
            public_id = resource['public_id']
            if '/' in public_id:
                category = public_id.split('/')[1] if public_id.count('/') > 1 else 'root'
                subcategories[category] = subcategories.get(category, 0) + 1
        
        if subcategories:
            self.stdout.write("\n📂 Breakdown per categoria:")
            for category, count in subcategories.items():
                self.stdout.write(f"  {category}: {count} immagini")
        
        # Conta immagini nel database locale
        items_with_images = Item.objects.exclude(image='').count()
        trade_messages_with_images = TradeMessage.objects.exclude(image='').count()
        
        self.stdout.write(f"\n🗃️  Database locale:")
        self.stdout.write(f"  Items con immagini: {items_with_images}")
        self.stdout.write(f"  Trade messages con immagini: {trade_messages_with_images}")
        
        total_db_images = items_with_images + trade_messages_with_images
        self.stdout.write(f"  Totale: {total_db_images}")
        
        # Differenza
        diff = stats['total_images'] - total_db_images
        if diff > 0:
            self.stdout.write(self.style.WARNING(f"⚠️ Possibili {diff} immagini orfane su Cloudinary"))
        elif diff < 0:
            self.stdout.write(self.style.WARNING(f"⚠️ {abs(diff)} immagini non migrate su Cloudinary"))
    
    def handle_cleanup(self, options):
        """Rimuove immagini orfane"""
        self.stdout.write(self.style.HTTP_INFO("=== CLEANUP IMMAGINI ORFANE ==="))
        
        if not is_cloudinary_configured():
            self.stdout.write(self.style.ERROR("❌ Cloudinary non configurato"))
            return
        
        if not options['force'] and not options['dry_run']:
            confirm = input("⚠️  Questa operazione eliminerà immagini da Cloudinary. Continuare? (y/N): ")
            if confirm.lower() != 'y':
                self.stdout.write("Operazione annullata.")
                return
        
        if options['dry_run']:
            self.stdout.write(self.style.WARNING("🧪 MODALITÀ DRY-RUN - Nessuna eliminazione effettuata"))
        
        # Esegui cleanup
        try:
            if options['dry_run']:
                # Simula cleanup (implementa versione dry-run se necessario)
                self.stdout.write("🔍 Analisi immagini orfane...")
                # TODO: Implementa logica dry-run
                orphaned_count = 0
            else:
                orphaned_count = cleanup_orphaned_cloudinary_images()
            
            if orphaned_count > 0:
                self.stdout.write(self.style.SUCCESS(f"✅ {orphaned_count} immagini orfane eliminate"))
            else:
                self.stdout.write("ℹ️  Nessuna immagine orfana trovata")
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Errore durante cleanup: {e}"))
    
    def handle_migrate(self, options):
        """Migra immagini esistenti su Cloudinary"""
        self.stdout.write(self.style.HTTP_INFO("=== MIGRAZIONE IMMAGINI ==="))
        
        if not is_cloudinary_configured():
            self.stdout.write(self.style.ERROR("❌ Cloudinary non configurato"))
            return
        
        limit = options['limit']
        dry_run = options['dry_run']
        
        if dry_run:
            self.stdout.write(self.style.WARNING("🧪 MODALITÀ DRY-RUN"))
        
        # Migra immagini Items
        self.stdout.write("🔄 Migrazione immagini Items...")
        items = Item.objects.exclude(image='')[:limit]
        
        migrated_items = 0
        for item in items:
            try:
                if not dry_run:
                    public_id = f"items/item_{item.pk}_{item.slug}"
                    result = upload_image_to_cloudinary(
                        item.image.file,
                        folder="items",
                        public_id=public_id
                    )
                    
                    if result:
                        migrated_items += 1
                        self.stdout.write(f"  ✅ Item {item.pk}: {item.title[:30]}...")
                    else:
                        self.stdout.write(f"  ❌ Errore Item {item.pk}")
                else:
                    migrated_items += 1
                    self.stdout.write(f"  🧪 Item {item.pk}: {item.title[:30]}... (simulato)")
                    
            except Exception as e:
                self.stdout.write(f"  ❌ Errore Item {item.pk}: {e}")
        
        # Migra immagini TradeMessage
        self.stdout.write("🔄 Migrazione immagini Trade Messages...")
        trade_messages = TradeMessage.objects.exclude(image='')[:limit]
        
        migrated_messages = 0
        for msg in trade_messages:
            try:
                if not dry_run:
                    public_id = f"trade_messages/trade_{msg.trade.pk}/msg_{msg.pk}"
                    result = upload_image_to_cloudinary(
                        msg.image.file,
                        folder="trade_messages",
                        public_id=public_id
                    )
                    
                    if result:
                        migrated_messages += 1
                        self.stdout.write(f"  ✅ Message {msg.pk}")
                    else:
                        self.stdout.write(f"  ❌ Errore Message {msg.pk}")
                else:
                    migrated_messages += 1
                    self.stdout.write(f"  🧪 Message {msg.pk} (simulato)")
                    
            except Exception as e:
                self.stdout.write(f"  ❌ Errore Message {msg.pk}: {e}")
        
        # Riepilogo
        total_migrated = migrated_items + migrated_messages
        self.stdout.write(self.style.SUCCESS(f"\n✅ Migrazione completata:"))
        self.stdout.write(f"  📦 Items: {migrated_items}")
        self.stdout.write(f"  💬 Messages: {migrated_messages}")
        self.stdout.write(f"  📊 Totale: {total_migrated}")
    
    def handle_test(self, options):
        """Testa configurazione Cloudinary"""
        self.stdout.write(self.style.HTTP_INFO("=== TEST CLOUDINARY ==="))
        
        if not is_cloudinary_configured():
            self.stdout.write(self.style.ERROR("❌ Cloudinary non configurato"))
            return
        
        try:
            # Test connessione API
            import cloudinary.api
            
            self.stdout.write("🔍 Test connessione API...")
            api_info = cloudinary.api.ping()
            
            if api_info.get('status') == 'ok':
                self.stdout.write("✅ Connessione API OK")
            else:
                self.stdout.write(self.style.ERROR("❌ Connessione API fallita"))
                return
            
            # Test upload (immagine di prova)
            if not options['dry_run']:
                self.stdout.write("🔄 Test upload immagine...")
                
                # Crea immagine di test temporanea
                from PIL import Image
                import io
                import tempfile
                
                # Crea immagine 100x100 rossa
                img = Image.new('RGB', (100, 100), color='red')
                img_buffer = io.BytesIO()
                img.save(img_buffer, format='PNG')
                img_buffer.seek(0)
                
                # Upload di test
                result = upload_image_to_cloudinary(
                    img_buffer,
                    folder="test",
                    public_id="test_upload"
                )
                
                if result:
                    self.stdout.write("✅ Upload test OK")
                    
                    # Cleanup test image
                    delete_success = delete_cloudinary_image(result['public_id'])
                    if delete_success:
                        self.stdout.write("✅ Cleanup test OK")
                    else:
                        self.stdout.write("⚠️ Cleanup test parzialmente fallito")
                else:
                    self.stdout.write(self.style.ERROR("❌ Upload test fallito"))
            else:
                self.stdout.write("🧪 Test upload saltato (dry-run)")
            
            self.stdout.write(self.style.SUCCESS("🎉 Test Cloudinary completato con successo!"))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Test fallito: {e}"))
    
    def handle_backup(self, options):
        """Backup URLs immagini esistenti"""
        self.stdout.write(self.style.HTTP_INFO("=== BACKUP URLS IMMAGINI ==="))
        
        backup_file = "cloudinary_backup_urls.txt"
        
        try:
            with open(backup_file, 'w') as f:
                f.write("# Backup URLs immagini NINVENDO\n")
                f.write(f"# Generato il {__import__('datetime').datetime.now()}\n\n")
                
                # Backup Items
                f.write("## ITEMS ##\n")
                for item in Item.objects.exclude(image=''):
                    f.write(f"Item {item.pk}: {item.image.url}\n")
                
                # Backup TradeMessages
                f.write("\n## TRADE MESSAGES ##\n")
                for msg in TradeMessage.objects.exclude(image=''):
                    f.write(f"TradeMessage {msg.pk}: {msg.image.url}\n")
            
            self.stdout.write(self.style.SUCCESS(f"✅ Backup salvato in: {backup_file}"))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Errore backup: {e}"))