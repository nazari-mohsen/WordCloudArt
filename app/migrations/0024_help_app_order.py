# Generated by Django 2.1.2 on 2018-11-25 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_help_app'),
    ]

    operations = [
        migrations.AddField(
            model_name='help_app',
            name='order',
            field=models.PositiveIntegerField(default=1, verbose_name='order'),
        ),
    ]
