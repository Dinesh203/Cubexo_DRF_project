# from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from HR_management_app.models import User
from HR_management_app.serializers import EmployeeSerializer, ProjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.

class AllEmployeeView(ModelViewSet):
    """ get all Employees detail """
    permission_classes = (IsAuthenticated,)
    serializer_class = EmployeeSerializer
    queryset = User.objects.all()


class EmployeeView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = User.objects.all()
        serializer = EmployeeSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CeoManage(APIView):
    """ get users
    """
    # def dispatch(self, request, *args, **kwargs):
    #     VIEW_RESPONSE = lambda x: super(CeoManage, self).dispatch(request, *args, **kwargs)
    #     if request.user.is_authenticated:
    #         if request.user.role == "CEO":
    #             return VIEW_RESPONSE(None)
    #         elif request.user.role == "HR":
    #             pass
        # return HttpResponse("You do not have permisision")

    def get(self, request):
        user = User.objects.all()
        serializer = EmployeeSerializer(user, many=True)
        return Response(serializer.data)


class HumanResources(APIView):
    """ Human resource management system.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = User.objects.all()
        serializer = EmployeeSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
