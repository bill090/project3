from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Cart
from products.models import Product
from django.contrib import messages

# Create your views here.

def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    cart, created = Cart.objects.get_or_create(
        item=item,
        user=request.user
    )
    if created:
        cart.quantity = 1
        cart.save()
        messages.info(request, f"{cart.item.name} has been added to your cart.")
    else:
        cart.quantity += 1
        cart.save()
        messages.info(request, f"{cart.item.name} quantity has been updated")

    return redirect("mainapp:home")

def increase_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    cart_qs = Cart.objects.filter(user=request.user, item=item)
    if cart_qs.exists():
        cart = cart_qs[0]
        cart.quantity += 1
        cart.save()
        messages.info(request, f"{item.name} quantity has updated.")
    else:
        messages.warning(request, "This item was not in your cart")
    return redirect("mainapp:cart-home")

def decrease_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    cart_qs = Cart.objects.filter(user=request.user, item=item)
    if cart_qs.exists():
        cart = cart_qs[0]
        # Checking the cart quantity
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
            messages.info(request, f"{item.name} quantity has updated.")
        else:
            cart.delete()
            messages.info(request, "This item was removed from your cart.")
    else:
        messages.warning(request, "This item was not in your cart")
    return redirect("mainapp:cart-home")

class CartListView(ListView):
    model = Cart
    template_name = 'cart/home.html'
    context_object_name = 'cart_list'
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)