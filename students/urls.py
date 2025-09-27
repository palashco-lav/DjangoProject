# students/urls.py
from django.urls import path
from students import views

app_name = 'students'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('index/', views.index, name='index'),
    path('student_detail/<int:student_id>/', views.student_detail, name='student_detail'),
    path('student_list/', views.student_list, name='student_list'),
    # path('', views.students_list, name='students_list'),
]
