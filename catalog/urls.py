# catalog/urls.py
from django.urls import path
from .views import HomeView, ContactsView

# app_name = 'catalog'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
]