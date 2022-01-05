# Generated by Django 4.0 on 2022-01-04 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HR_management_app', '0002_alter_projectdevelopment_dead_line_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdevelopment',
            name='dead_line',
            field=models.DateField(default=''),
        ),
        migrations.AlterField(
            model_name='projectdevelopment',
            name='project',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='project_fields', to='HR_management_app.project'),
        ),
        migrations.AlterField(
            model_name='projectdevelopment',
            name='team_leader',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='team_leader', to='HR_management_app.user'),
        ),
    ]