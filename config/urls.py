# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    # path('', include('products.urls')),
    path('', include('catalog.urls')),
    # path('catalog/', include('catalog.urls')),
    # path('', include('library.urls')),
    # path('products/', include('products.urls')),
    path('users/', include('users.urls', namespace='users')),
    # path('students/', include('students.urls')),
    # path('', include('library.urls', namespace='library')),
    # ath('blogs/', include('blogs.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)