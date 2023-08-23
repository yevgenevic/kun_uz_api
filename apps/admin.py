from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from apps.models import Post, Category


@admin.register(Post)
class PostModelAdmin(TranslationAdmin):
    list_display = ('title_uz', 'status')


@admin.register(Category)
class CategoryModelAdmin(TranslationAdmin):
    list_display = ('title', 'title_en', 'title_ru')
