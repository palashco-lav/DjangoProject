# products/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Product


class HomeView(TemplateView):
    """Контроллер главной страницы - общедоступный"""
    template_name = 'products/home.html'


class ProductsListView(ListView):
    """Контроллер для списка всех товаров - ОБЩЕДОСТУПНЫЙ"""
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        """Добавляем заголовок в контекст"""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог товаров'
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Контроллер для отображения детальной информации о товаре - ТОЛЬКО ДЛЯ АВТОРИЗОВАННЫХ"""
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'
    login_url = '/users/login/'  # URL для перенаправления неавторизованных пользователей

    def get_context_data(self, **kwargs):
        """Добавляем заголовок в контекст"""
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.object.name} - Детальная информация'
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'products/product_form.html'  # Убедитесь, что путь правильный
    fields = ['name', 'description', 'price', 'category', 'in_stock', 'image']
    success_url = reverse_lazy('products:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить товар'
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'products/product_form.html'  # Убедитесь, что путь правильный
    fields = ['name', 'description', 'price', 'category', 'in_stock', 'image']
    pk_url_kwarg = 'product_id'
    success_url = reverse_lazy('products:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактировать {self.object.name}'
        return context


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'  # Убедитесь, что путь правильный
    pk_url_kwarg = 'product_id'
    success_url = reverse_lazy('products:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Удалить {self.object.name}'
        return context


class TestTemplateView(TemplateView):
    """Контроллер для тестирования шаблонов - общедоступный"""
    template_name = 'products/base.html'