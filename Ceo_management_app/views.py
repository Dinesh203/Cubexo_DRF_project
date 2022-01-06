""" This is IT company management app views"""
from django.http import HttpResponse, Http404
from HR_management_app.models import User, Project, ProjectDevelopment
from HR_management_app.serializers import EmployeeSerializer, ProjectSerializer, ProjectDevelopmentSerializer, \
    ChangePasswordSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from Ceo_management_app.permissions import IsCompanyManager, CheckEmployeeStatus


# Create your views here.

class ChangeProjectStatus(APIView):
    """ Project status change
    """
    def patch(self, request, pk):
        print("request", request.data['status'])
        print("request", request.user.role)
        print("pk", pk)
        project = Project.objects.get(pk=pk)
        project.status = False if project.status else True
        project.save()
        return Response(status.HTTP_200_OK)


class CeoManage(APIView):
    """ company manager can get details, add new employee, update detail, and delete
    employees """
    permission_classes = (IsCompanyManager, CheckEmployeeStatus)

    def get(self, request, pk=None):
        if pk:
            user = User.objects.filter(pk=pk)
            if not user:
                return Response({"status": "invalid user or id"})
            serializer = EmployeeSerializer(User.objects.get(pk=pk))
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        user = User.objects.all()
        serializer = EmployeeSerializer(user, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        if pk:
            try:
                serializer_data = EmployeeSerializer(User.objects.get(id=pk), data=request.data, partial=True)
            except Exception as e:
                return HttpResponse(e)
            print(serializer_data)
            if serializer_data.is_valid():
                serializer_data.save()
                return Response({"status": "success", "data": serializer_data.data})
            else:
                return Response({"status": "error", "data": serializer_data.errors})
        else:
            return Response({"status": "invalid detail or attribute"})

    def delete(self, request, pk=None):
        if pk:
            user = User.objects.filter(pk=pk)
            if not user:
                return Response({'status': 'page not found'})
            user.delete()
            return Response({"status": "success", "data": "Item Deleted"})
        else:
            return Response({'error': 'user id not found'})


class CeoProjects(APIView):
    """ company head can get project detail
    """

    def get(self, request, pk=None):
        if pk:
            project = Project.objects.filter(pk=pk)
            if not project:
                return Response({'status': 'invalid username or id'})
            serializer = ProjectSerializer(Project.objects.get(pk=pk))
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        serializer = ProjectSerializer(Project.objects.all(), many=True)
        return Response(serializer.data)


class CeoUpdateProject(APIView):
    """ company head can retrieve Update and delete project detail """

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        if pk:
            try:
                serializer = ProjectSerializer(Project.objects.get(pk=pk), data=request.data, partial=True)
            except Exception:
                return Response({'error': 'matching query does not exist'})
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors})
        else:
            return Response({"status": "invalid detail or attribute"})

    def delete(self, request, pk=None):
        if pk:
            project = Project.objects.filter(pk=pk)
            if not project:
                return Response({'status': 'id not found'})
            project.delete()
            return Response({"status": "success", "data": "Item Deleted"})
        else:
            return Response({'error': 'user id not found'})


class DevelopmentStatus(APIView):
    """ Ceo can get Project Development status and make update
    """
    def get(self, request, pk=None):
        if pk:
            try:
                project = ProjectDevelopment.objects.get(pk=pk)
            except Exception:
                return Response({'error': 'id does not exist'})
            if not project:
                Response({'error': "Not have any detail"})
            serializer = ProjectDevelopmentSerializer(ProjectDevelopment.objects.get(pk=pk))
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        serializer = ProjectDevelopmentSerializer(ProjectDevelopment.objects.all(), many=True)
        return Response(serializer.data)


class AddDevelopmentStatus(APIView):
    """ Create developments status """

    def post(self, request):
        serializer = ProjectDevelopmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        if pk:
            try:
                serializer = ProjectDevelopmentSerializer(ProjectDevelopment.objects.get(pk=pk), data=request.data,
                                                          partial=True)
            except Exception:
                return Response({'error': 'matching query does not exist'})
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            else:
                return Response({"status": "error", "data": serializer.errors})
        else:
            return Response({"status": "invalid detail or attribute"})

    def delete(self, request, pk=None):
        if pk:
            development_status = ProjectDevelopment.objects.filter(pk=pk)
            if not development_status:
                return Response({'status': 'user id not found'})
            development_status.delete()
            return Response({"status": "success", "data": "Item Deleted"})
        else:
            return Response({'error': 'user id not found'})


class ChangePasswordView(generics.UpdateAPIView):
    """ Employees/User can Change password """

    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer

