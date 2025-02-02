from django.contrib import admin
from log.models import Request_photo, CashCoin, Coinvideo, CreateUser, Crash, Photo_log


# admin.site.register(Request_image)
@admin.register(Request_photo)
class request_photo(admin.ModelAdmin):
    list_display = ('id', 'user', 'createDateTime')
    list_display_links = ('id', )
    ordering = ('id', )
    list_filter = ('createDateTime',)
    search_fields = ('user', 'log')
    list_per_page = 20
    readonly_fields = ('user', 'log')

@admin.register(Photo_log)
class Photo_log(admin.ModelAdmin):
    list_display = ('id', 'user', 'Photo', 'createDateTime')
    list_display_links = ('id',)
    ordering = ('id',)
    list_filter = ('createDateTime',)
    search_fields = ('Photo', 'user')
    list_per_page = 50

@admin.register(CashCoin)
class cashcoin(admin.ModelAdmin):
    list_display = ('id', 'user', 'createDateTime')
    list_display_links = ('id', )
    ordering = ('id', )
    list_filter = ('createDateTime',)
    search_fields = ('user', 'log')
    list_per_page = 20
    readonly_fields = ('user', 'log')

@admin.register(Coinvideo)
class coinvideo(admin.ModelAdmin):
    list_display = ('id', 'user', 'createDateTime', 'all_video')
    list_display_links = ('id', )
    ordering = ('id', )
    list_filter = ('createDateTime',)
    search_fields = ('user', 'log')
    list_per_page = 20
    readonly_fields = ('user', 'log')
    def all_video(self, obj):
        # p = Coin_video.objects.filter(~Q(coin_video=201), ~Q(coin_video=1001)).count()
        p = Coinvideo.objects.all().count()
        return p

@admin.register(CreateUser)
class createuser(admin.ModelAdmin):
    list_display = ('id', 'createDateTime')
    list_display_links = ('id', )
    ordering = ('id', )
    list_filter = ('createDateTime',)
    search_fields = ('log',)
    list_per_page = 20
    readonly_fields = ('log',)

@admin.register(Crash)
class Crash(admin.ModelAdmin):
    list_display = ('id', 'user', 'createDateTime')
    list_display_links = ('id', )
    ordering = ('id', )
    list_filter = ('createDateTime',)
    search_fields = ('log', 'user')
    list_per_page = 20
    #readonly_fields = ('user', 'log')
