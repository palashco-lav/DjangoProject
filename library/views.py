# library/views.py
from django.shortcuts import render
from django.http import HttpResponse

# Простейшая view-функция для примера.
# Её наличие позволяет успешно импортировать модуль 'views'.
def index(request):
    return HttpResponse("Hello from library app!")