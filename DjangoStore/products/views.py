from django.shortcuts import render
from django.views.generic import ListView
from django.template import Context
from .models import Product, Category

# Create your views here.

class Home(ListView):
    model = Product
    context_object_name = 'all_products_list'
    template_name = 'products/home.html'

# class CategoryView(ListView):
#     model = Product
#     context_object_name = 'cpu_products_list'
#     template_name = 'products/home.html'

def CategoryView(request, slug):
    category = Category.objects.filter(slug=slug)[0]
    products = Product.objects.filter(category=category)
    context = {"all_products_list": list(products)}
    return render(request, 'products/home.html', context)
