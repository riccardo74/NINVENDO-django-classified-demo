from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def calculate_total_with_fees(price):
    """Calcola il prezzo totale con commissioni"""
    try:
        item_price = Decimal(str(price))
        platform_fee = item_price * Decimal('0.03')  # 3%
        stripe_fee = (item_price * Decimal('0.014')) + Decimal('0.25')  # 1.4% + €0.25
        total = item_price + platform_fee + stripe_fee
        return f"{total:.2f}"
    except:
        return price

@register.filter
def calculate_fees_only(price):
    """Calcola solo le commissioni"""
    try:
        item_price = Decimal(str(price))
        platform_fee = item_price * Decimal('0.03')
        stripe_fee = (item_price * Decimal('0.014')) + Decimal('0.25')
        total_fees = platform_fee + stripe_fee
        return f"{total_fees:.2f}"
    except:
        return "0.00"

@register.filter
def multiply(value, arg):
    """Moltiplica due valori"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0