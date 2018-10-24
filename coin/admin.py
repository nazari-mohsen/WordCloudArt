from django.contrib import admin
from coin.models import  Coin_video, Coin_price


@admin.register(Coin_video)
class coin_video(admin.ModelAdmin):
    list_display = ('id', 'coin_video', 'createDateTime', 'user')
    list_display_links = ('id',)
    list_filter = ('createDateTime',)
    list_per_page = 20

@admin.register(Coin_price)
class coin_price(admin.ModelAdmin):
    list_display = ('id', 'coin_price', 'createDateTime', 'user')
    list_display_links = ('id',)
    list_filter = ('createDateTime',)
    list_per_page = 20