from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order', 'owner', 'status', 'created_at')
    list_filter = ('status', )
    ordering = ('id',)
    list_editable = ('title', 'status', 'order')
    search_fields = ('title', )
