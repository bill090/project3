from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView
from django.template import Context
from django.http import HttpResponseRedirect
from .models import Product, Category

# Create your views here.

def Home(request):
    products = Product.objects.filter(featured=True)
    context = {"all_products_list": list(products)}
    return render(request, 'products/home.html', context)

def CategoryView(request, slug):
    category = Category.objects.filter(slug=slug)[0]
    products = Product.objects.filter(category=category)
    context = {"all_products_list": list(products)}
    return render(request, 'products/home.html', context)

def AllView(request):
    products = Product.objects.all()
    context = {"all_products_list": list(products)}
    return render(request, 'products/home.html', context)

def SearchView(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query)
    
    context = {"all_products_list": list(products)}

    return render(request, 'products/home.html', context)
