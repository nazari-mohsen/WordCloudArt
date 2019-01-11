# Generated by Django 2.1.2 on 2018-11-25 17:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0022_remove_config_colormap'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help_App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, unique=True, verbose_name='title')),
                ('status', models.CharField(choices=[('0', 'Draft'), ('1', 'Published')], default='0', max_length=4, verbose_name='status')),
                ('order', models.PositiveIntegerField(default=1, verbose_name='order')),
                ('url', models.FileField(upload_to='help/', validators=[django.core.validators.FileExtensionValidator(['jpg'])], verbose_name='file')),
                ('createDateTime', models.DateTimeField(auto_now_add=True, verbose_name='create date')),
                ('owner', models.ForeignKey(blank=True, default=1, help_text='please choose owner post', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'verbose_name': 'help',
                'verbose_name_plural': 'helps',
            },
        ),
    ]
