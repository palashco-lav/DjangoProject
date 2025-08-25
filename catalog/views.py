# catalog/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'catalog/home.html')

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