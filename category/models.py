from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
STATUS_CHOICES = (
    ('0', _('De-Active')),
    ('1', _('Active'))
)


class Category(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              verbose_name=_('owner'),
                              help_text=_('please choose owner post'),
                              blank=True,
                              on_delete=models.CASCADE,
                              default=1
                              )
    title = models.CharField(_('title'), max_length=250)
    order = models.PositiveIntegerField(_('order'), default=1)
    status = models.CharField(_('status'), choices=STATUS_CHOICES, default='1', max_length=2)
    url = models.FileField(_('extra files'), upload_to='photography/category/', null=True, blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=['title'], name='title'),
            models.Index(fields=['order'], name='order'),
            models.Index(fields=['url'], name='url'),
        ]
        verbose_name = _('Category')
        verbose_name_plural = _('Categorys')
