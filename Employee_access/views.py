from Ceo_management_app.views import CeoManage, CeoProjects
from rest_framework.response import Response
from Ceo_management_app.permissions import CheckEmployeeStatus
from rest_framework import status
from rest_framework.views import APIView
from HR_management_app.serializers import EmployeeSerializer
from HR_management_app.models import User


# Create your views here.


class EmployeeDetail(APIView):
    """ Employee can get self profile details.
    """
    permission_classes = (CheckEmployeeStatus,)

    def get(self, request):
        user = User.objects.get(pk=request.user.pk)
        serializer = EmployeeSerializer(user)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class EmployeeProject(CeoProjects):
    """ get projects details.
    """
    permission_classes = (CheckEmployeeStatus,)
    pass

    # def dispatch(self, request, *args, **kwargs):
    #     view_responce = lambda x: super(CeoManage, self).dispatch(request, *args, **kwargs)
    #     if request.user.is_authenticated:
    #         if request.user.role == "CEO":
    #             return view_responce(None)
    #         elif request.user.role == "HR":
    #             pass
    #     return HttpResponse("You do not have permission")
