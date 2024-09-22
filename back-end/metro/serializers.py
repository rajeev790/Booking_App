from rest_framework import serializers
from .models import MetroBooking

class MetroBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetroBooking
        fields = ['id', 'user', 'origin', 'destination', 'travel_date', 'travel_time', 'created_at']
