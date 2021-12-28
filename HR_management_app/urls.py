
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'Hr_emp_views/', HrAllEmployeeView)

urlpatterns = [
    path('', CeoManage.as_view(), name='CEO Dashboard'),
    path('<int:id>', CeoManage.as_view(), name='CEO Dashboard'),
    path('Ceo_project/', CeoProjects.as_view(), name='CeoProjects'),
    path('ceo_update_project/<int:pk>', CeoUpdateProject.as_view(), name='Ceo_Update_Projects'),
    # path('change_status/<int:pk>', projectStatus.as_view(), name='Change_project_status'),

    path("Hr_emp_viewsets/", include(router.urls), name='Employee_View'),
    path('hr_update_employee/<int:pk>', HrUpdateEmployee.as_view(), name='Update_Employees_details'),
    path("Hr_project_get/", HrProjectView.as_view(), name='Hr_project_get'),
    path("Hr_project_retrieve/<int:pk>", HrProjectView.as_view(), name='Hr_project_retrieve'),

    path('employee_detail/', EmployeeDetail.as_view(), name='employee_self_detail'),
    path('employee_project/', EmployeeProject.as_view(), name='employee_project')


]
