# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-24 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20181001_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.FileField(blank=True, null=True, upload_to='photography/category/', verbose_name='extra files'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['title'], name='title'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['url'], name='url'),
        ),
    ]
