from datetime import datetime, timedelta
from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderdate = models.DateTimeField(auto_now_add=True, blank=True)
    shippingdate = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)

    def __str__(self):
        return self.orderdate.strftime("%b.%d,%Y,%I:%M %p")

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()