
from django.shortcuts import render
from Ceo_management_app.views import CeoManage, CeoProjects
from rest_framework.response import Response
from HR_management_app.serializers import EmployeeSerializer
from HR_management_app.models import User

# Create your views here.


class EmployeeDetail(CeoManage):
    """ Employee can get self profile details.
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
