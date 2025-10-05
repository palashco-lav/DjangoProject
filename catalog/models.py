from django.db import models
import os
from django.utils import timezone


class Category(models.Model):
    """Модель категории товаров"""
    name = models.CharField(
        max_length=100,
        verbose_name='Наименование'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель товара"""
    name = models.CharField(
        max_length=100,
        verbose_name='Наименование'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='products/',
        verbose_name='Изображение',
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        blank=True,
        null=True,
        related_name='products'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена за покупку'
    )
    is_available = models.BooleanField(
        default=True,
        verbose_name='В наличии',
        help_text='Отметьте, если товар есть в наличии'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата последнего изменения'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_image_url(self):
        """Возвращает URL изображения или заглушку"""
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return '/static/images/no-image.png'

    def get_image_filename(self):
        """Возвращает имя файла изображения"""
        if self.image:
            return os.path.basename(self.image.name)
        return 'No image'

    def get_availability_display(self):
        """Возвращает текстовое представление наличия товара"""
        return "В наличии" if self.is_available else "Нет в наличии"

    def get_availability_badge(self):
        """Возвращает HTML бейдж для отображения наличия"""
        if self.is_available:
            return '<span class="badge bg-success">В наличии</span>'
        else:
            return '<span class="badge bg-danger">Нет в наличии</span>'

    def save(self, *args, **kwargs):
        """Переопределяем save для обработки изображений"""
        # Если это обновление существующего объекта и изображение изменено
        if self.pk:
            try:
                old_instance = Product.objects.get(pk=self.pk)
                if old_instance.image and old_instance.image != self.image:
                    # Удаляем старое изображение
                    old_instance.image.delete(save=False)
            except Product.DoesNotExist:
                pass

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Переопределяем delete для удаления изображения"""
        if self.image:
            self.image.delete(save=False)
        super().delete(*args, **kwargs)