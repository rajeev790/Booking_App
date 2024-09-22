from rest_framework import serializers
from .models import RailwayBooking

class RailwayBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RailwayBooking
        fields = ['id', 'user', 'train_name', 'origin', 'destination', 'travel_date', 'seat_class', 'created_at']
