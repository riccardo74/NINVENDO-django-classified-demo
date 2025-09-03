"""
Template tags per integrare Cloudinary nei template Django
"""
from django import template
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from ..cloudinary_utils import (
    get_cloudinary_url,
    get_optimized_image_tag,
    is_cloudinary_configured,
    cloudinary_templatetag
)
import logging

register = template.Library()
logger = logging.getLogger(__name__)


@register.simple_tag
@cloudinary_templatetag
def cloudinary_url(image_field, transformation='medium'):
    """
    Genera URL Cloudinary per un'immagine
    
    Uso: {% cloudinary_url item.image 'thumbnail' %}
    """
    return get_cloudinary_url(image_field, transformation) or ''


@register.simple_tag
@cloudinary_templatetag
def cloudinary_img(image_field, alt_text="", css_class="img-fluid", transformation='medium'):
    """
    Genera tag <img> ottimizzato con Cloudinary
    
    Uso: {% cloudinary_img item.image "Descrizione" "img-fluid rounded" "large" %}
    """
    html = get_optimized_image_tag(image_field, alt_text, css_class, transformation)
    return mark_safe(html)


@register.simple_tag
@cloudinary_templatetag 
def cloudinary_thumbnail(image_field, alt_text="", css_class="thumbnail"):
    """
    Genera thumbnail ottimizzata
    
    Uso: {% cloudinary_thumbnail item.image "Thumbnail prodotto" %}
    """
    html = get_optimized_image_tag(image_field, alt_text, css_class, 'thumbnail')
    return mark_safe(html)


@register.simple_tag
@cloudinary_templatetag
def cloudinary_responsive_img(image_field, alt_text="", css_class="img-responsive", sizes="(max-width: 768px) 100vw, 50vw"):
    """
    Genera immagine completamente responsive con sizes attribute
    
    Uso: {% cloudinary_responsive_img item.image "Prodotto" "img-fluid" "(max-width: 768px) 100vw, 50vw" %}
    """
    if not image_field:
        return mark_safe(f'<div class="no-image-placeholder {css_class}"><span class="text-muted">📷 Nessuna immagine</span></div>')
    
    try:
        # URL base
        base_url = get_cloudinary_url(image_field, 'medium')
        if not base_url:
            return mark_safe(f'<img src="{image_field.url}" alt="{alt_text}" class="{css_class}" loading="lazy">')
        
        # Se Cloudinary configurato, crea srcset completo per responsive
        if is_cloudinary_configured():
            # Diverse larghezze per responsive breakpoints
            widths = [320, 480, 640, 800, 1024, 1200]
            srcset_urls = []
            
            for width in widths:
                # Usa l'utility per generare URL con larghezza specifica
                from cloudinary import CloudinaryImage
                import os
                
                if hasattr(image_field, 'public_id'):
                    public_id = image_field.public_id
                else:
                    public_id = os.path.splitext(image_field.name)[0]
                
                cloudinary_image = CloudinaryImage(public_id)
                url = cloudinary_image.build_url(
                    width=width,
                    crop='scale',
                    quality='auto:good',
                    format='auto'
                )
                srcset_urls.append(f"{url} {width}w")
            
            srcset = ", ".join(srcset_urls)
            
            return mark_safe(format_html(
                '<img src="{}" srcset="{}" sizes="{}" alt="{}" class="{}" loading="lazy">',
                base_url, srcset, sizes, alt_text, css_class
            ))
        else:
            return mark_safe(format_html(
                '<img src="{}" alt="{}" class="{}" loading="lazy">',
                base_url, alt_text, css_class
            ))
            
    except Exception as e:
        logger.error(f"Errore cloudinary_responsive_img: {e}")
        return mark_safe(f'<img src="{image_field.url}" alt="{alt_text}" class="{css_class}" loading="lazy">')


@register.inclusion_tag('cloudinary/image_gallery.html')
@cloudinary_templatetag
def cloudinary_gallery(images, thumbnail_class="col-md-3", lightbox=True):
    """
    Crea una galleria di immagini con Cloudinary
    
    Uso: {% cloudinary_gallery item.images.all %}
    """
    return {
        'images': images,
        'thumbnail_class': thumbnail_class,
        'lightbox': lightbox,
        'cloudinary_configured': is_cloudinary_configured()
    }


@register.simple_tag
def cloudinary_status():
    """
    Verifica stato configurazione Cloudinary
    
    Uso: {% cloudinary_status %}
    """
    return "✅ Configurato" if is_cloudinary_configured() else "❌ Non configurato"


@register.filter
@cloudinary_templatetag
def cloudinary_transform(image_field, transformation):
    """
    Filter per trasformazioni Cloudinary
    
    Uso: {{ item.image|cloudinary_transform:"thumbnail" }}
    """
    return get_cloudinary_url(image_field, transformation) or ''


@register.simple_tag
@cloudinary_templatetag
def cloudinary_background_img(image_field, css_class="hero-bg", transformation='large'):
    """
    Genera CSS per background-image con Cloudinary
    
    Uso: {% cloudinary_background_img hero.image "hero-section" "large" %}
    """
    if not image_field:
        return mark_safe(f'<div class="{css_class} no-bg-image"></div>')
    
    url = get_cloudinary_url(image_field, transformation)
    if not url:
        url = image_field.url
    
    style = f'background-image: url({url}); background-size: cover; background-position: center;'
    
    return mark_safe(format_html(
        '<div class="{}" style="{}"></div>',
        css_class, style
    ))


@register.simple_tag(takes_context=True)
@cloudinary_templatetag  
def cloudinary_share_image(context, image_field, transformation='large'):
    """
    Genera URL assoluto per condivisione social (Open Graph)
    
    Uso: {% cloudinary_share_image item.image "large" %}
    """
    if not image_field:
        return ""
    
    url = get_cloudinary_url(image_field, transformation)
    if not url:
        url = image_field.url
    
    # Converti in URL assoluto se necessario
    request = context.get('request')
    if request and not url.startswith('http'):
        url = request.build_absolute_uri(url)
    
    return url


# Template context processor
def cloudinary_context(request):
    """
    Context processor per aggiungere info Cloudinary in tutti i template
    """
    return {
        'CLOUDINARY_CONFIGURED': is_cloudinary_configured(),
        'CLOUDINARY_TRANSFORMATIONS': getattr(settings, 'CLOUDINARY_TRANSFORMATIONS', {})
    }