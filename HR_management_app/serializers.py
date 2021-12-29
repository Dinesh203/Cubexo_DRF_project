from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Project, ProjectDevelopment, Attendance
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
    """ ProjectSerializer model class """

    class Meta:
        """ User Project serializer Meta class """
        model = Project
        fields = '__all__'


class ProjectDevelopmentSerializer(serializers.ModelSerializer):
    """ ProjectDevelopment Serializer model class """
    project = serializers.StringRelatedField(read_only=True)
    team_leader = serializers.StringRelatedField(read_only=True)
    team = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        """ User ProjectDevelopment serializer Meta class """
        model = ProjectDevelopment
        fields = ['id', 'project', 'team_leader', 'team', 'dead_line', 'progress', 'project']


class AttendanceSerializer(serializers.ModelSerializer):
    """ AttendanceSerializer model class """

    class Meta:
        """ Attendance serializer Meta class """
        model = Attendance
        fields = '__all__'
