from datetime import date
from django.db import models
from imagekit.models import ImageSpecField  # https://django-imagekit.readthedocs.io/en/latest/
from imagekit.processors import ResizeToFit


class Category(models.Model):
    """Категории документов"""
    name = models.CharField('Категория', max_length=120)
    url = models.SlugField(max_length=50, unique=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категории'


class ArticleData(models.Model):
    """Текст и метаданные статьи"""
    article_url = models.SlugField('Уникальный ID', max_length=50, unique=True,
                                   help_text='Только латинские буквы, цифры, знаки "-", "_". Максимум 50 символов')
    categories = models.ManyToManyField(Category, verbose_name='категории')
    title = models.CharField('Название', max_length=250)
    text = models.TextField('Текст', blank=True)
    author = models.CharField('Автор', max_length=50, blank=True, help_text='Необязательно')
    pub_date = models.DateField('Дата публикации', default=date.today)
    is_template = models.BooleanField('HTML-шаблон?', default=False)
    is_published = models.BooleanField('Опубликовано?', default=False)

    class Meta:
        verbose_name_plural = 'Статьи авторов'


def upload_path(instance, filename):
    """Photo upload path. Subdirectory name = article_url"""
    return f'articles_photo/{instance.article.article_url}/{filename}'


class ArticlePhoto(models.Model):
    """Фотографии к статьям (если есть)"""
    article = models.ForeignKey(ArticleData, on_delete=models.CASCADE)
    image_source = models.ImageField('-- Файл --', upload_to=upload_path, blank=True, max_length=256)
    image_prev = ImageSpecField(source='image_source',
                                processors=[ResizeToFit(320, 320)],
                                format='JPEG',
                                options={'quality': 90})

    class Meta:
        verbose_name_plural = 'Фото к статьям'
