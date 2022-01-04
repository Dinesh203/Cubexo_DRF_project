
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'Hr_emp_views/', HrAllEmployeeView)

urlpatterns = [
    path("Hr_emp_viewsets/", include(router.urls), name='Employee_View'),
    path('hr_update_employee/<int:pk>', HrUpdateEmployee.as_view(), name='Update_Employees_details'),
    path("Hr_project_get/", HrProjectView.as_view(), name='Hr_project_get'),
    path("Hr_project_get/<int:pk>", HrProjectView.as_view(), name='Hr_project_retrieve'),


]
