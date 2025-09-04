"""
Template tags e context per integrare Cloudinary nei template Django.
Mantiene tutte le funzioni originali, con fix e robustezza aggiuntiva.
"""

from django import template
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.conf import settings
from urllib.parse import urlparse
import logging

# Utilities del progetto (come nel file originale)
# - get_cloudinary_url(image_field, transformation)
# - get_optimized_image_tag(image_field, alt_text, css_class, transformation)
# - is_cloudinary_configured()
# - cloudinary_templatetag (decorator di guardia)
from ..cloudinary_utils import (
    get_cloudinary_url,
    get_optimized_image_tag,
    is_cloudinary_configured,
    cloudinary_templatetag,
)

register = template.Library()
logger = logging.getLogger(__name__)


# ----------------------------
# Helper interni (non esportati)
# ----------------------------

def _is_cloudinary_url(url: str) -> bool:
    if not url:
        return False
    try:
        return "res.cloudinary.com" in urlparse(url).netloc
    except Exception:
        return False


# ----------------------------
# Simple tags principali
# ----------------------------

@register.simple_tag
@cloudinary_templatetag
def cloudinary_url(image_field, transformation="medium"):
    """
    Genera URL Cloudinary per un'immagine.
    Uso: {% cloudinary_url item.image 'thumbnail' %}
    """
    return get_cloudinary_url(image_field, transformation) or ""


@register.simple_tag
@cloudinary_templatetag
def cloudinary_img(image_field, alt_text="", css_class="img-fluid", transformation="medium"):
    """
    Genera tag <img> ottimizzato con Cloudinary.
    Uso: {% cloudinary_img item.image "Descrizione" "img-fluid rounded" "large" %}
    """
    html = get_optimized_image_tag(image_field, alt_text, css_class, transformation)
    return mark_safe(html)


@register.simple_tag
@cloudinary_templatetag
def cloudinary_thumbnail(image_field, alt_text="", css_class="thumbnail"):
    """
    Genera thumbnail ottimizzata.
    Uso: {% cloudinary_thumbnail item.image "Thumbnail prodotto" %}
    """
    html = get_optimized_image_tag(image_field, alt_text, css_class, "thumbnail")
    return mark_safe(html)


@register.simple_tag
@cloudinary_templatetag
def cloudinary_background_img(image_field, css_class="hero-bg", transformation="large"):
    """
    Genera un DIV con background-image basato su Cloudinary.
    Uso: {% cloudinary_background_img hero.image "hero-section" "large" %}
    """
    if not image_field:
        return mark_safe(f'<div class="{css_class} no-bg-image"></div>')

    url = get_cloudinary_url(image_field, transformation) or getattr(image_field, "url", "")
    style = f"background-image: url({url}); background-size: cover; background-position: center;"
    return mark_safe(format_html('<div class="{}" style="{}"></div>', css_class, style))


@register.simple_tag(takes_context=True)
@cloudinary_templatetag
def cloudinary_share_image(context, image_field, transformation="large"):
    """
    Ritorna un URL assoluto adatto a Open Graph (og:image).
    - Se l'immagine è su Cloudinary: applica il preset.
    - Altrimenti: restituisce un URL assoluto al file esistente.
    Uso: {% cloudinary_share_image item.image "large" %}
    """
    if not image_field:
        return ""

    url = get_cloudinary_url(image_field, transformation)
    if not url:
        # fallback a URL del campo se non gestito da Cloudinary
        url = getattr(image_field, "url", "") or str(image_field) or ""

    # Per og:image vogliamo sempre un URL assoluto
    request = context.get("request")
    if request and url and not url.startswith(("http://", "https://")):
        try:
            url = request.build_absolute_uri(url)
        except Exception:
            # Ultimo fallback: se non riusciamo, restituiamo così com'è
            pass

    return url or ""


@register.simple_tag
def cloudinary_status():
    """
    Stato configurazione Cloudinary (stringa).
    Uso: {% cloudinary_status %}
    """
    return "✅ Configurato" if is_cloudinary_configured() else "❌ Non configurato"


# ----------------------------
# Filter
# ----------------------------

@register.filter
@cloudinary_templatetag
def cloudinary_transform(image_field, transformation):
    """
    Applica una trasformazione a un'immagine (ritorna URL).
    Uso: {{ item.image|cloudinary_transform:"thumbnail" }}
    """
    return get_cloudinary_url(image_field, transformation) or ""


# ----------------------------
# Tag responsive / gallery
# ----------------------------

@register.simple_tag
@cloudinary_templatetag
def cloudinary_responsive_img(
    image_field,
    alt_text="",
    css_class="img-responsive",
    sizes="(max-width: 768px) 100vw, 50vw",
):
    """
    Genera <img> responsive con srcset/sizes.
    Uso: {% cloudinary_responsive_img item.image "Prodotto" "img-fluid" "(max-width: 768px) 100vw, 50vw" %}
    """
    if not image_field:
        return mark_safe(
            f'<div class="no-image-placeholder {css_class}"><span class="text-muted">📷 Nessuna immagine</span></div>'
        )

    try:
        # URL base (preset 'medium' come nel file originale)
        base_url = get_cloudinary_url(image_field, "medium")
        if not base_url:
            # non Cloudinary → normale <img> lazy
            fallback = getattr(image_field, "url", "")
            return mark_safe(f'<img src="{fallback}" alt="{alt_text}" class="{css_class}" loading="lazy">')

        # Cloudinary configurato → srcset multiplo
        if is_cloudinary_configured():
            widths = [320, 480, 640, 800, 1024, 1200]
            srcset_urls = []

            # Costruzione tramite public_id per URL trasformati
            try:
                from cloudinary import CloudinaryImage
                import os
                if hasattr(image_field, "public_id") and image_field.public_id:
                    public_id = image_field.public_id
                else:
                    public_id = os.path.splitext(getattr(image_field, "name", ""))[0]
            except Exception:
                public_id = None

            if public_id:
                for w in widths:
                    ci = CloudinaryImage(public_id)
                    u = ci.build_url(width=w, crop="scale", quality="auto:good", format="auto")
                    srcset_urls.append(f"{u} {w}w")

            # Se per qualche motivo non siamo riusciti a generare srcset, cadiamo al solo base_url
            if srcset_urls:
                srcset = ", ".join(srcset_urls)
                return mark_safe(
                    format_html('<img src="{}" srcset="{}" sizes="{}" alt="{}" class="{}" loading="lazy">',
                                base_url, srcset, sizes, alt_text, css_class)
                )

        # fallback: singolo URL
        return mark_safe(format_html('<img src="{}" alt="{}" class="{}" loading="lazy">', base_url, alt_text, css_class))

    except Exception as e:
        logger.error(f"Errore cloudinary_responsive_img: {e}")
        fallback = getattr(image_field, "url", "")
        return mark_safe(f'<img src="{fallback}" alt="{alt_text}" class="{css_class}" loading="lazy">')


@register.inclusion_tag("cloudinary/image_gallery.html")
@cloudinary_templatetag
def cloudinary_gallery(images, thumbnail_class="col-md-3", lightbox=True):
    """
    Galleria immagini basata su Cloudinary.
    Uso: {% cloudinary_gallery item.images.all %}
    """
    return {
        "images": images,
        "thumbnail_class": thumbnail_class,
        "lightbox": lightbox,
        "cloudinary_configured": is_cloudinary_configured(),
    }


# ----------------------------
# Context processor (tenuto qui per retro-compatibilità)
# ----------------------------

def cloudinary_context(request):
    """
    Espone info Cloudinary in tutti i template.
    (Se preferisci, sposta questa funzione in project/context_processors.py)
    """
    cfg = getattr(settings, "CLOUDINARY_STORAGE", {}) or {}
    return {
        "CLOUDINARY_CONFIGURED": is_cloudinary_configured(),
        "CLOUDINARY_ACTIVE": bool(getattr(settings, "USE_CLOUDINARY", False)),
        "CLOUDINARY_CLOUD_NAME": cfg.get("CLOUD_NAME", ""),
        "CLOUDINARY_TRANSFORMATIONS": getattr(settings, "CLOUDINARY_TRANSFORMATIONS", {}),
    }
