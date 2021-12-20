from django.urls import path
from HR_management_app.views import *
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from django.contrib.auth.models import User
from rest_framework import viewsets