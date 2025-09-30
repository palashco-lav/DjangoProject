# blog/admin.py
from django.contrib import admin
from .models import BlogsPost

@admin.register(BlogsPost)
class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'is_published', 'views_count']
    list_filter = ['is_published', 'created_at']
    search_fields = ['title', 'content']
    readonly_fields = ['views_count', 'created_at']