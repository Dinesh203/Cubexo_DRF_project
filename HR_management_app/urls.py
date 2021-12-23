
from django.urls import path
from HR_management_app.views import *

urlpatterns = [
    path('', CeoManage.as_view(), name='CEO Dashboard'),
    path('<int:id>', CeoManage.as_view(), name='CEO Dashboard'),
    path('HR_Managements/', HumanResources.as_view(), name='HR_Managements'),
    path('Employee_Dashboard/', EmployeeView.as_view(), name='EmployeeDashboard')
    # path('Employee_Dashboard/', EmployeeView.as_view(), name='EmployeeDashboard')

]
