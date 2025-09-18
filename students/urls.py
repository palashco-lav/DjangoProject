# students/urls.py
from django.urls import path
from students import views

app_name = 'students'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('', views.students_list, name='students_list'),
]
