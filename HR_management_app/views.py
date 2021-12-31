
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


class EmployeeDetail(CeoManage):
    """ Employee can get self profile details.
    """
    pass
    # def get(self, request, pk=None):
    #     """Get Employee Detail"""
    #     super(EmployeeDetail, self).get(request, pk)


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
