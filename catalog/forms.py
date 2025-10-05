from django import forms
from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """Форма для создания и редактирования продукта с валидацией запрещенных слов и изображений"""

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price', 'is_available']
        widgets = {
            'name': forms.TextInput(),
            'description': forms.Textarea(attrs={'rows': 4}),
            'image': forms.FileInput(),
            'category': forms.Select(),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
            'is_available': forms.CheckboxInput(),  # ✅ Стилизация чекбокса
        }
        labels = {
            'name': 'Наименование товара',
            'description': 'Описание товара',
            'image': 'Изображение товара',
            'category': 'Категория',
            'price': 'Цена (руб.)',
            'is_available': 'В наличии'  # ✅ Метка для булевого поля
        }
        help_texts = {
            'image': 'Допустимые форматы: JPEG, PNG. Максимальный размер: 5 МБ',
            'name': 'Не используйте запрещенные слова в названии',
            'description': 'Не используйте запрещенные слова в описании',
            'is_available': 'Отметьте, если товар есть в наличии',  # ✅ Подсказка для чекбокса
        }

    def __init__(self, *args, **kwargs):
        """Стилизация форм для соответствия общей стилистике"""
        super().__init__(*args, **kwargs)

        # Применяем классы Bootstrap ко всем полям
        for field_name, field in self.fields.items():
            if field_name == 'image':
                field.widget.attrs.update({
                    'class': 'form-control',
                    'accept': '.jpg,.jpeg,.png'
                })
            elif field_name == 'is_available':
                # ✅ Специальная стилизация для чекбокса
                field.widget.attrs.update({
                    'class': 'form-check-input',
                })
            else:
                field.widget.attrs['class'] = 'form-control'

            # Добавляем placeholder для улучшения UX
            if field_name == 'name':
                field.widget.attrs['placeholder'] = 'Введите название товара'
            elif field_name == 'description':
                field.widget.attrs['placeholder'] = 'Введите описание товара'
            elif field_name == 'price':
                field.widget.attrs['placeholder'] = '0.00'

    def _contains_forbidden_words(self, text):
        """Проверяет текст на наличие запрещенных слов"""
        if not text:
            return False

        text_lower = text.lower()
        for forbidden_word in self.FORBIDDEN_WORDS:
            if forbidden_word in text_lower:
                return forbidden_word
        return False

    def clean_name(self):
        """Валидация названия продукта"""
        name = self.cleaned_data.get('name')

        if not name:
            raise forms.ValidationError('Название товара обязательно для заполнения')

        forbidden_word = self._contains_forbidden_words(name)
        if forbidden_word:
            raise forms.ValidationError(
                f'Название содержит запрещенное слово: "{forbidden_word}"'
            )

        return name

    def clean_description(self):
        """Валидация описания продукта"""
        description = self.cleaned_data.get('description')

        forbidden_word = self._contains_forbidden_words(description)
        if forbidden_word:
            raise forms.ValidationError(
                f'Описание содержит запрещенное слово: "{forbidden_word}"'
            )

        return description

    def clean_price(self):
        """Валидация цены продукта"""
        price = self.cleaned_data.get('price')

        if price is None:
            raise forms.ValidationError('Цена обязательна для заполнения')

        if price < 0:
            raise forms.ValidationError('Цена не может быть отрицательной')

        if price == 0:
            raise forms.ValidationError('Цена не может быть нулевой')

        return price

    def clean_image(self):
        """Валидация загружаемого изображения"""
        image = self.cleaned_data.get('image')

        # Если изображение не загружено, пропускаем валидацию
        if not image:
            return image

        # Проверка размера файла
        if image.size > self.MAX_UPLOAD_SIZE:
            raise forms.ValidationError(
                f'Размер файла не должен превышать {filesizeformat(self.MAX_UPLOAD_SIZE)}. '
                f'Текущий размер: {filesizeformat(image.size)}'
            )

        # Проверка типа файла
        if image.content_type not in self.ALLOWED_IMAGE_TYPES:
            raise forms.ValidationError(
                f'Недопустимый формат файла. Допустимые форматы: {", ".join(self.ALLOWED_IMAGE_TYPES)}'
            )

        # Дополнительная проверка расширения файла
        import os
        ext = os.path.splitext(image.name)[1].lower()
        if ext not in ['.jpg', '.jpeg', '.png']:
            raise forms.ValidationError(
                'Недопустимое расширение файла. Допустимые расширения: .jpg, .jpeg, .png'
            )

        # Проверка на вредоносные файлы (базовая)
        if hasattr(image, 'temporary_file_path'):
            # Файл сохранен во временной директории
            try:
                from PIL import Image
                img = Image.open(image.temporary_file_path())
                img.verify()  # Проверка целостности изображения
            except Exception as e:
                raise forms.ValidationError('Файл поврежден или не является допустимым изображением')

        return image