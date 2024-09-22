from rest_framework import serializers
from .models import TripBooking

class TripBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripBooking
        fields = ['id', 'user', 'trip_name', 'start_location', 'end_location', 'travel_date', 'created_at']
