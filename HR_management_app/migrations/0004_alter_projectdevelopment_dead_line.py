# Generated by Django 4.0 on 2022-01-04 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR_management_app', '0003_alter_projectdevelopment_dead_line_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdevelopment',
            name='dead_line',
            field=models.DateField(blank=True),
        ),
    ]