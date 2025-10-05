from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from django.utils.deconstruct import deconstructible
from PIL import Image
import os


@deconstructible
class ImageValidator:
    """
    Валидатор для проверки загружаемых изображений
    """

    def __init__(self, max_size=5 * 1024 * 1024, allowed_types=None, min_dimensions=None, max_dimensions=None):
        self.max_size = max_size
        self.allowed_types = allowed_types or ['image/jpeg', 'image/png', 'image/jpg']
        self.min_dimensions = min_dimensions  # (width, height)
        self.max_dimensions = max_dimensions  # (width, height)

    def __call__(self, value):
        if not value:
            return

        # Проверка размера файла
        if value.size > self.max_size:
            raise ValidationError(
                f'Размер файла не должен превышать {filesizeformat(self.max_size)}. '
                f'Текущий размер: {filesizeformat(value.size)}'
            )

        # Проверка типа файла
        if value.content_type not in self.allowed_types:
            raise ValidationError(
                f'Недопустимый формат файла. Допустимые форматы: {", ".join(self.allowed_types)}'
            )

        # Проверка расширения файла
        ext = os.path.splitext(value.name)[1].lower()
        if ext not in ['.jpg', '.jpeg', '.png']:
            raise ValidationError(
                'Недопустимое расширение файла. Допустимые расширения: .jpg, .jpeg, .png'
            )

        # Проверка размеров изображения
        try:
            if hasattr(value, 'temporary_file_path'):
                img = Image.open(value.temporary_file_path())
            else:
                # Для файлов в памяти
                img = Image.open(value)

            width, height = img.size

            if self.min_dimensions and (width < self.min_dimensions[0] or height < self.min_dimensions[1]):
                raise ValidationError(
                    f'Минимальный размер изображения: {self.min_dimensions[0]}x{self.min_dimensions[1]}px. '
                    f'Текущий размер: {width}x{height}px'
                )

            if self.max_dimensions and (width > self.max_dimensions[0] or height > self.max_dimensions[1]):
                raise ValidationError(
                    f'Максимальный размер изображения: {self.max_dimensions[0]}x{self.max_dimensions[1]}px. '
                    f'Текущий размер: {width}x{height}px'
                )

        except Exception as e:
            raise ValidationError('Файл поврежден или не является допустимым изображением')

    def __eq__(self, other):
        return (
                isinstance(other, ImageValidator) and
                self.max_size == other.max_size and
                self.allowed_types == other.allowed_types
        )