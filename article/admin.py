from django.contrib import admin
from .import models as AM


@admin.register(AM.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('avtor', 'title', 'body', 'date_pub')
    raw_id_fields = ('avtor', )
    readonly_fields = ('date_pub',)


@admin.register(AM.Category)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
