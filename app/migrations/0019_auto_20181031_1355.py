# Generated by Django 2.1.2 on 2018-10-31 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20181031_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='save_place',
            field=models.CharField(default='0', max_length=70, verbose_name='save_place'),
        ),
        migrations.AlterField(
            model_name='config',
            name='url_pre',
            field=models.CharField(default='0', max_length=70, verbose_name='url_pre'),
        ),
        migrations.AlterField(
            model_name='version',
            name='ver',
            field=models.IntegerField(default=None, verbose_name='ver_number'),
        ),
    ]
