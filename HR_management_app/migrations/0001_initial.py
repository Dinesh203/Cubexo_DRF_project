# Generated by Django 4.0 on 2021-12-21 09:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=1000)),
                ('date_of_assign', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('employee_id', models.CharField(default='employee_id', max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('gender', models.EmailField(blank=True, choices=[('male', 'MALE'), ('female', 'FEMALE')], max_length=200)),
                ('is_employee', models.BooleanField(default=False)),
                ('role', models.CharField(choices=[('1', 'PROJECT MANAGER'), ('2', 'TECHNICAL LEAD/TEAM LEADER'), ('3', 'CHIEF ARCHITECT'), ('4', 'SOFTWARE ARCHITECT'), ('5', 'SENIOR SOFTWARE DEVELOPER'), ('6', 'SOFTWARE ENGINEER'), ('7', 'JUNIOR SOFTWARE DEVELOPER'), ('8', 'INTERN SOFTWARE DEVELOPER'), ('9', 'SOFTWARE ADMINISTRATOR'), ('10', 'ABCD')], default=None, max_length=100, null=True)),
                ('employment_data', models.DateField(auto_now_add=True)),
                ('contact', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField(blank=True, default=None, null=True)),
                ('address', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('add', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectDevelopment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR_management_app.project')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR_management_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout', models.BooleanField(default=False, null=True)),
                ('presents', models.CharField(default=0, max_length=50)),
                ('leaves', models.CharField(default=0, max_length=50)),
                ('absents', models.CharField(default=0, max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR_management_app.user')),
            ],
        ),
    ]