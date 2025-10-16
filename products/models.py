# products/models.py
from django.db import models
from django.conf import settings


class Product(models.Model):
    PUBLICATION_STATUS = [
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
        ('unpublished', 'Снято с публикации'),
    ]

    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение")
    category = models.CharField(max_length=100, verbose_name="Категория")
    in_stock = models.BooleanField(default=True, verbose_name="В наличии")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    # Поле для статуса публикации
    publication_status = models.CharField(
        max_length=20,
        choices=PUBLICATION_STATUS,
        default='draft',
        verbose_name="Статус публикации"
    )

    # владелец продукта
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Используем AUTH_USER_MODEL вместо прямого импорта User
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name="Владелец"
    )

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ("can_unpublish_product", "Может отменять публикацию продукта"),
        ]