# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-30 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20181030_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='watermark',
            field=models.FileField(default='1', upload_to='config/', verbose_name='watermark'),
        ),
        migrations.AlterField(
            model_name='version',
            name='url',
            field=models.FileField(default='1', upload_to='version/', verbose_name='file'),
        ),
    ]
