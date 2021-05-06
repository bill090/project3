from django.urls import path
from .views import Home, CategoryView, AllView, SearchView
from cart.views import add_to_cart, CartListView, increase_cart, decrease_cart, checkoutFormView, checkoutView
from orders.views import OrderCreateView, OrderCompleteView, OrderShowView, OrderDetailView

app_name = 'mainapp'

urlpatterns = [
    path('', Home, name='home'),
    path('all', AllView, name='all'),
    path('search', SearchView, name='search'),
    path('orders/new', OrderCreateView, name='new-order'),
    path('list/<slug>', CategoryView, name='list'),
    path('cart/<slug>', add_to_cart, name='cart'),
    path('increase/<slug>', increase_cart, name='increase-cart'),
    path('decrease/<slug>', decrease_cart, name='decrease-cart'),
    path('cart/', CartListView.as_view(), name='cart-home'),
    path('checkout-form', OrderCreateView.as_view(), name='checkout-form'),
    path('orders/complete/<int:pk>', OrderCompleteView.as_view(), name='checkout'),
    path('orders/show', OrderShowView, name='orders-show'),
    path('orders/detail/<int:pk>', OrderDetailView, name='orders-detail'),
]