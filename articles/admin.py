from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, ArticleData, ArticlePhoto

admin.site.site_title = "Админ-панель"
admin.site.site_header = "Админ-панель"


@admin.register(ArticlePhoto)
class ArticlePhotoAdmin(admin.ModelAdmin):
    list_display = ('get_article_title', 'image_source', 'get_image',)
    list_filter = ('article__categories',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={str(obj.image_source.url)} width="15%"')
    get_image.short_description = '--Миниатюра--'

    def get_article_title(self, obj):
        return obj.article.title
    get_article_title.short_description = '--Статья--'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url',)
    list_display_links = ('name',)
    fieldsets = (
        (None, {
            'fields': (('name', 'url',),)
        }),
    )


class ArticlePhotoInline(admin.TabularInline):
    model = ArticlePhoto
    extra = 0
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={str(obj.image_source.url)} width="15%"')
    get_image.short_description = "-- Превью --"


@admin.register(ArticleData)
class ArticleDataAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('article_url', 'title', 'author', 'pub_date', 'is_template', 'is_published',)
    list_display_links = ('article_url', 'title',)
    list_filter = ('categories',)
    inlines = [ArticlePhotoInline]
    fieldsets = (
        (None, {
            'fields': (('title', 'article_url', 'author',),)
        }),
        (None, {
            'fields': (('text', 'categories',),)
        }),
        (None, {
            'fields': (('pub_date', 'is_published', 'is_template',),)
        }),
    )

    def save_model(self, request, obj, form, change):
        """found in: https://blog.rousek.name/2017/08/11/uploading-multiple-files-in-django-admin/"""
        obj.save()
        for afile in request.FILES.getlist('photos_multiple'):
            obj.articlephoto_set.create(article=obj.article_url, image_source=afile)
