
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import EmployeeSerializer
from rest_framework import status, generics
from Ceo_management_app.views import CeoProjects, CeoManage

# Create your views here.


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

