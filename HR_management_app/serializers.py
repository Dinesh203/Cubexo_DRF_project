from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
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


class ChangePasswordSerializer(serializers.ModelSerializer):
    """ Change password serializer class"""
    new_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'new_password', 'confirm_password')

    def validate(self, attrs):
        print("attrs", attrs)
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def validate_old_password(self, value):
        """ Validate old password """
        user = self.context['request'].user
        print("user", user.role)
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        """ update serialize instance in hasher form """
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance
