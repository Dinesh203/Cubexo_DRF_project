"""CubexO_managements URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("Hr/", include('HR_management_app.urls')),
    path("", include('Ceo_management_app.urls')),
    path("Employee/", include('Employee_access.urls')),
    path("token/", jwt_views.TokenObtainPairView.as_view()),
    path("token_refresh/", jwt_views.TokenRefreshView.as_view()),

]
