# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-12 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0009_auto_20181003_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo_mask',
            name='max_word',
            field=models.PositiveIntegerField(default=50, verbose_name='max_word'),
        ),
        migrations.AlterField(
            model_name='photo_mask',
            name='medium_word',
            field=models.PositiveIntegerField(default=100, verbose_name='medium_word'),
        ),
        migrations.AlterField(
            model_name='photo_mask',
            name='min_word',
            field=models.PositiveIntegerField(default=200, verbose_name='min_word'),
        ),
    ]
