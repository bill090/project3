from django.contrib import admin
from .models import OrderItem, Order

# Register your models here.

admin.register(Order)
admin.register(OrderItem)