# -*- coding:utf-8 -*-
import os
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env(
    DEBUG=(bool, False),
    CACHE_URL=(str, 'locmemcache://'),
    EMAIL_URL=(str, 'consolemail://'),
    SECRET_KEY=(str, 'secret'),
    DATABASE_URL=(str, 'sqlite:///db.sqlite'),
)

env.read_env(str(os.path.join(BASE_DIR, ".env")))

DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')

ADMINS = (
    ('Demo Classified Admin', os.environ.get('ADMIN_EMAIL', 'admin@example.com')),
)

MANAGERS = ADMINS

# Expected comma separated string with the ALLOWED_HOSTS list
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1,.herokuapp.com').split(',')

# (Opzionale ma utile in deploy dietro proxy/Render per OAuth)
# Comma-separated, es: "https://nintendo-swap.onrender.com"
CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS', '').split(',') if os.environ.get('CSRF_TRUSTED_ORIGINS') else []

DATABASES = {
    'default': env.db(),
}

# Cache configuration for development
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'default-cache',
        'OPTIONS': {
            'MAX_ENTRIES': 1000,
            'CULL_FREQUENCY': 3,
        }
    }
}

# Local time zone for this installation.
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ============================================
# CONFIGURAZIONE CLOUDINARY PER IMMAGINI
# ============================================

# Configurazione Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUDINARY_CLOUD_NAME', default='your_cloud_name'),
    'API_KEY': env('CLOUDINARY_API_KEY', default='your_api_key'), 
    'API_SECRET': env('CLOUDINARY_API_SECRET', default='your_api_secret'),
    'SECURE': True,  # Usa HTTPS
}

# Solo se Cloudinary è configurato correttamente
if (CLOUDINARY_STORAGE['CLOUD_NAME'] != 'your_cloud_name' and 
    CLOUDINARY_STORAGE['API_KEY'] != 'your_api_key'):
    
    import cloudinary
    import cloudinary.uploader
    import cloudinary.api
    
    cloudinary.config(
        cloud_name=CLOUDINARY_STORAGE['CLOUD_NAME'],
        api_key=CLOUDINARY_STORAGE['API_KEY'],
        api_secret=CLOUDINARY_STORAGE['API_SECRET'],
        secure=CLOUDINARY_STORAGE['SECURE']
    )
    
    # Configurazioni Cloudinary avanzate
    CLOUDINARY_STORAGE.update({
        'FOLDER': 'ninvendo',  # Cartella principale
        'FORMAT': 'auto',      # Formato automatico (WebP quando possibile)
        'QUALITY': 'auto:best',  # Qualità automatica ottimizzata
        'FETCH_FORMAT': 'auto', # Formato di fetch automatico
        'FLAGS': 'progressive', # Caricamento progressivo
    })

# ============================================
# CONFIGURAZIONI CLOUDINARY TRASFORMAZIONI
# ============================================

# Preset di trasformazioni per diverse dimensioni
CLOUDINARY_TRANSFORMATIONS = {
    'thumbnail': {
        'width': 150,
        'height': 150,
        'crop': 'fill',
        'quality': 'auto:good',
        'format': 'auto'
    },
    'medium': {
        'width': 400, 
        'height': 300,
        'crop': 'fill',
        'quality': 'auto:good',
        'format': 'auto'
    },
    'large': {
        'width': 800,
        'height': 600,
        'crop': 'fit',
        'quality': 'auto:best',
        'format': 'auto'
    },
    'trade_message': {
        'width': 300,
        'height': 300,
        'crop': 'fit',
        'quality': 'auto:good',
        'format': 'auto'
    },
    'hero': {
        'width': 1200,
        'height': 400,
        'crop': 'fill',
        'quality': 'auto:best',
        'format': 'auto'
    }
}

# ============================================
# MEDIA E STATIC FILES
# ============================================

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"

# Absolute path to the directory static files should be collected to.
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like '/home/html/static' or 'C:/www/django/static'.
)

# Configurazioni upload immagini
MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10MB max per immagine
ALLOWED_IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.webp']

# Configurazione Storage - MANTENIAMO LA LOGICA ORIGINALE
# Usa Cloudinary per i MEDIA (file caricati dagli utenti) SOLO SE CONFIGURATO
if not DEBUG and (CLOUDINARY_STORAGE['CLOUD_NAME'] != 'your_cloud_name'):
    # PRODUZIONE: Cloudinary per media files se configurato
    DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
else:
    # SVILUPPO O CLOUDINARY NON CONFIGURATO: Filesystem locale
    DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

STORAGES = {
    "default": {
        "BACKEND": DEFAULT_FILE_STORAGE,
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

MIDDLEWARE = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

# 🔐 Backends: Google OAuth2 + username/password Django (e manteniamo Facebook se già configurato)
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',     # Google Login
    'social_core.backends.facebook.FacebookOAuth2', # (opzionale) Facebook già presente
    'django.contrib.auth.backends.ModelBackend',    # Username/Password nativo Django
)

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Social Auth context processors
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',

                # Django Classified context processors
                'django_classified.context_processors.common_values',
                
                # ⭐ CLOUDINARY CONTEXT PROCESSOR (se necessario)
                'project.context_processors.site_config',
                'project.templatetags.cloudinary_tags.cloudinary_context',
            ],
            'debug': True
        },
    },
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.staticfiles',  # ⭐ AGGIUNTO - era mancante!

    'bootstrapform',
    'sorl.thumbnail',
    'django_classified',
    'social_django',

    # ⭐ MODULI ESSENZIALI PER BARATTO
    'crispy_forms',         # django-crispy-forms
    'crispy_bootstrap4',    # crispy bootstrap4 template pack
    'widget_tweaks',        # django-widget-tweaks
    'django_extensions',    # utilities per sviluppo

    # ⭐ CLOUDINARY SUPPORT - ORDINE CORRETTO
    'cloudinary_storage',   # DEVE essere prima di cloudinary
    'cloudinary',          # cloudinary

    'demo',
    'registration',  
    "trade",
    'payments',
    
    # ⭐ PROJECT APP (per management commands e utilities) - SE NECESSARIO
    'project',
]

# ⭐ CONFIGURAZIONI CRISPY FORMS
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

# Email per notifiche (già presente, assicuriamoci sia configurato)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # development
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # production

ACCOUNT_ACTIVATION_DAYS = 7  # per backend 'default' (con email)

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = '/'

DCF_SITE_NAME = 'NinVendo : a place for NinTendo lovers'

# ---- Social Auth: Google (aggiunto) ----
# Imposta questi valori nell'ambiente (.env o Render env)
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

# Se sei dietro proxy/https terminato a monte (es. Render), abilita il redirect HTTPS:
# In locale lascialo False; in produzione metti env SOCIAL_AUTH_REDIRECT_IS_HTTPS=true
SOCIAL_AUTH_REDIRECT_IS_HTTPS = env.bool('SOCIAL_AUTH_REDIRECT_IS_HTTPS', default=False)

# ---- Social Auth: Facebook (già presente, opzionale) ----
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}

SOCIAL_AUTH_EMAIL_FORM_HTML = 'demo/email_signup.html'  # ⭐ MANTENUTO ORIGINALE
SOCIAL_AUTH_EMAIL_VALIDATION_URL = '/email-sent/'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.mail.mail_validation',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.debug.debug',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.debug.debug'
)

DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'demo@example.com')  # ⭐ MANTENUTO ORIGINALE

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Configure email Backend via EMAIL_URL
vars().update(env.email_url())

DCF_CURRENCY = 'EUR'
DCF_DISPLAY_EMPTY_GROUPS = True
GOOGLE_ANALYTICS_PROPERTY_ID = os.environ.get('GOOGLE_ANALYTICS_PROPERTY_ID')

# ============================================
# CONFIGURAZIONE STRIPE PAGAMENTI
# ============================================

# Configurazione per testing (sostituisci con chiavi reali)
STRIPE_PUBLIC_KEY = env('STRIPE_PUBLIC_KEY', default='pk_test_placeholder')
STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY', default='sk_test_placeholder') 
STRIPE_WEBHOOK_SECRET = env('STRIPE_WEBHOOK_SECRET', default='whsec_placeholder')

# Dominio per redirect Stripe
STRIPE_DOMAIN = env('STRIPE_DOMAIN', default='http://127.0.0.1:8000')

# Commissioni
PLATFORM_FEE_PERCENTAGE = env.float('PLATFORM_FEE_PERCENTAGE', default=3.0)
STRIPE_FEE_PERCENTAGE = env.float('STRIPE_FEE_PERCENTAGE', default=1.4)
STRIPE_FEE_FIXED_CENTS = env.int('STRIPE_FEE_FIXED_CENTS', default=25)

# ============================================
# LOGGING CONFIGURATION (OPZIONALE)
# ============================================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'cloudinary': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

# Crea directory logs se non esiste (opzionale)
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR, exist_ok=True)