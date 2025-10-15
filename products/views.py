# products/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseForbidden
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
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог товаров'
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    """Контроллер для отображения детальной информации о товаре - ТОЛЬКО ДЛЯ АВТОРИЗОВАННЫХ"""
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'
    login_url = '/users/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.object.name} - Детальная информация'
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Создание продукта - автоматически привязываем к текущему пользователю"""
    model = Product
    template_name = 'products/product_form.html'
    fields = ['name', 'description', 'price', 'category', 'in_stock', 'image', 'publication_status']
    success_url = reverse_lazy('products:list')

    def form_valid(self, form):
        """Автоматически привязываем продукт к текущему пользователю"""
        form.instance.owner = self.request.user
        messages.success(self.request, f'Продукт "{form.instance.name}" успешно создан!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить товар'
        return context


class OwnerRequiredMixin(UserPassesTestMixin):
    """Миксин для проверки, что пользователь является владельцем продукта"""

    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, 'У вас нет прав для редактирования этого продукта.')
        return HttpResponseForbidden('Доступ запрещен')


class ModeratorOrOwnerRequiredMixin(UserPassesTestMixin):
    """Миксин для проверки, что пользователь является владельцем ИЛИ модератором"""

    def test_func(self):
        product = self.get_object()
        user = self.request.user
        # Владелец ИЛИ пользователь с правом удаления продуктов (модератор)
        return product.owner == user or user.has_perm('products.delete_product')

    def handle_no_permission(self):
        messages.error(self.request, 'У вас нет прав для удаления этого продукта.')
        return HttpResponseForbidden('Доступ запрещен')


class ProductUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    """Только владелец может редактировать"""
    model = Product
    template_name = 'products/product_form.html'
    fields = ['name', 'description', 'price', 'category', 'in_stock', 'image', 'publication_status']
    pk_url_kwarg = 'product_id'
    success_url = reverse_lazy('products:list')

    def form_valid(self, form):
        messages.success(self.request, f'Продукт "{form.instance.name}" успешно обновлен!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактировать {self.object.name}'
        return context


class ProductDeleteView(LoginRequiredMixin, ModeratorOrOwnerRequiredMixin, DeleteView):
    """Владелец ИЛИ модератор может удалять"""
    model = Product
    template_name = 'products/product_confirm_delete.html'
    pk_url_kwarg = 'product_id'
    success_url = reverse_lazy('products:list')

    def delete(self, request, *args, **kwargs):
        product = self.get_object()
        messages.success(request, f'Продукт "{product.name}" успешно удален!')
        return super().delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Удалить {self.object.name}'
        return context


# Дополнительный view для снятия с публикации
from django.views import View
from django.shortcuts import redirect


class ProductUnpublishView(LoginRequiredMixin, View):
    """Снятие продукта с публикации - только модераторы"""

    def post(self, request, product_id):
        if not request.user.has_perm('products.can_unpublish_product'):
            messages.error(request, 'У вас нет прав для снятия продуктов с публикации.')
            return redirect('products:list')

        product = get_object_or_404(Product, id=product_id)
        if product.publication_status == 'published':
            product.publication_status = 'unpublished'
            product.save()
            messages.success(request, f'Продукт "{product.name}" снят с публикации!')
        else:
            messages.warning(request, 'Продукт уже не опубликован')

        return redirect('products:list')


class TestTemplateView(TemplateView):
    """Контроллер для тестирования шаблонов - общедоступный"""
    template_name = 'products/base.html'