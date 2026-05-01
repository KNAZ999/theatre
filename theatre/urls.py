from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('homepage.urls')),   # → /
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('plays/', include('plays.urls')), # → /plays/show/1/

    path('admin/', admin.site.urls),
]