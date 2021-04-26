from django.urls import path
from .views import Home, CategoryView
from cart.views import add_to_cart, CartListView, increase_cart, decrease_cart

app_name = 'mainapp'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('list/<slug>', CategoryView, name='list'),
    path('cart/<slug>', add_to_cart, name='cart'),
    path('increase/<slug>', increase_cart, name='increase-cart'),
    path('decrease/<slug>', decrease_cart, name='decrease-cart'),
    path('cart/', CartListView.as_view(), name='cart-home'),
]