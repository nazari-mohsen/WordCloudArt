from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Request_photo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                              verbose_name=_('owner'),
                              related_name='Request_photo',
                              help_text=_('please choose owner Coin_price'),
                              blank=True,
                              on_delete=models.CASCADE,
                              null=True
                              )
    log = models.TextField(verbose_name=_('log'))
    createDateTime = models.DateTimeField(_('create date'), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _('Request_photo')
        verbose_name_plural = _('Request_photo')


class Coinvideo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                              verbose_name=_('owner'),
                              related_name='Coinvideo',
                              help_text=_('please choose owner Coin_price'),
                              blank=True,
                              on_delete=models.CASCADE,
                              null=True
                              )
    log = models.TextField(verbose_name=_('log'))
    createDateTime = models.DateTimeField(_('create date'), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _('Coinvideo')
        verbose_name_plural = _('Coinvideo')

class CashCoin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                              verbose_name=_('owner'),
                              related_name='CashCoin',
                              help_text=_('please choose owner Coin_price'),
                              blank=True,
                              on_delete=models.CASCADE,
                              null=True
                              )
    log = models.TextField(verbose_name=_('log'))
    createDateTime = models.DateTimeField(_('create date'), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _('CashCoin')
        verbose_name_plural = _('CashCoin')

class CreateUser(models.Model):
    log = models.TextField(verbose_name=_('log'))
    createDateTime = models.DateTimeField(_('create date'), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _('CreateUser')
        verbose_name_plural = _('CreateUser')