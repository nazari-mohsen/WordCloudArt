from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.validators import FileExtensionValidator



STATUS_CHOICES = (
    ('0', _('Draft')),
    ('1', _('Published'))
)

class Config(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              verbose_name=_('owner'),
                              help_text=_('please choose owner post'),
                              blank=True,
                              null=True,
                              default=1
                              )
    title = models.CharField(max_length=70, verbose_name=_('title'), null=True)
    status = models.CharField(_('status'), choices=STATUS_CHOICES, default='0', max_length=4)
    content = models.TextField(verbose_name=_('content'))
    url_pre = models.CharField(max_length=70, verbose_name=_('url_pre'), null=True)
    watermark = models.FileField(_('watermark'), upload_to='config/', validators=[FileExtensionValidator(['png'])])
    save_place = models.CharField(max_length=70, verbose_name=_('save_place'), null=True)
    createDateTime = models.DateTimeField(_('create date'), auto_now=False, auto_now_add=True)
    updateDateTime = models.DateTimeField(_('update date'), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Config')
        verbose_name_plural = _('Config')

class version(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              verbose_name=_('owner'),
                              help_text=_('please choose owner post'),
                              blank=True,
                              on_delete=models.CASCADE,
                              null=True,
                              default=1
                              )

    content = models.TextField(verbose_name=_('content'))
    status = models.CharField(_('status'), choices=STATUS_CHOICES, default='0', max_length=4)
    url = models.FileField(_('file'), upload_to='version/', validators=[FileExtensionValidator(['apk'])])
    ver = models.IntegerField(verbose_name=_('ver_number'), null=True, default=None)
    createDateTime = models.DateTimeField(_('create date'), auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _('version')
        verbose_name_plural = _('versions')


