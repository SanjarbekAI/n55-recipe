from django.contrib import admin

from blogs import models


@admin.register(models.BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author__first_name', 'created_at']
    search_fields = ['title', 'short_description', 'long_description']
    list_filter = ['created_at', 'updated_at']
    ordering = ['-created_at']


@admin.register(models.BlogHashtagModel)
class BlogHashtagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at', 'updated_at']
    ordering = ['-created_at']
