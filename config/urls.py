# config/urls.py

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('', include('products.urls')),
    # path('catalog/', include('catalog.urls')),
    # path('library/', include('library.urls')),
    # path('students/', include('students.urls')),
    # path('', include('library.urls', namespace='library')),
]