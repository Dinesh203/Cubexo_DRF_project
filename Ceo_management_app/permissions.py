from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission
from rest_framework.response import Response


class IsCompanyManager(BasePermission):
    """ CEO permissions """

    def has_permission(self, request, view):
        """ Check permissions """
        print("role", request.user.role)
        if request.user.role == 'CEO' or request.user.role == 'HR':
            return True
        else:
            return False


class CheckEmployeeStatus(BasePermission):
    """ check employee status is active or not.
    """
    def has_permission(self, request, view):
        """ Check employee queryset status """
        print("is_employee", request.user.is_employee)
        if request.user.is_employee:
            return True
        else:
            return
