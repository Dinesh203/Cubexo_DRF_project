# Generated by Django 4.0 on 2021-12-28 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR_management_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_owner',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
    ]
