from django.contrib import admin
from log.models import Request_photo, CashCoin, Coinvideo, CreateUser, Crash, Photo_log


# admin.site.register(Request_image)
@admin.register(Request_photo)
class request_photo(admin.ModelAdmin):
    list_display = ('id', 'user', 'createDateTime')
    list_display_links = ('id', )
    ordering = ('id', )
    list_filter = ('user',)
    search_fields = ('user', 'log')
    list_per_page = 20

@admin.register(Photo_log)
class Admin_log(admin.ModelAdmin):
    list_display = ('id', 'user', 'Photo', 'createDateTime')
    list_display_links = ('id',)
    ordering = ('id',)
    list_filter = ('createDateTime', 'Photo')
    search_fields = ('Photo', 'user')
    list_per_page = 50

@admin.register(CashCoin)
class cashcoin(admin.ModelAdmin):
    list_display = ('id', 'user', 'createDateTime')
    list_display_links = ('id', )
    ordering = ('id', )
    list_filter = ('user',)
    search_fields = ('user', 'log')
    list_per_page = 20

@admin.register(Coinvideo)
class coinvideo(admin.ModelAdmin):
    list_display = ('id', 'user', 'createDateTime')
    list_display_links = ('id', )
    ordering = ('id', )
    list_filter = ('user',)
    search_fields = ('user', 'log')
    list_per_page = 20

@admin.register(CreateUser)
class createuser(admin.ModelAdmin):
    list_display = ('id', 'createDateTime')
    list_display_links = ('id', )
    ordering = ('id', )
    list_filter = ('id',)
    search_fields = ('log', )
    list_per_page = 20

@admin.register(Crash)
class Crash(admin.ModelAdmin):
    list_display = ('id', 'user', 'createDateTime')
    list_display_links = ('id', )
    ordering = ('id', )
    list_filter = ('id',)
    search_fields = ('log', )
    list_per_page = 20