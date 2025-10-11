# users/urls.py
from django.urls import path
from .views import RegisterView
from django.contrib.auth.views import LoginView, LogoutView
# from .views import books_list, book_detail

app_name = 'users'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'library:books_list'), name='logout'),

    ]