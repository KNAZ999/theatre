from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('actors/', views.ActorListView.as_view(), name='actor-list'),
    path('shows/', views.ShowListView.as_view(), name='show-list'),
    path('bookings/', views.BookingListCreateView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', views.BookingRetrieveUpdateDestroyView.as_view(), name='booking-detail'),
]