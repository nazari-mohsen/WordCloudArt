import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from cloud import settings



class User(AbstractUser):
    # user_key = models.CharField(_('User Key'), max_length=42, default=uuid.uuid4, unique=True)
    # phone_number = models.CharField(_('Phone Number'), max_length=20, null=True, blank=True)
    i = models.CharField(_('IMEI'), max_length=20, null=True)
    ar = models.CharField(_('Android version'), max_length=10, default="26")
    are = models.CharField(_('Application version'), max_length=2, default="1")
    ms = models.CharField(_('MAC Address'), max_length=50, null=True)
    ad = models.CharField(_('android_id'), max_length=50, null=True)
    br = models.CharField(_('android_brand'), max_length=50, null=True)
    iam = models.CharField(_('im_id_mac'), max_length=200)
    # coin = models.IntegerField(_('Coin_sum'), default=0, unique=False)
    Password_user = models.CharField(_('Password'), max_length=20, default="123456789")
    class Meta:
        indexes = [
            models.Index(fields=['ad'], name='android_id_idx'),
            models.Index(fields=['i'], name='imei_idx'),
            models.Index(fields=['ms'], name='MAC_Address_idx'),
            # models.Index(fields=['user_key'], name='user_key_idx'),
        ]

        verbose_name = _('User')
        verbose_name_plural = _('User')


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile",
                                primary_key=True)

    coin_video = models.IntegerField(_('Coin_video'), default=0, unique=False)
    coin_price = models.IntegerField(_('Coin_price'), default=0, unique=False)
    coin = models.IntegerField(_('Coin_sum'), default=0, unique=False)

    class Meta:
        indexes = [
            models.Index(fields=['coin'], name='coin_idx'),
            models.Index(fields=['coin_video'], name='coin_video_idx'),
            models.Index(fields=['coin_price'], name='coin_price_idx'),
        ]
        ordering = ['-coin']
        verbose_name = _('Profile')
        verbose_name_plural = _('Profile')

