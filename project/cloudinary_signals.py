"""
Signal handlers per gestire automaticamente upload/eliminazione immagini su Cloudinary
"""
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.conf import settings
import os
import logging

# Import dei modelli che hanno immagini
try:
    from django_classified.models import Item, ItemImage  # Se esiste un modello ItemImage
except ImportError:
    # Se non esiste ItemImage, usiamo solo Item
    from django_classified.models import Item
    ItemImage = None

from trade.models import TradeMessage  # Per le immagini nei messaggi

from .cloudinary_utils import (
    upload_image_to_cloudinary,
    delete_cloudinary_image,
    is_cloudinary_configured
)

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Item)
def handle_item_image_upload(sender, instance, created, **kwargs):
    """
    Gestisce upload automatico dell'immagine principale quando viene salvato un Item
    """
    if not is_cloudinary_configured():
        return
    
    # Solo in produzione (non in debug)
    if settings.DEBUG:
        return
    
    try:
        # Se c'è un'immagine e non è ancora stata processata
        if hasattr(instance, 'image') and instance.image:
            # Controlla se l'immagine è stata appena caricata
            if created or not hasattr(instance, '_cloudinary_processed'):
                
                # Genera public_id univoco
                public_id = f"items/item_{instance.pk}_{instance.slug}"
                
                # Upload su Cloudinary
                result = upload_image_to_cloudinary(
                    instance.image.file,
                    folder="items",
                    public_id=public_id
                )
                
                if result:
                    # Marca come processato
                    instance._cloudinary_processed = True
                    logger.info(f"Immagine Item {instance.pk} caricata su Cloudinary: {result['public_id']}")
                else:
                    logger.warning(f"Fallito upload Cloudinary per Item {instance.pk}")
                    
    except Exception as e:
        logger.error(f"Errore signal handler Item image delete: {e}")


@receiver(post_save, sender=TradeMessage)
def handle_trade_message_image_upload(sender, instance, created, **kwargs):
    """
    Gestisce upload automatico delle immagini nei messaggi di scambio
    """
    if not is_cloudinary_configured():
        return
    
    if settings.DEBUG:
        return
    
    try:
        # Se c'è un'immagine e il messaggio è appena stato creato
        if created and hasattr(instance, 'image') and instance.image:
            
            # Genera public_id univoco per il messaggio
            public_id = f"trade_messages/trade_{instance.trade.pk}/msg_{instance.pk}"
            
            # Upload su Cloudinary
            result = upload_image_to_cloudinary(
                instance.image.file,
                folder="trade_messages",
                public_id=public_id
            )
            
            if result:
                logger.info(f"Immagine TradeMessage {instance.pk} caricata su Cloudinary: {result['public_id']}")
            else:
                logger.warning(f"Fallito upload Cloudinary per TradeMessage {instance.pk}")
                
    except Exception as e:
        logger.error(f"Errore signal handler TradeMessage image upload: {e}")


@receiver(post_delete, sender=TradeMessage)
def handle_trade_message_image_delete(sender, instance, **kwargs):
    """
    Elimina immagine da Cloudinary quando viene eliminato un TradeMessage
    """
    if not is_cloudinary_configured():
        return
    
    if settings.DEBUG:
        return
    
    try:
        if hasattr(instance, 'image') and instance.image:
            # Ricostruisci public_id
            public_id = f"ninvendo/trade_messages/trade_{instance.trade.pk}/msg_{instance.pk}"
            
            success = delete_cloudinary_image(public_id)
            
            if success:
                logger.info(f"Immagine TradeMessage {instance.pk} eliminata da Cloudinary")
            else:
                logger.warning(f"Impossibile eliminare immagine TradeMessage {instance.pk} da Cloudinary")
                
    except Exception as e:
        logger.error(f"Errore signal handler TradeMessage image delete: {e}")


# Signal handler generico per modelli con immagini multiple (se necessario)
if ItemImage:  # Se esiste un modello per immagini multiple
    
    @receiver(post_save, sender=ItemImage)
    def handle_item_image_multiple_upload(sender, instance, created, **kwargs):
        """
        Gestisce upload di immagini multiple per un Item
        """
        if not is_cloudinary_configured() or settings.DEBUG:
            return
        
        try:
            if created and instance.image:
                public_id = f"items/item_{instance.item.pk}/image_{instance.pk}"
                
                result = upload_image_to_cloudinary(
                    instance.image.file,
                    folder="items",
                    public_id=public_id
                )
                
                if result:
                    logger.info(f"ItemImage {instance.pk} caricata su Cloudinary: {result['public_id']}")
                
        except Exception as e:
            logger.error(f"Errore signal handler ItemImage upload: {e}")
    
    
    @receiver(post_delete, sender=ItemImage)
    def handle_item_image_multiple_delete(sender, instance, **kwargs):
        """
        Elimina immagini multiple da Cloudinary
        """
        if not is_cloudinary_configured() or settings.DEBUG:
            return
        
        try:
            if instance.image:
                public_id = f"ninvendo/items/item_{instance.item.pk}/image_{instance.pk}"
                success = delete_cloudinary_image(public_id)
                
                if success:
                    logger.info(f"ItemImage {instance.pk} eliminata da Cloudinary")
                
        except Exception as e:
            logger.error(f"Errore signal handler ItemImage delete: {e}")


# Signal per ottimizzazione immagini esistenti
@receiver(pre_save, sender=Item)
def optimize_item_image_before_save(sender, instance, **kwargs):
    """
    Ottimizza immagini prima del salvataggio (solo per upload iniziali)
    """
    if not is_cloudinary_configured() or settings.DEBUG:
        return
    
    try:
        # Solo se è un nuovo oggetto o se l'immagine è cambiata
        if instance.pk is None:  # Nuovo oggetto
            if hasattr(instance, 'image') and instance.image:
                # Qui potresti aggiungere validazioni/ottimizzazioni pre-upload
                # Ad esempio, controllare dimensioni, formato, ecc.
                
                # Esempio: validazione dimensioni massime
                if hasattr(instance.image, 'file') and instance.image.file:
                    file_size = instance.image.file.size
                    max_size = getattr(settings, 'MAX_UPLOAD_SIZE', 10 * 1024 * 1024)  # 10MB
                    
                    if file_size > max_size:
                        raise ValueError(f"File troppo grande: {file_size/1024/1024:.1f}MB. Max: {max_size/1024/1024:.1f}MB")
                
                logger.debug(f"Pre-validazione immagine Item completata")
                
    except Exception as e:
        logger.error(f"Errore pre-save optimization: {e}")
        # Non bloccare il salvataggio per errori di ottimizzazione
        pass


def cleanup_orphaned_cloudinary_images():
    """
    Utility function per pulire immagini orfane su Cloudinary
    Può essere chiamata da un comando di gestione Django
    """
    if not is_cloudinary_configured():
        logger.warning("Cloudinary non configurato, cleanup saltato")
        return
    
    try:
        from .cloudinary_utils import get_folder_stats
        import cloudinary.api
        
        # Ottieni tutte le immagini dalla cartella ninvendo
        stats = get_folder_stats("ninvendo")
        
        if not stats:
            return
        
        orphaned_count = 0
        
        # Controlla ogni immagine se ha un corrispondente nel database
        for resource in stats['resources']:
            public_id = resource['public_id']
            
            # Estrai informazioni dal public_id
            if 'items/' in public_id:
                # Controlla se l'item esiste ancora
                try:
                    item_id = public_id.split('item_')[1].split('_')[0]
                    if not Item.objects.filter(pk=item_id).exists():
                        # Item non esiste più, elimina l'immagine
                        success = delete_cloudinary_image(public_id)
                        if success:
                            orphaned_count += 1
                            logger.info(f"Eliminata immagine orfana: {public_id}")
                except (IndexError, ValueError):
                    # Public ID non parsabile, salta
                    continue
            
            elif 'trade_messages/' in public_id:
                # Controlla se il messaggio esiste ancora
                try:
                    msg_id = public_id.split('msg_')[1]
                    if not TradeMessage.objects.filter(pk=msg_id).exists():
                        success = delete_cloudinary_image(public_id)
                        if success:
                            orphaned_count += 1
                            logger.info(f"Eliminata immagine messaggio orfana: {public_id}")
                except (IndexError, ValueError):
                    continue
        
        logger.info(f"Cleanup completato: {orphaned_count} immagini orfane eliminate")
        return orphaned_count
        
    except Exception as e:
        logger.error(f"Errore durante cleanup immagini orfane: {e}")
        return 0 signal handler Item image upload: {e}")


@receiver(post_delete, sender=Item)
def handle_item_image_delete(sender, instance, **kwargs):
    """
    Elimina immagine da Cloudinary quando viene eliminato un Item
    """
    if not is_cloudinary_configured():
        return
    
    if settings.DEBUG:
        return
    
    try:
        if hasattr(instance, 'image') and instance.image:
            # Estrai public_id dall'immagine
            if hasattr(instance.image, 'public_id'):
                public_id = instance.image.public_id
            else:
                # Ricostruisci public_id dal nome file
                public_id = f"ninvendo/items/item_{instance.pk}_{instance.slug}"
            
            success = delete_cloudinary_image(public_id)
            
            if success:
                logger.info(f"Immagine Item {instance.pk} eliminata da Cloudinary")
            else:
                logger.warning(f"Impossibile eliminare immagine Item {instance.pk} da Cloudinary")
                
    except Exception as e:
        logger.error(f"Errore