from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.quantity} of {self.item.name}'
        
    def get_total(self):
        total = self.item.price * self.quantity
        return total
        
    @classmethod
    def get_cart_quantity(cls,user):
        total_quantity = 0
        items = Cart.objects.filter(user=user)
        if items.exists():
            for item in items:
                total_quantity += item.quantity
        return total_quantity

    @classmethod
    def get_cart_sum(cls,user):
        sum = 0.0
        items = Cart.objects.filter(user=user)
        if items.exists():
            for item in items:
                sum += item.get_total()
        return sum