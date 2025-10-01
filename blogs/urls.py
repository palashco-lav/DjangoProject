# blog/urls.py
from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.BlogsPostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.BlogsPostDetailView.as_view(), name='post_detail'),
    path('post/create/', views.BlogsPostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.BlogsPostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.BlogsPostDeleteView.as_view(), name='post_delete'),
]