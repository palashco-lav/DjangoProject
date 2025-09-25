# students/views.py
from django.shortcuts import render
from django.http import HttpResponse

from students.models import Student

def about(request):
    return render(request, 'students/about.html')

def contact(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'students/contact.html')

def example_view(request):
    return render(request, 'students/example.html')

def index(request):
    student = Student.objects.get(id=1)
    context = {
        'students_name': f"{student.first_name} {student.last_name}",
        'students_year': student.get_year_display,
    }
    return render(request, 'students/index.html', context=context)

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    context = {
        'student': student,
    }
    return render(request, 'students/student_detail.html', context=context)

def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'students/student_list.html', context=context)