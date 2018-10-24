from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings




class Coin_video(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                              verbose_name=_('owner'),
                              related_name='Coin_video',
                              help_text=_('please choose owner Coin_video'),
                              blank=True,
                              on_delete=models.CASCADE,
                              null=True
                              )
    coin_video = models.IntegerField(_('Coin_video'), default=0, unique=False)
    createDateTime = models.DateTimeField(_('create date'), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _('Coin_video')
        verbose_name_plural = _('Coin_video')


class Coin_price(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                              verbose_name=_('owner'),
                              related_name='Coin_price',
                              help_text=_('please choose owner Coin_price'),
                              blank=True,
                              on_delete=models.CASCADE,
                              null=True
                              )
    coin_price = models.IntegerField(_('coin_price'), default=0, unique=False)
    orderId = models.CharField(verbose_name=_('orderId'), max_length=42, default=0)
    createDateTime = models.DateTimeField(_('create date'), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _('Coin_price')
        verbose_name_plural = _('Coin_price')