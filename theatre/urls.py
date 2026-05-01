"""theatre URL Configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("homepage.urls")),         # Главная страница
    path('users/', include('users.urls')),      # ✅ Добавлено: маршруты входа/выхода/регистрации
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]