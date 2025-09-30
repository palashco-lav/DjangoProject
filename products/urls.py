# products/urls.py
from django.urls import path
from .views import HomeView, ProductsListView, ProductDetailView, TestTemplateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductsListView.as_view(), name='products_list'),
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('test/', TestTemplateView.as_view(), name='test_template'),
]