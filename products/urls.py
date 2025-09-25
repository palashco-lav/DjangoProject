# products/urls.py
from django.urls import path

# from products.urls import app_name
from . import views

# app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    # или для функционального представления:
    # path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]