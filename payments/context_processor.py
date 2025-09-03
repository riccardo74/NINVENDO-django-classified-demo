from django.conf import settings


def stripe_settings(request):
    """
    Context processor per rendere disponibili le impostazioni Stripe nei template
    """
    return {
        'STRIPE_PUBLIC_KEY': getattr(settings, 'STRIPE_PUBLIC_KEY', ''),
        'PLATFORM_FEE_PERCENTAGE': getattr(settings, 'PLATFORM_FEE_PERCENTAGE', 3.0),
    }