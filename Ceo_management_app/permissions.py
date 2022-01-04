from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission
from rest_framework.response import Response


class IsCompanyManager(BasePermission):
    """ CEO permissions """

    def has_permission(self, request, view):
        """ Check permissions """
        print("request", request.user.role)
        if request.user.role == 'CEO' or request.user.role == 'HR':
            return True
        else:
            return False


# class CheckEmployeeStatus(BasePermission):
#     """ check current employee status is active or deactivate"""
#
#     def has_permission(self, request, view):
#         """ Check permissions """
#         print("request", request.user)
#         if request.user.role == 'CEO' or request.user.role == 'HR':
#             return True
#         else:
#             return False

    # def has_object_permission(self, request, view, obj):
    #     """ object level permissions """
    #     print("object_permissions")
    #     print("obj", obj)
    #     print("check role", request.user.is_staff)
    #     if request.user.is_staff:
    #         return True
    #
    #     return obj == request.user
