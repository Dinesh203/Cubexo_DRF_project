from django.contrib import admin
from HR_management_app.models import User, Project, ProjectDevelopment, Attendance
# Register your models here.

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Attendance)
admin.site.register(ProjectDevelopment)
