from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

from account.models import User, Profile


# admin.site.register(User, UserAdmin)

@admin.register(User)
class ConfigAdmin(admin.ModelAdmin):
   list_display = ('id', 'i', 'username', 'mr', 'ar', 'are', 'br', 'ad')
   list_display_links = ('username', )
   ordering = ('-id', )
   list_filter = ('are', 'mr', 'br', 'ar')
   search_fields = ('i', )
   list_per_page = 20


@admin.register(Profile)
class ConfigA(admin.ModelAdmin):
    list_display = ('user_id', 'user', 'coin', 'coin_video', 'coin_price')
    list_display_links = ('user_id', )
    ordering = ('user_id', )
    # list_filter = ('user',)
    search_fields = ('coin_price', )
    list_per_page = 20
