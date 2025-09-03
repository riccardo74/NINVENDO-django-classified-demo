# 📷 Cloudinary Integration - NINVENDO

Guida completa per configurare e utilizzare Cloudinary per la gestione delle immagini nel progetto NINVENDO.

## 🚀 Panoramica

Cloudinary è un servizio cloud per la gestione, ottimizzazione e distribuzione di immagini. Offre:

- **🔄 Ottimizzazione automatica** - Ridimensionamento, compressione, formato automatico
- **🌍 CDN globale** - Distribuzione veloce in tutto il mondo  
- **📱 Immagini responsive** - Adattamento automatico ai diversi device
- **🎨 Trasformazioni on-the-fly** - Ritaglio, filtri, effetti in tempo reale
- **💾 Storage sicuro** - Backup e ridondanza automatici

## 🛠️ Setup Cloudinary

### 1. Registrazione Account

1. Vai su [cloudinary.com](https://cloudinary.com)
2. Registra un account gratuito (25GB storage + 25GB traffico/mese)
3. Accedi al **Dashboard**

### 2. Ottenere le Credenziali

Dal dashboard Cloudinary copia:

```bash
Cloud Name: your_cloud_name
API Key: 123456789012345  
API Secret: your_api_secret
```

### 3. Configurazione Ambiente

Aggiungi al tuo file `.env`:

```bash
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### 4. Verifica Configurazione

```bash
python manage.py cloudinary_admin status
```

## 📋 Funzionalità Implementate

### 🎯 Template Tags

#### Immagine Ottimizzata Base
```html
{% load cloudinary_tags %}

<!-- Immagine responsive ottimizzata -->
{% cloudinary_img item.image "Descrizione" "img-fluid" "medium" %}
```

#### URL Cloudinary
```html
<!-- Solo URL per uso in CSS/JS -->
{% cloudinary_url item.image "large" %}
```

#### Thumbnail
```html
<!-- Thumbnail 150x150 -->
{% cloudinary_thumbnail item.image "Prodotto" "thumbnail-class" %}
```

#### Immagine Responsive Completa
```html
<!-- Con srcset per tutti i breakpoints -->
{% cloudinary_responsive_img item.image "Prodotto" "img-fluid" "(max-width: 768px) 100vw, 50vw" %}
```

#### Galleria Immagini
```html
<!-- Galleria con lightbox -->
{% cloudinary_gallery item.images.all "col-md-3" True %}
```

#### Background Image CSS
```html
<!-- Div con background-image ottimizzata -->
{% cloudinary_background_img hero.image "hero-section" "large" %}
```

### 🔧 Trasformazioni Predefinite

Configurate in `settings.py`:

```python
CLOUDINARY_TRANSFORMATIONS = {
    'thumbnail': {    # 150x150, ritagliata
        'width': 150,
        'height': 150,
        'crop': 'fill',
        'quality': 'auto:good',
        'format': 'auto'
    },
    'medium': {       # 400x300, adattata
        'width': 400,
        'height': 300, 
        'crop': 'fill',
        'quality': 'auto:good',
        'format': 'auto'
    },
    'large': {        # 800x600, preserva proporzioni
        'width': 800,
        'height': 600,
        'crop': 'fit',
        'quality': 'auto:best',
        'format': 'auto'
    }
}
```

### 🤖 Upload Automatico

Gli upload su Cloudinary avvengono automaticamente tramite **Django signals**:

- **Nuovi Item** → Upload immagine principale
- **Nuovi TradeMessage** → Upload immagine allegata
- **Eliminazione** → Cleanup automatico su Cloudinary

## 🎛️ Management Commands

### Status e Diagnostica

```bash
# Verifica configurazione
python manage.py cloudinary_admin status

# Statistiche utilizzo storage  
python manage.py cloudinary_admin stats

# Test connessione e upload
python manage.py cloudinary_admin test
```

### Migrazione Immagini

```bash
# Migra immagini esistenti su Cloudinary
python manage.py cloudinary_admin migrate --limit 100

# Simulazione senza upload reale
python manage.py cloudinary_admin migrate --dry-run --limit 10
```

### Pulizia Storage

```bash
# Rimuovi immagini orfane da Cloudinary
python manage.py cloudinary_admin cleanup

# Simulazione pulizia
python manage.py cloudinary_admin cleanup --dry-run

# Backup URL prima della pulizia
python manage.py cloudinary_admin backup
```

## 🏗️ Architettura del Sistema

### Flusso Upload

1. **Utente carica immagine** → Salvata localmente (sviluppo) o Cloudinary (produzione)
2. **Signal handler** → Upload automatico su Cloudinary (solo produzione)
3. **Template rendering** → URL ottimizzati tramite template tags
4. **Browser** → Carica immagini ottimizzate da CDN Cloudinary

### Storage Strategy

- **🛠️ Sviluppo**: Filesystem locale + template tags simulano Cloudinary
- **🚀 Produzione**: Upload diretto su Cloudinary + CDN delivery

### File Organization

```
ninvendo/                    # Cartella root su Cloudinary
├── items/                   # Immagini prodotti
│   ├── item_1_nintendo-switch/
│   └── item_2_pokemon-cards/
├── trade_messages/          # Immagini messaggi scambi
│   ├── trade_1/msg_1/
│   └── trade_1/msg_2/
└── test/                   # Immagini di test
```

## 🎨 Esempi Pratici

### Lista Prodotti con Thumbnail

```html
{% load cloudinary_tags %}

<div class="products-grid">
    {% for item in items %}
        <div class="product-card">
            <!-- Thumbnail ottimizzata 150x150 -->
            {% cloudinary_thumbnail item.image item.title "product-thumb" %}
            
            <h5>{{ item.title }}</h5>
            <p class="price">{{ item.price }}€</p>
        </div>
    {% endfor %}
</div>
```

### Dettaglio Prodotto Responsive

```html
{% load cloudinary_tags %}

<div class="product-detail">
    <!-- Immagine principale responsive -->
    <div class="main-image">
        {% cloudinary_responsive_img item.image item.title "img-fluid" "(max-width: 768px) 100vw, 60vw" %}
    </div>
    
    <!-- Galleria immagini aggiuntive -->
    {% if item.images.all %}
        <div class="image-gallery">
            {% cloudinary_gallery item.images.all "col-md-3" True %}
        </div>
    {% endif %}
</div>
```

### Meta Tag Open Graph

```html
{% load cloudinary_tags %}

<!-- Per condivisione social media -->
<meta property="og:image" content="{% cloudinary_share_image item.image 'large' %}" />
```

### Hero Section con Background

```html
{% load cloudinary_tags %}

<!-- Hero con background ottimizzata -->
{% cloudinary_background_img hero.image "hero-banner d-flex align-items-center justify-content-center" "hero" %}
    <div class="hero-content text-white text-center">
        <h1>Benvenuto su NINVENDO</h1>
        <p>Il marketplace per i fan di Nintendo</p>
    </div>
</div>

<style>
.hero-banner {
    min-height: 60vh;
    background-size: cover;
    background-position: center;
    position: relative;
}

.hero-banner::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0; 
    bottom: 0;
    background: rgba(0,0,0,0.4);
    z-index: 1;
}

.hero-content {
    position: relative;
    z-index: 2;
}
</style>
```

## 🔍 Debug e Troubleshooting

### Verifiche Comuni

```bash
# 1. Configurazione
python manage.py cloudinary_admin status

# 2. Test upload
python manage.py cloudinary_admin test

# 3. Verifica immagini nel database
python manage.py shell
>>> from django_classified.models import Item
>>> Item.objects.filter(image__isnull=False).count()
```

### Log di Debug

In `settings.py` per debug dettagliato:

```python
LOGGING = {
    'loggers': {
        'project.cloudinary_utils': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
```

### Problemi Comuni

| Problema | Soluzione |
|----------|-----------|
| Immagini non si caricano | Verifica credenziali Cloudinary |
| Upload lento | Controlla dimensioni immagini (max 10MB) |
| Template tag non funziona | Aggiungi `{% load cloudinary_tags %}` |
| Signal non triggera | Verifica `DEBUG=False` in produzione |

## 📊 Limiti Piano Gratuito

- **Storage**: 25GB
- **Traffico**: 25GB/mese  
- **Trasformazioni**: 25,000/mese
- **Richieste API**: 1,000/ora

Per utilizzo superiore considera upgrade a piano a pagamento.

## 🔐 Security Best Practices

1. **Credenziali** - Mai committare API secrets nel codice
2. **Validazione** - Controlla tipo/dimensioni file prima upload
3. **Rate Limiting** - Implementa limiti upload per utente
4. **Signed URLs** - Usa per contenuti privati (non implementato in questa versione)

## 🚀 Deploy in Produzione

### Variabili Ambiente

```bash
CLOUDINARY_CLOUD_NAME=your_production_cloud
CLOUDINARY_API_KEY=your_production_key  
CLOUDINARY_API_SECRET=your_production_secret
DEBUG=False
```

### Post-Deploy Checklist

1. ✅ Verifica configurazione: `cloudinary_admin status`
2. ✅ Test upload: `cloudinary_admin test`
3. ✅ Migra immagini esistenti: `cloudinary_admin migrate`
4. ✅ Setup monitoring utilizzo storage
5. ✅ Configura backup periodico URLs

## 📚 Risorse Utili

- [Cloudinary Documentation](https://cloudinary.com/documentation)
- [Django Cloudinary Storage](https://github.com/tiagomfreire/django-cloudinary-storage)
- [Cloudinary Transformation Reference](https://cloudinary.com/documentation/image_transformation_reference)
- [Responsive Images Guide](https://cloudinary.com/documentation/responsive_images)

---

💡 **Tip**: Usa sempre il comando `cloudinary_admin stats` per monitorare l'utilizzo e rimanere nei limiti del piano gratuito!