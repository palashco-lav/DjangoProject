from django.urls import path
from .views import (
    HomeView,
    ProductsListView,
    ProductDetailView,
    TestTemplateView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView
)

app_name = 'products'

urlpatterns = [
    # Главная страница
    path('', HomeView.as_view(), name='home'),

    # Список товаров
    path('products/', ProductsListView.as_view(), name='list'),

    # Тестовая страница
    path('test/', TestTemplateView.as_view(), name='test'),

    # Защищенные маршруты (только для авторизованных)
    path('products/create/', ProductCreateView.as_view(), name='create'),
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='detail'),
    path('products/<int:product_id>/update/', ProductUpdateView.as_view(), name='update'),
    path('products/<int:product_id>/delete/', ProductDeleteView.as_view(), name='delete'),
]