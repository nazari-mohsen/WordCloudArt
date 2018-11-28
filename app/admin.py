from django.contrib import admin
from .models import Config, version, Help_App
import jdatetime
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html

@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'createDateTime', 'owner', 'watermark', 'image_tag')
    list_display_links = ('title',)
    ordering = ('id',)
    list_filter = ('createDateTime',)
    search_fields = ('title', 'content')

@admin.register(version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'status', 'ver', 'file_link', 'file_create')
    list_display_links = ('id',)
    list_editable = ('status',)
    ordering = ('createDateTime', 'id')
    list_filter = ('createDateTime',)
    search_fields = ('content',)
    def file_create(self, obj):
        if obj.createDateTime:
            return jdatetime.date.fromgregorian(date=obj.createDateTime)
        else:
            return "No attachment"
    def file_link(self, obj):
        if obj.url:
            return format_html('<a href="%s" target="_blank">%s</a>' % (obj.url.url, obj.url.url))
        else:
            return "No attachment"

    file_link.allow_tags = True
    file_create.short_description = _('File Create')

@admin.register(Help_App)
class Help_AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'order', 'owner', 'createDateTime', 'image_tag')
    list_display_links = ('id',)
    list_editable = ('status',)
    ordering = ('id',)
    list_filter = ('createDateTime',)
    search_fields = ('title',)