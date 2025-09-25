# products/urls.py
from django.urls import path

# from products.urls import app_name
from . import views

# app_name = 'products'

urlpatterns = [
    path('', views.home, name='home'),
    path('products_list', views.products_list, name='products_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    # или для функционального представления:
    # path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]