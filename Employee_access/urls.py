
from django.urls import path
from .views import *


urlpatterns = [
    path('employee_detail/', EmployeeDetail.as_view(), name='emp_get_self_detail'),
    path('employee_detail/<int:pk>', EmployeeDetail.as_view(), name='emp_get_self_detail'),
    path('employee_project/', EmployeeProject.as_view(), name='emp_get_project_detail'),
    path('employee_project/<int:pk>', EmployeeProject.as_view(), name='emp_Retrieve_project')

]
