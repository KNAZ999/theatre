from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions

from api.serializers import ActorSerializer, ShowSerializer, BookingSerializer
from api.permissions import IsOwner
from plays.models import Actor, Show, Booking


class ActorListView(generics.ListAPIView):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()


class ShowListView(generics.ListAPIView):
    serializer_class = ShowSerializer
    queryset = Show.objects.all()


class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def filter_queryset(self, queryset):
        return queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Booking.objects.filter(owner=self.request.user)