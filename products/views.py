# products/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import Product


class HomeView(TemplateView):
    """Контроллер главной страницы"""
    template_name = 'products/home.html'


class ProductsListView(ListView):
    """Контроллер для списка всех товаров"""
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        """Добавляем заголовок в контекст"""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог товаров'
        return context


class ProductDetailView(DetailView):
    """Контроллер для отображения детальной информации о товаре"""
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'  # Указываем, что параметр называется product_id

    def get_context_data(self, **kwargs):
        """Добавляем заголовок в контекст"""
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.object.name} - Детальная информация'
        return context


class TestTemplateView(TemplateView):
    """Контроллер для тестирования шаблонов"""
    template_name = 'products/base.html'  # Путь относительно templates/

# Удаляем старые FBV функции:
# def home(request):
# def products_list(request):
# def product_detail(request, product_id):
# def test_template(request):