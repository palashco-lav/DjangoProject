# products/management/commands/fill_products.py
from django.core.management.base import BaseCommand
from django.core.files import File
from products.models import Product
from datetime import datetime
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Заполнение базы данных тестовыми товарами'

    def handle(self, *args, **options):
        # Данные для тестовых товаров
        products_data = [
            {
                'name': 'Ноутбук Apple MacBook Pro 16"',
                'description': 'Мощный ноутбук для профессионалов с чипом M2 Pro и дисплеем Liquid Retina XDR.',
                'price': 249999.00,
                'category': 'Ноутбуки',
                'in_stock': True,
            },
            {
                'name': 'Наушники Sony WH-1000XM5',
                'description': 'Беспроводные наушники с продвинутым шумоподавлением и автономностью до 30 часов.',
                'price': 34999.50,
                'category': 'Аксессуары',
                'in_stock': True,
            },
            {
                'name': 'Планшет iPad Air 5',
                'description': 'Универсальный планшет с чипом M1, поддержкой Apple Pencil и Magic Keyboard.',
                'price': 74999.00,
                'category': 'Планшеты',
                'in_stock': False,
            },
            {
                'name': 'Фотокамера Canon EOS R6',
                'description': 'Беззеркальная камера с полнокадровой матрицей и стабилизацией изображения 8 ступеней.',
                'price': 189999.00,
                'category': 'Фототехника',
                'in_stock': True,
            },
            {
                'name': 'Умные часы Apple Watch Series 9',
                'description': 'Смарт-часы с функцией измерения ЭКГ, отслеживанием сна и фитнес-трекером.',
                'price': 41999.00,
                'category': 'Гаджеты',
                'in_stock': True,
            },
            {
                'name': 'Игровая консоль PlayStation 5',
                'description': 'Новейшая игровая консоль с поддержкой 4K 120fps и SSD накопителем.',
                'price': 69999.00,
                'category': 'Игровые консоли',
                'in_stock': True,
            },
            {
                'name': 'Монитор Dell UltraSharp 32"',
                'description': '4K монитор с точной цветопередачей для профессиональной работы с графикой.',
                'price': 89999.00,
                'category': 'Мониторы',
                'in_stock': True,
            },
            {
                'name': 'Внешний SSD Samsung T7 2TB',
                'description': 'Портативный SSD накопитель со скоростью передачи данных до 1050 МБ/с.',
                'price': 15999.00,
                'category': 'Комплектующие',
                'in_stock': True,
            },
            {
                'name': 'Электрическая зубная щетка Oral-B iO',
                'description': 'Умная зубная щетка с технологией магнитного привода и приложением для контроля.',
                'price': 14999.00,
                'category': 'Бытовая техника',
                'in_stock': False,
            }
        ]

        created_count = 0
        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Создан товар: {product.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Товар уже существует: {product.name}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Успешно создано {created_count} товаров')
        )