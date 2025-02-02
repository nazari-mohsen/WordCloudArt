from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.utils.html import format_html


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
                              on_delete=models.CASCADE,
                              default=1
                              )
    title = models.CharField(max_length=70, verbose_name=_('title'), unique=True)
    status = models.CharField(_('status'), choices=STATUS_CHOICES, default='0', max_length=4)
    content = models.TextField(verbose_name=_('content'), null=False)
    watermark = models.FileField(_('watermark'), upload_to='config/', validators=[FileExtensionValidator(['png'])], null=False)
    createDateTime = models.DateTimeField(_('create date'), auto_now=False, auto_now_add=True)
    updateDateTime = models.DateTimeField(_('update date'), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Config')
        verbose_name_plural = _('Config')

    def image_tag(self):
        return format_html(u'<img src="%s" width="50" height="50"/>' % (self.watermark.url))

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
    url = models.FileField(_('file'), upload_to='version/', validators=[FileExtensionValidator(['apk'])], null=False)
    ver = models.IntegerField(verbose_name=_('ver_number'), null=False, default=None)
    createDateTime = models.DateTimeField(_('create date'), auto_now=False, auto_now_add=True)


    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _('version')
        verbose_name_plural = _('versions')


class Help_App(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              verbose_name=_('owner'),
                              help_text=_('please choose owner post'),
                              blank=True,
                              on_delete=models.CASCADE,
                              null=True,
                              default=1
                              )

    title = models.CharField(max_length=70, verbose_name=_('title'), unique=True)
    status = models.CharField(_('status'), choices=STATUS_CHOICES, default='0', max_length=4)
    order = models.PositiveIntegerField(_('order'), default=1)
    url = models.FileField(_('file'), upload_to='help/', validators=[FileExtensionValidator(['jpg'])], null=False)
    createDateTime = models.DateTimeField(_('create date'), auto_now=False, auto_now_add=True)

    def image_tag(self):
        return format_html(u'<img src="%s" width="50" height="50"/>' % (self.url.url))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('help')
        verbose_name_plural = _('helps')
