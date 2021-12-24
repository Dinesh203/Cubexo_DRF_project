from rest_framework import serializers
from django.contrib.auth.hashers import make_password
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

    def create(self, validated_data):
        """ Create and return a new `User` instance, given the validated data."""
        user = super(EmployeeSerializer, self).create(validated_data)
        user.password = make_password(validated_data['password'])
        user.save()
        return user


class ProjectSerializer(serializers.ModelSerializer):
    """ UserSerializer model class """

    class Meta:
        """ User serializer Meta class """
        model = Project
        fields = ['id', 'project_name', 'description', 'date_of_assign']
