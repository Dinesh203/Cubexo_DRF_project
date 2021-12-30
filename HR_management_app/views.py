
from django.http import HttpResponse, Http404
from rest_framework.viewsets import ModelViewSet
from .models import User, Project, ProjectDevelopment
from .serializers import EmployeeSerializer, ProjectSerializer, ProjectDevelopmentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics


# Create your views here.

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

    def get(self, request, pk=None):
        if pk:
            user = User.objects.filter(pk=pk)
            if not user:
                return Response({"status": "invalid username or id"})
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
            print("pk", pk)
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
    """ Ceo can get Project Development status and make update"""

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
        print(serializer)
        if serializer.is_valid():
            print('Hii')
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
                return Response({'status': 'id not found'})
            development_status.delete()
            return Response({"status": "success", "data": "Item Deleted"})
        else:
            return Response({'error': 'user id not found'})


class HrAllEmployeeView(ModelViewSet):
    """ get all Employees detail """
    serializer_class = EmployeeSerializer
    queryset = User.objects.all()


class HrUpdateEmployee(generics.RetrieveUpdateDestroyAPIView):
    """ Hr can Update Retrieves and Delete employees details """
    lookup_field = 'pk'
    serializer_class = EmployeeSerializer
    queryset = User.objects.all()


class HrProjectView(CeoProjects):
    """ Hr can get all and retrieve project details"""
    pass


class EmployeeDetail(CeoProjects):
    """ Employee can get self profile details.
    """

    def get(self, request, pk=None):
        super(EmployeeDetail, self).get(request, pk)


class EmployeeProject(CeoProjects):
    """ get projects details.
    """
    pass
    # def dispatch(self, request, *args, **kwargs):
    #     view_responce = lambda x: super(CeoManage, self).dispatch(request, *args, **kwargs)
    #     if request.user.is_authenticated:
    #         if request.user.role == "CEO":
    #             return view_responce(None)
    #         elif request.user.role == "HR":
    #             pass
    #     return HttpResponse("You do not have permission")
