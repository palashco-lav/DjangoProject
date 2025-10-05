# blogs/models.py
from django.db import models
from django.urls import reverse

class BlogsPost(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок'
    )
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(
        upload_to='blogs/previews/',
        verbose_name='Превью',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Признак публикации'
    )
    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество просмотров',
        editable = False
    )

    class Meta:
        verbose_name = 'Блоговая запись'
        verbose_name_plural = 'Блоговые записи'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs:post_detail', kwargs={'pk': self.pk})

    def increment_views(self):
        """Увеличивает счетчик просмотров"""
        self.views_count += 1
        self.save(update_fields=['views_count'])
