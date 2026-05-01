from django.urls import path
from .views import ShowDetailView, create_show

app_name = 'plays'

urlpatterns = [
    path('show/<int:pk>/', ShowDetailView.as_view(), name='show_detail'),
    path('create/', create_show, name='create_show'),
]