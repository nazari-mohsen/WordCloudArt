# Generated by Django 2.1.2 on 2018-10-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0011_auto_20181030_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=250, unique=True, verbose_name='title'),
        ),
    ]
