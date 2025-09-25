# products/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Поля, которые отображаются в списке товаров
    list_display = [
        'id',
        'name',
        'category',
        'price',
        'in_stock',
        'created_at',
        'actions'
    ]

    # Поля для фильтрации
    list_filter = ['category', 'in_stock', 'created_at']

    # Поля для поиска
    search_fields = ['name', 'description', 'category']

    # Поля, которые можно редактировать прямо из списка
    list_editable = ['price', 'in_stock']

    # Пагинация
    list_per_page = 20

    # Порядок сортировки по умолчанию
    ordering = ['-created_at']

    # Поля в форме редактирования
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description', 'category')
        }),
        ('Цена и наличие', {
            'fields': ('price', 'in_stock')
        }),
        ('Дополнительная информация', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        })
    )

    # Только для чтения поля
    readonly_fields = ['created_at']

    def actions(self, obj):
        """Кастомные действия для каждой строки"""
        return format_html(
            '<a href="/admin/products/product/{}/change/">✏️</a> '
            '<a href="/admin/products/product/{}/delete/">🗑️</a>',
            obj.id, obj.id
        )

    actions.short_description = 'Действия'

    # Кастомные действия для массового редактирования

    @admin.action(description="Пометить как в наличии")
    def make_in_stock(self, request, queryset):
        queryset.update(in_stock=True)
        self.message_user(request, "Выбранные товары помечены как в наличии")

    @admin.action(description="Пометить как отсутствующие")
    def make_out_of_stock(self, request, queryset):
        queryset.update(in_stock=False)
        self.message_user(request, "Выбранные товары помечены как отсутствующие")

    @admin.action(description="Увеличить цену на 10%")
    def increase_price_10_percent(self, request, queryset):
        for product in queryset:
            product.price *= 1.1
            product.save()
        self.message_user(request, "Цены увеличены на 10%")

    actions = [make_in_stock, make_out_of_stock, increase_price_10_percent]