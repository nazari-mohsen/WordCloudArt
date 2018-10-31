# Generated by Django 2.1.2 on 2018-10-31 10:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20181031_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='url',
            field=models.FileField(upload_to='version/', validators=[django.core.validators.FileExtensionValidator(['apk'])], verbose_name='file'),
        ),
    ]
