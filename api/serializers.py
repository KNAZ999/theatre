from rest_framework import serializers
from plays.models import Actor, Show, Booking


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'