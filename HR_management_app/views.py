from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, user_logged_in
from rest_framework.viewsets import ModelViewSet
from .models import User, Project, ProjectDevelopment, Attendance
from .serializers import EmployeeSerializer, ProjectSerializer, ProjectDevelopmentSerializer, AttendanceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status, generics


# Create your views here.

def get_object(pk):
    """ get User detail """
    try:
        return User.objects.get(pk=pk)
    except Exception as e:
        Response(e)


def get_project_object(pk):
    """ get User detail """
    try:
        return Project.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404


def check_role_ceo():
    """ Check Role"""
    user = User.objects.get('role' == 'CEO')
    if user:
        return user
    else:
        raise Http404


class projectStatus(APIView):
    """ Project status change"""
    def patch(self, request, pk):
        project = Project.objects.get(pk=pk)

        project.status = False if project.status else True
        project.save()



class CeoManage(APIView):
    """ get users
    """

    def get(self, request, id=None):
        if id:
            user = User.objects.filter(id=id)
            if not user:
                return Response({"status": "invalid username or id"})
            serializer = EmployeeSerializer(get_object(id))
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


class CeoProjects(generics.ListCreateAPIView):
    """ company head can get project detail """
    try:
        serializer_class = ProjectSerializer
        queryset = Project.objects.all()
    except Exception as e:
        Response(e)


class CeoUpdateProject(generics.RetrieveUpdateDestroyAPIView):
    """ company head can retrieve Update and delete project detail """
    lookup_field = 'pk'
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


# class


class HrAllEmployeeView(ModelViewSet):
    """ get all Employees detail """
    serializer_class = EmployeeSerializer
    queryset = User.objects.all()


class HrUpdateEmployee(generics.RetrieveUpdateDestroyAPIView):
    """ Hr can Update Retrieves and Delete employees details """
    lookup_field = 'pk'
    serializer_class = EmployeeSerializer
    queryset = User.objects.all()


class HrProjectView(APIView):
    """ Hr can get all and retrieve project details"""
    def get(self, request, pk=None):
        if pk:
            print(pk)
            user = User.objects.filter(pk=pk)
            print(user)
            if not user:
                return Response({'status': 'invalid username or id'})
            serializer = ProjectSerializer(Project.objects.get(pk=pk))
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        serializer = ProjectSerializer(Project.objects.all(), many=True)
        return Response(serializer.data)


class EmployeeDetail(APIView):
    """ Employee can get self profile details.
    """
    def get(self, request):
        # if request.auth is None:
        #     pass
        user = request.user
        serializer = EmployeeSerializer(request.user)
        return Response(serializer.data)


class EmployeeProject(APIView):
    """
    get projects details.
    """
    http_method_names = ['get', 'head']

    def get(self, request):
        project = Project.objects.get('user_id')
        # detail = request.user
        # print("detail:", detail)
        serializer = ProjectSerializer(request.user, many=True)
        return Response(serializer.data)

    # def dispatch(self, request, *args, **kwargs):
    #     view_responce = lambda x: super(CeoManage, self).dispatch(request, *args, **kwargs)
    #     if request.user.is_authenticated:
    #         if request.user.role == "CEO":
    #             return view_responce(None)
    #         elif request.user.role == "HR":
    #             pass
    #     return HttpResponse("You do not have permission")
