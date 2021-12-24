# from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, user_logged_in
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from HR_management_app.models import User, Project, ProjectDevelopment, Attendance
from HR_management_app.serializers import EmployeeSerializer, ProjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.

def get_object(id):
    try:
        return User.objects.get(id=id)
    except User.DoesNotExist:
        raise Http404


# def check_role():
#     user = User.objects.get('role' == 'CEO')
#     if user:
#         return user
#     else:
#         raise Http404

# def has(serializer):
#     up = User.objects.get(email=serializer.data["email"])
#     up.password = make_password(serializer.data["email"])
#     up.save()

class CeoManage(APIView):
    """ get users
    """
    # def dispatch(self, request, *args, **kwargs):
    #     view_responce = lambda x: super(CeoManage, self).dispatch(request, *args, **kwargs)
    #     if request.user.is_authenticated:
    #         if request.user.role == "CEO":
    #             return view_responce(None)
    #         elif request.user.role == "HR":
    #             pass
    #     return HttpResponse("You do not have permission")

    def get(self, request, id=None):
        if id:
            user = User.objects.get(id=id)
            serializer = EmployeeSerializer(user)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        user = User.objects.all()
        serializer = EmployeeSerializer(user, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        user = get_object(id)
        serializer = EmployeeSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        user = get_object(id)
        print(user)
        user.delete()
        return Response({"status": "success", "data": "Item Deleted"})


class CeoProjects(generics.ListAPIView):
    """ company head can get project detail """
    serializer_class = ProjectSerializer
    queryset = User.objects.all()

    pass

# class CeoProjectDevelopment()


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


class AllEmployeeView(ModelViewSet):
    """ get all Employees detail """
    permission_classes = (IsAuthenticated,)
    serializer_class = EmployeeSerializer
    queryset = User.objects.all()


class EmployeeView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    pass
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        detail = request.data
        print(detail)
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
