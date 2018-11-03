from django.urls import reverse
from django.db import models
from category.models import Category
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import jdatetime
from django.core.validators import FileExtensionValidator
from django.utils.html import format_html

STATUS_CHOICES = (
    ('0', _('Draft')),
    ('1', _('Published'))
)

class photo_Mask(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              verbose_name=_('owner'),
                              help_text=_('please choose owner post'),
                              blank=True,
                              on_delete=models.CASCADE,
                              default=1
                              )
    title = models.CharField(max_length=70, verbose_name=_('title'), unique=True, null=False)
    min_word = models.PositiveIntegerField(_('min_word'), default=200, null=False)
    medium_word = models.PositiveIntegerField(_('medium_word'), default=100, null=False)
    max_word = models.PositiveIntegerField(_('max_word'), default=50, null=False)
    publish = models.DateTimeField(_('publish'), default=timezone.now)
    url = models.FileField(_('extra files'), upload_to='photography/photo_Mask/', validators=[FileExtensionValidator(['jpg'])], null=False)
    createDateTime = models.DateTimeField(_('create date'), auto_now=False, auto_now_add=True)
    updateDateTime = models.DateTimeField(_('update date'), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=['min_word'], name='min_word'),
            models.Index(fields=['medium_word'], name='medium_word'),
            models.Index(fields=['max_word'], name='max_word'),
            models.Index(fields=['url'], name='url'),
        ]

        verbose_name = _('photo_Mask')
        verbose_name_plural = _('photo_Masks')

    def get_absolute_url(self):
        return reverse('images:detail', kwargs={'id': self.id})

    def image_tag(self):
        return format_html(u'<img src="%s" width="50" height="50"/>' % (self.url.url))

    image_tag.short_description = _('photo_Mask')
    image_tag.allow_tags = True


class photo_main(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              verbose_name=_('owner'),
                              help_text=_('please choose owner post'),
                              blank=True,
                              on_delete=models.CASCADE,
                              default=1
                              )
    title = models.CharField(max_length=70, verbose_name=_('title'), unique=True, null=False)
    publish = models.DateTimeField(_('publish'), default=timezone.now)
    url = models.FileField(_('extra files'), upload_to='photography/photo_main/', validators=[FileExtensionValidator(['png'])], null=False)
    createDateTime = models.DateTimeField(_('create date'), auto_now=False, auto_now_add=True)
    updateDateTime = models.DateTimeField(_('update date'), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=['url'], name='url'),
        ]

        verbose_name = _('photo_main')
        verbose_name_plural = _('photo_main')

    def get_absolute_url(self):
        return reverse('images:detail', kwargs={'id': self.id})

    def image_tag(self):
        return format_html(u'<img src="%s" width="50" height="50"/>' % (self.url.url))

    image_tag.short_description = _('photo_main')
    image_tag.allow_tags = True


class thumbnail(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              verbose_name=_('owner'),
                              related_name="thumbnail_photo",
                              help_text=_('please choose owner post'),
                              blank=True,
                              on_delete=models.CASCADE,
                              default=1
                              )
    title = models.CharField(max_length=70, verbose_name=_('title'), unique=True, null=False)
    count = models.IntegerField(verbose_name=_('count'), default=1, null=False)
    cash = models.IntegerField(_('cash'), default=50, unique=False, null=False)
    order = models.PositiveIntegerField(_('order'), default=1)
    status = models.CharField(_('status'), choices=STATUS_CHOICES, default='1', max_length=10)
    url = models.FileField(_('extra files'), upload_to='photography/thumbnail/', validators=[FileExtensionValidator(['jpg'])], null=False)
    category = models.ForeignKey(Category, verbose_name=_('category'), on_delete=models.CASCADE, related_name="thumbnail_photo", null=False)
    photo_Mask = models.ForeignKey(photo_Mask, verbose_name=_('photo_Mask'), on_delete=models.CASCADE, null=False)
    photo_main = models.ForeignKey(photo_main, verbose_name=_('photo_main'), on_delete=models.CASCADE, null=False)
    publish = models.DateTimeField(_('publish'), default=timezone.now)
    createDateTime = models.DateTimeField(_('create date'), auto_now=False, auto_now_add=True)
    updateDateTime = models.DateTimeField(_('update date'), auto_now=True, auto_now_add=False)


    def pre_publish(self):
        return str(jdatetime.datetime.fromgregorian(datetime=self.publish))

    def pre_date_publish(self):
        return str(jdatetime.date.fromgregorian(date=self.publish))


    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=['count'], name='count'),
            models.Index(fields=['cash'], name='cash'),
            models.Index(fields=['url'], name='url'),
        ]

        verbose_name = _('thumbnail')
        verbose_name_plural = _('thumbnail')
        ordering = ['order']

    def get_absolute_url(self):
        return reverse('images:detail', kwargs={'id': self.id})

    def image_tag(self):
        return format_html(u'<img src="%s" width="50" height="50"/>' % (self.url.url))

    image_tag.short_description = _('thumbnail')
    image_tag.allow_tags = True


# class Photo_log(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                               verbose_name=_('user'),
#                               related_name='Photo_log',
#                               help_text=_('please choose owner Coin_price'),
#                               blank=True,
#                               on_delete=models.CASCADE,
#                               null=True
#                               )
#     Photo = models.ForeignKey(thumbnail, verbose_name=_('photo'), on_delete=models.CASCADE, null=False)
#     createDateTime = models.DateTimeField(_('create date'), auto_now=False, auto_now_add=True)
#
#
#     class Meta:
#         verbose_name = _('Photo_log')
#         verbose_name_plural = _('Photo_log')