from django.contrib import admin
from .models import thumbnail, photo_main, photo_Mask, Photo_log

@admin.register(thumbnail)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cash', 'order', 'category', 'status', 'owner', 'image_tag')
    list_editable = ('status', 'order', 'cash', 'category')
    list_display_links = ('id',)
    ordering = ('category', 'order', 'cash')
    list_filter = ('createDateTime', 'cash')
    search_fields = ('title', 'photo_Mask', 'photo_main')
    autocomplete_fields = ('photo_Mask', 'photo_main')
    readonly_fields = ('image_tag',)
    list_per_page = 50


@admin.register(photo_Mask)
class Photo_Mask(admin.ModelAdmin):
    list_display = ('id', 'title', 'min_word', 'medium_word', 'max_word', 'createDateTime', 'owner', 'image_tag')
    list_editable = ('min_word', 'medium_word', 'max_word',)
    list_display_links = ('id',)
    ordering = ('id',)
    list_filter = ('createDateTime',)
    search_fields = ('title',)
    readonly_fields = ('image_tag',)
    list_per_page = 50


@admin.register(photo_main)
class Photo_main(admin.ModelAdmin):
    list_display = ('id', 'title', 'createDateTime', 'owner', 'image_tag')
    # list_editable = ('title',)
    list_display_links = ('id',)
    ordering = ('id',)
    list_filter = ('createDateTime',)
    search_fields = ('title', 'content')
    readonly_fields = ('image_tag',)
    list_per_page = 50


@admin.register(Photo_log)
class Admin_log(admin.ModelAdmin):
    list_display = ('id', 'user', 'Photo', 'createDateTime')
    list_display_links = ('id',)
    ordering = ('id',)
    list_filter = ('createDateTime', 'Photo')
    search_fields = ('Photo', 'user')
    list_per_page = 50