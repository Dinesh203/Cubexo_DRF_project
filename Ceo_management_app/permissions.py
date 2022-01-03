
from rest_framework.permissions import BasePermission
from rest_framework.response import Response


class IsCompanyManager(BasePermission):
    """ CEO permissions """

    def has_permission(self, request, view):
        """ Check permissions """
        print("request", request.user.role)
        if request.user.role == "CEO":
            return True
        else:
            return Response({'error': 'not have permissions only company head access this function'})

    # def has_object_permission(self, request, view, obj):
    #     """ object level permissions """
    #     print(obj)
