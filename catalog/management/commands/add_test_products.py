from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Добавляет тестовые продукты в базу данных (удаляет старые данные)'

    def handle(self, *args, **options):
        # Удаляем все существующие данные
        self.stdout.write('Удаление старых данных...')
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создаем категории
        self.stdout.write('Создание категорий...')
        categories_data = [
            {'name': 'Электроника', 'description': 'Техника и гаджеты'},
            {'name': 'Одежда', 'description': 'Модная одежда'},
            {'name': 'Книги', 'description': 'Литература разных жанров'},
            {'name': 'Мебель', 'description': 'Домашняя и офисная мебель'},
            {'name': 'Спорт', 'description': 'Спортивные товары'},
        ]

        categories = {}
        for cat_data in categories_data:
            category = Category.objects.create(**cat_data)
            categories[cat_data['name']] = category
            self.stdout.write(f'Создана категория: {category.name}')

        # Создаем продукты
        self.stdout.write('Создание продуктов...')
        products_data = [
            {
                'name': 'Смартфон iPhone 15',
                'description': 'Новый флагманский смартфон с улучшенной камерой',
                'category': categories['Электроника'],
                'price': 999.99
            },
            {
                'name': 'Ноутбук Dell XPS 15',
                'description': 'Мощный ноутбук для работы и творчества',
                'category': categories['Электроника'],
                'price': 1499.99
            },
            {
                'name': 'Наушники Sony WH-1000XM5',
                'description': 'Беспроводные наушники с шумоподавлением',
                'category': categories['Электроника'],
                'price': 349.99
            },
            {
                'name': 'Хлопковая футболка',
                'description': 'Удобная футболка из 100% хлопка',
                'category': categories['Одежда'],
                'price': 24.99
            },
            {
                'name': 'Джинсы классические',
                'description': 'Классические джинсы прямого кроя',
                'category': categories['Одежда'],
                'price': 59.99
            },
            {
                'name': 'Куртка зимняя',
                'description': 'Теплая зимняя куртка с мехом',
                'category': categories['Одежда'],
                'price': 199.99
            },
            {
                'name': 'Война и мир',
                'description': 'Классический роман Льва Толстого',
                'category': categories['Книги'],
                'price': 19.99
            },
            {
                'name': 'Преступление и наказание',
                'description': 'Роман Фёдора Достоевского',
                'category': categories['Книги'],
                'price': 15.99
            },
            {
                'name': 'Офисное кресло',
                'description': 'Эргономичное кресло для работы',
                'category': categories['Мебель'],
                'price': 199.99
            },
            {
                'name': 'Диван угловой',
                'description': 'Удобный угловой диван для гостиной',
                'category': categories['Мебель'],
                'price': 899.99
            },
            {
                'name': 'Беговая дорожка',
                'description': 'Электрическая беговая дорожка для дома',
                'category': categories['Спорт'],
                'price': 799.99
            },
            {
                'name': 'Гантели наборные',
                'description': 'Наборные гантели до 20 кг',
                'category': categories['Спорт'],
                'price': 89.99
            },
        ]

        for product_data in products_data:
            product = Product.objects.create(**product_data)
            self.stdout.write(f'Создан продукт: {product.name} - {product.price} руб.')

        # Статистика
        self.stdout.write(
            self.style.SUCCESS(
                f'\nУспешно создано: '
                f'{Category.objects.count()} категорий и '
                f'{Product.objects.count()} продуктов!'
            )
        )