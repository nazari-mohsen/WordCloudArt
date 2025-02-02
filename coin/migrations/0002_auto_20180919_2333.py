# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-19 19:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coin_price',
            options={'verbose_name': 'Coin_price', 'verbose_name_plural': 'Coin_price'},
        ),
        migrations.AlterModelOptions(
            name='coin_video',
            options={'verbose_name': 'Coin_video', 'verbose_name_plural': 'Coin_video'},
        ),
        migrations.AddField(
            model_name='coin_price',
            name='orderId',
            field=models.CharField(default=0, max_length=42, verbose_name='orderId'),
        ),
        migrations.AlterField(
            model_name='coin_price',
            name='user',
            field=models.ForeignKey(blank=True, help_text='please choose owner Coin_price', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Coin_price', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AlterField(
            model_name='coin_video',
            name='user',
            field=models.ForeignKey(blank=True, help_text='please choose owner Coin_video', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Coin_video', to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
    ]
