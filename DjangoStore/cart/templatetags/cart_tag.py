from django import template
from cart.models import Cart
register = template.Library()
@register.filter
def cart_total_quantity(user):
    return Cart.get_cart_quantity(user)
@register.filter
def cart_total_sum(user):
    return Cart.get_cart_sum(user)