# Generated by Django 4.0 on 2022-01-06 07:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR_management_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdevelopment',
            name='dead_line',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectdevelopment',
            name='team',
            field=models.ManyToManyField(blank=True, related_name='User', to=settings.AUTH_USER_MODEL),
        ),
    ]
