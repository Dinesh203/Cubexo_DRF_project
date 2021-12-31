
from rest_framework.permissions import BasePermission
from rest_framework.response import Response


class IsCompanyManager(BasePermission):
    """ CEO permissions """
    print("hello")

    def has_permission(self, request, view):
        """ Check permissions """
        print("request", request.user)
        print(request.auth)
        print(request)
        print(view)
        role = request.user.role
        print(role)
        if role:
            if role == "CEO":
                return True
            else:
                return Response({'error': 'not have permissions'})
