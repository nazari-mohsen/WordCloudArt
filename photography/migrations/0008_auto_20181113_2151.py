# Generated by Django 2.1.2 on 2018-11-13 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0012_auto_20181030_1953'),
        ('photography', '0007_auto_20181112_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thumbnail',
            name='category',
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='category',
            field=models.ManyToManyField(related_name='thumbnail_photo', to='category.Category', verbose_name='category'),
        ),
    ]
