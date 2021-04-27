from django.contrib import admin
from .models import OrderItem, Order

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'orderdate', 'shippingdate', 'address', 'city', 'province', 'postal_code')
    
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'item', 'quantity', 'price')