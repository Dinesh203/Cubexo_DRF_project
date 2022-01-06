
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', CeoManage.as_view(), name='CEO Dashboard'),
    path('<int:pk>', CeoManage.as_view(), name='CEO Dashboard'),
    path('Ceo_project/', CeoProjects.as_view(), name='CeoProjects'),
    path('Ceo_project/<int:pk>', CeoProjects.as_view(), name='Ceo_Get_Projects'),
    path('Change_password/<int:pk>', ChangePasswordView.as_view(), name='change_password'),
    path('ceo_update_project/', CeoUpdateProject.as_view(), name='Ceo_Update_Projects'),
    path('ceo_update_project/<int:pk>', CeoUpdateProject.as_view(), name='Ceo_Update_Projects'),
    path('development_staus/', DevelopmentStatus.as_view(), name='development_status'),
    path('development_staus/<int:pk>', DevelopmentStatus.as_view(), name='development_status'),
    path('add_development_status/', AddDevelopmentStatus.as_view(), name='get_ret_development_status'),
    path('add_development_status/<int:pk>', AddDevelopmentStatus.as_view(), name='add_development_status'),
    path('change_project_status/<int:pk>', ChangeProjectStatus.as_view(), name='change_project_status'),
    # path('employee_status/', EmployeesStatus.as_view(), name='employee_status'),


]
