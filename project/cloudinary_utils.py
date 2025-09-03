"""
Utilities per gestire Cloudinary nel progetto NINVENDO
"""
import os
from django.conf import settings
from django.utils.html import format_html
from django.template.loader import render_to_string
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary import CloudinaryImage
import logging

logger = logging.getLogger(__name__)


def is_cloudinary_configured():
    """Verifica se Cloudinary è configurato correttamente"""
    try:
        cloud_name = getattr(settings, 'CLOUDINARY_STORAGE', {}).get('CLOUD_NAME')
        api_key = getattr(settings, 'CLOUDINARY_STORAGE', {}).get('API_KEY')
        api_secret = getattr(settings, 'CLOUDINARY_STORAGE', {}).get('API_SECRET')
        
        return all([cloud_name, api_key, api_secret]) and \
               cloud_name != 'your_cloud_name' and \
               api_key != 'your_api_key'
    except:
        return False


def get_cloudinary_url(image_field, transformation='medium'):
    """
    Genera URL Cloudinary per un'immagine con trasformazioni
    
    Args:
        image_field: Campo immagine del modello Django
        transformation: Nome della trasformazione (da settings.CLOUDINARY_TRANSFORMATIONS)
    
    Returns:
        str: URL dell'immagine trasformata
    """
    if not image_field:
        return None
        
    # Se non è configurato Cloudinary, usa URL normale
    if not is_cloudinary_configured():
        return image_field.url if hasattr(image_field, 'url') else None
    
    try:
        # Estrai public_id dal percorso
        if hasattr(image_field, 'public_id'):
            public_id = image_field.public_id
        elif hasattr(image_field, 'name'):
            # Per campi FileField, estrai il public_id dal name
            public_id = os.path.splitext(image_field.name)[0]
        else:
            return image_field.url if hasattr(image_field, 'url') else None
            
        # Ottieni parametri di trasformazione
        transform_params = settings.CLOUDINARY_TRANSFORMATIONS.get(
            transformation, 
            settings.CLOUDINARY_TRANSFORMATIONS['medium']
        )
        
        # Crea CloudinaryImage e genera URL
        cloudinary_image = CloudinaryImage(public_id)
        return cloudinary_image.build_url(**transform_params)
        
    except Exception as e:
        logger.warning(f"Errore generazione URL Cloudinary: {e}")
        return image_field.url if hasattr(image_field, 'url') else None


def get_optimized_image_tag(image_field, alt_text="", css_class="", transformation='medium'):
    """
    Genera tag HTML <img> ottimizzato con srcset per responsive images
    
    Args:
        image_field: Campo immagine
        alt_text: Testo alternativo
        css_class: Classi CSS
        transformation: Trasformazione base
    
    Returns:
        str: Tag HTML completo
    """
    if not image_field:
        return format_html(
            '<div class="no-image-placeholder {}">'
            '<span class="text-muted">📷 Nessuna immagine</span>'
            '</div>',
            css_class
        )
    
    try:
        base_url = get_cloudinary_url(image_field, transformation)
        if not base_url:
            # Fallback per sviluppo locale
            return format_html(
                '<img src="{}" alt="{}" class="{}" loading="lazy">',
                image_field.url, alt_text, css_class
            )
        
        # Se Cloudinary è configurato, crea srcset responsive
        if is_cloudinary_configured():
            # Genera diverse risoluzioni
            srcset_urls = []
            base_transform = settings.CLOUDINARY_TRANSFORMATIONS.get(transformation, {})
            base_width = base_transform.get('width', 400)
            
            # Crea varianti per diversi device pixel ratio
            for dpr in [1, 1.5, 2]:
                width = int(base_width * dpr)
                transform_params = base_transform.copy()
                transform_params['width'] = width
                transform_params['dpr'] = dpr
                
                if hasattr(image_field, 'public_id'):
                    public_id = image_field.public_id
                else:
                    public_id = os.path.splitext(image_field.name)[0]
                
                cloudinary_image = CloudinaryImage(public_id)
                url = cloudinary_image.build_url(**transform_params)
                srcset_urls.append(f"{url} {dpr}x")
            
            srcset = ", ".join(srcset_urls)
            
            return format_html(
                '<img src="{}" srcset="{}" alt="{}" class="{}" loading="lazy">',
                base_url, srcset, alt_text, css_class
            )
        else:
            return format_html(
                '<img src="{}" alt="{}" class="{}" loading="lazy">',
                base_url, alt_text, css_class
            )
            
    except Exception as e:
        logger.error(f"Errore generazione tag immagine: {e}")
        # Fallback sicuro
        return format_html(
            '<img src="{}" alt="{}" class="{}" loading="lazy">',
            image_field.url if hasattr(image_field, 'url') else '',
            alt_text, css_class
        )


def upload_image_to_cloudinary(image_file, folder="items", public_id=None):
    """
    Carica un'immagine su Cloudinary con ottimizzazioni
    
    Args:
        image_file: File immagine da caricare
        folder: Cartella di destinazione su Cloudinary
        public_id: ID pubblico personalizzato (opzionale)
    
    Returns:
        dict: Risultato upload Cloudinary
    """
    if not is_cloudinary_configured():
        logger.warning("Cloudinary non configurato, upload saltato")
        return None
    
    try:
        upload_options = {
            'folder': f"ninvendo/{folder}",
            'use_filename': True,
            'unique_filename': True if not public_id else False,
            'overwrite': False,
            'quality': 'auto:best',
            'format': 'auto',
            'flags': 'progressive',
            'transformation': [
                {'quality': 'auto:good'},
                {'fetch_format': 'auto'}
            ]
        }
        
        if public_id:
            upload_options['public_id'] = public_id
        
        result = cloudinary.uploader.upload(image_file, **upload_options)
        
        logger.info(f"Immagine caricata su Cloudinary: {result.get('public_id')}")
        return result
        
    except Exception as e:
        logger.error(f"Errore upload Cloudinary: {e}")
        return None


def delete_cloudinary_image(public_id):
    """
    Elimina un'immagine da Cloudinary
    
    Args:
        public_id: ID pubblico dell'immagine da eliminare
    
    Returns:
        bool: True se eliminata con successo
    """
    if not is_cloudinary_configured() or not public_id:
        return False
    
    try:
        result = cloudinary.uploader.destroy(public_id)
        success = result.get('result') == 'ok'
        
        if success:
            logger.info(f"Immagine eliminata da Cloudinary: {public_id}")
        else:
            logger.warning(f"Immagine non trovata su Cloudinary: {public_id}")
        
        return success
        
    except Exception as e:
        logger.error(f"Errore eliminazione Cloudinary: {e}")
        return False


def get_folder_stats(folder_path="ninvendo"):
    """
    Ottieni statistiche su una cartella Cloudinary
    
    Args:
        folder_path: Percorso della cartella
    
    Returns:
        dict: Statistiche della cartella
    """
    if not is_cloudinary_configured():
        return None
    
    try:
        # Ottieni informazioni sulla cartella
        result = cloudinary.api.resources(
            type="upload",
            prefix=folder_path,
            max_results=500
        )
        
        total_resources = result.get('total_count', 0)
        resources = result.get('resources', [])
        total_bytes = sum(r.get('bytes', 0) for r in resources)
        
        return {
            'total_images': total_resources,
            'total_size_mb': round(total_bytes / (1024 * 1024), 2),
            'resources': resources
        }
        
    except Exception as e:
        logger.error(f"Errore statistiche Cloudinary: {e}")
        return None


# Decorator per template tags
def cloudinary_templatetag(func):
    """Decorator per template tags che usano Cloudinary"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Errore template tag Cloudinary: {e}")
            return ""
    return wrapper