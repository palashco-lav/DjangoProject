from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, View, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from django.http import HttpResponse
from .models import Product, Category
from .forms import ProductForm


class HomeView(ListView):
    """Контроллер главной страницы"""
    template_name = 'catalog/home.html'
    context_object_name = 'latest_products'

    def get_queryset(self):
        """Получаем последние 5 созданных продуктов"""
        queryset = Product.objects.all().order_by('-created_at')[:5]

        # Выводим в консоль
        print("=== ПОСЛЕДНИЕ 5 ПРОДУКТОВ ===")
        for product in queryset:
            print(f"{product.name} - {product.price} руб. - {product.created_at}")
        print("=============================")

        return queryset

    def get_context_data(self, **kwargs):
        """Добавляем заголовок в контекст"""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['products_count'] = Product.objects.count()
        context['categories_count'] = Category.objects.count()
        return context


class ContactsView(View):
    """Контроллер страницы контактов"""

    def get(self, request):
        """Обработка GET запроса - отображение формы"""
        return render(request, 'catalog/contacts.html', {'title': 'Контакты'})

    def post(self, request):
        """Обработка POST запроса - обработка формы"""
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! тел. {phone} Ваше сообщение получено.")


class ProductListView(ListView):
    """Контроллер для списка всех продуктов"""
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все товары'
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    """Контроллер для детального просмотра продукта"""
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Товар: {self.object.name}'
        return context


class ProductCreateView(CreateView):
    """Контроллер для создания нового продукта"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание товара'
        context['submit_text'] = 'Создать товар'
        return context

    def form_valid(self, form):
        """Добавляем сообщение об успехе"""
        messages.success(self.request, f'Товар "{form.instance.name}" успешно создан!')
        return super().form_valid(form)

    def form_invalid(self, form):
        """Добавляем сообщение об ошибке"""
        messages.error(self.request, 'Пожалуйста, исправьте ошибки в форме.')
        return super().form_invalid(form)


class ProductUpdateView(UpdateView):
    """Контроллер для редактирования продукта"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование: {self.object.name}'
        context['submit_text'] = 'Сохранить изменения'
        return context

    def form_valid(self, form):
        """Добавляем сообщение об успехе"""
        messages.success(self.request, f'Товар "{form.instance.name}" успешно обновлен!')
        return super().form_valid(form)

    def form_invalid(self, form):
        """Добавляем сообщение об ошибке"""
        messages.error(self.request, 'Пожалуйста, исправьте ошибки в форме.')
        return super().form_invalid(form)


class ProductDeleteView(DeleteView):
    """Контроллер для удаления продукта"""
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Удаление товара: {self.object.name}'
        return context

    def delete(self, request, *args, **kwargs):
        """Добавляем сообщение об успехе"""
        product_name = self.get_object().name
        messages.success(self.request, f'Товар "{product_name}" успешно удален!')
        return super().delete(request, *args, **kwargs)