
from rest_framework import serializers
from HR_management_app.models import User, Project, ProjectDevelopment, Attendance
from django.contrib.auth.hashers import make_password


class EmployeeSerializer(serializers.ModelSerializer):
    """ UserSerializer model class """

    class Meta:
        """ User serializer Meta class """
        model = User
        fields = ['id', 'name', 'email', 'password', 'gender', 'is_employee',
                  'role', 'employment_date', 'contact', 'date_of_birth', 'address']
        extra_kwargs = {'password': {'write_only': True}}


class ProjectSerializer(serializers.ModelSerializer):
    """ UserSerializer model class """

    class Meta:
        """ User serializer Meta class """
        model = Project
        fields = ['id', 'project_name', 'description', 'date_of_assign']
