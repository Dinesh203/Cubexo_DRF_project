"""CubexO_managements URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('HR_management_app.urls')),
    path("token/", jwt_views.TokenObtainPairView.as_view()),
    path("token_refresh/", jwt_views.TokenRefreshView.as_view()),
]
