
from django.urls import path, include
from .views import CeoManage, CeoProjects, HrAllEmployeeView, EmployeeDetail,\
    EmployeeView, EmployeeProject, CeoUpdateProject
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'Hr_emp_viewsets', HrAllEmployeeView)

urlpatterns = [
    path('', CeoManage.as_view(), name='CEO Dashboard'),
    path('<int:id>', CeoManage.as_view(), name='CEO Dashboard'),
    path('Ceo_project/', CeoProjects.as_view(), name='CeoProjects'),
    path('ceo_update_project/<int:pk>', CeoUpdateProject.as_view(), name='Ceo_Update_Projects'),

    path("Hr_emp_viewsets/", include(router.urls), name='Employee_View'),

    path('employee_detail/', EmployeeDetail.as_view(), name='employee_self_detail'),
    path('employee_view/', EmployeeView.as_view(), name='employee_detail'),
    path('employee_project/', EmployeeProject.as_view(), name='employee_project')


]
