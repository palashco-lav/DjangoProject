# catalog/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def home(request):
    """Контроллер главной страницы"""
    # Получаем последние 5 созданных продуктов
    latest_products = Product.objects.all().order_by('-created_at')[:5]

    # Выводим в консоль
    print("=== ПОСЛЕДНИЕ 5 ПРОДУКТОВ ===")
    for product in latest_products:
        print(f"{product.name} - {product.price} руб. - {product.created_at}")
    print("=============================")

    # Передаем в контекст шаблона
    context = {
        'latest_products': latest_products,
        'title': 'Главная страница'
    }

    return render(request, 'catalog/home.html', context)

def contacts(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! тел. {phone} Ваше сообщение получено.")
    return render(request, 'catalog/contacts.html')