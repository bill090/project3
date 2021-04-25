from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

# Create your views here.

class Home(ListView):
    model = Product
    context_object_name = 'all_products_list'
    template_name = 'products/home.html'