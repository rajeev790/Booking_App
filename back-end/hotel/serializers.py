from rest_framework import serializers
from .models import HotelBooking

class HotelBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelBooking
        fields = ['id', 'user', 'hotel_name', 'location', 'check_in_date', 'check_out_date', 'created_at']
