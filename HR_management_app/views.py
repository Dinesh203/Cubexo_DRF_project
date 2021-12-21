# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from HR_management_app.models import User
from HR_management_app.serializers import EmployeeSerializer, ProjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.permissions import IsAuthenticated


# Create your views here.

class AllUserView(ModelViewSet):
    """ get all Employees detail """
    serializer_class = EmployeeSerializer
    queryset = User.objects.all()


class EmployeeView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = EmployeeSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EmployeeView(APIView):
#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # permission_classes = [IsAuthenticated]
#
#     def get(self, request, format=None):
#         content = {
#             'user': str(request.user),  # `django.contrib.auth.User` instance.
#             'auth': str(request.auth),  # None
#         }
#         return Response(content)


class ViewEmployees(APIView):
    """ get users
    """
    def get(self, request):
        content = {'message': "Hello, Dinesh"}
        user = User.objects.all()
        serializer = EmployeeSerializer(user, many=True)
        return Response(serializer.data)
