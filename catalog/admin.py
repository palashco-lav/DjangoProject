from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Админка для категорий"""
    list_display = ['id', 'name']  # id и name в списке
    list_display_links = ['id', 'name']  # Ссылки на редактирование
    search_fields = ['name', 'description']  # Поиск по названию и описанию
    ordering = ['id']  # Сортировка по ID


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админка для товаров"""
    list_display = ['id', 'name', 'price', 'category']  # id, name, price, category в списке
    list_display_links = ['id', 'name']  # Ссылки на редактирование
    list_filter = ['category']  # Фильтрация по категории
    search_fields = ['name', 'description']  # Поиск по названию и описанию
    list_per_page = 20  # Пагинация
    ordering = ['-id']  # Сортировка по ID (новые сверху)

    # Группировка полей на форме редактирования
    fieldsets = [
        ('Основная информация', {
            'fields': ['name', 'description', 'image']
        }),
        ('Категория и цена', {
            'fields': ['category', 'price']
        }),
        ('Даты', {
            'fields': ['created_at', 'updated_at'],
            'classes': ['collapse']  # Сворачиваемый блок
        }),
    ]

    # Только для чтения поля с датами
    readonly_fields = ['created_at', 'updated_at']