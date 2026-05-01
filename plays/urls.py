from django.urls import path
from plays.views import ShowDetailView

app_name = 'plays'

urlpatterns = [
    path('show/<int:pk>/', ShowDetailView.as_view(), name='show_detail'),
]