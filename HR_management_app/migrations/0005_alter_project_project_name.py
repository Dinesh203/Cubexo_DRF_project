# Generated by Django 4.0 on 2021-12-29 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR_management_app', '0004_remove_projectdevelopment_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(default=None, max_length=50, unique=True),
        ),
    ]
