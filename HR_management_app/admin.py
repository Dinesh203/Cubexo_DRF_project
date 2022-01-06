from django.contrib import admin
from .models import User, Project, ProjectDevelopment, Attendance, ClientDetail
# Register your models here.

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Attendance)
admin.site.register(ProjectDevelopment)
admin.site.register(ClientDetail)
