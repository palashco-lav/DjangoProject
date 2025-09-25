# products/views.py
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product


class ProductDetailView(View):
    """Контроллер для отображения детальной информации о товаре"""

    def get(self, request, product_id):
        # Получаем товар по ID или возвращаем 404
        product = get_object_or_404(Product, id=product_id)

        # Передаем товар в контекст шаблона
        context = {
            'product': product,
            'title': f'{product.name} - Детальная информация'
        }

        return render(request, 'products/product_detail.html', context)

def product_list(request):
    """Представление для списка всех товаров"""
    products = Product.objects.all()
    context = {
        'products': products,
        'title': 'Каталог товаров'
    }
    return render(request, 'products/product_list.html', context)

# Альтернативный вариант с функциональным представлением
def product_detail(request, product_id):
    """Функциональное представление для детальной страницы товара"""
    product = get_object_or_404(Product, id=product_id)

    context = {
        'product': product,
        'title': f'{product.name} - Детальная информация'
    }

    return render(request, 'products/product_detail.html', context)

def test_template(request):
    return render(request, 'products/base.html')  # Путь относительно templates/