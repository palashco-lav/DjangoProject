# catalog/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, View
from .models import Product


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
        return context


class ContactsView(View):
    """Контроллер страницы контактов"""

    def get(self, request):
        """Обработка GET запроса - отображение формы"""
        return render(request, 'catalog/contacts.html')

    def post(self, request):
        """Обработка POST запроса - обработка формы"""
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! тел. {phone} Ваше сообщение получено.")