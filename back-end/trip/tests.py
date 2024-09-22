from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import TripBooking

User = get_user_model()

class TripBookingTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.booking_url = reverse('tripbooking-list')

    def test_create_trip_booking(self):
        data = {
            'trip_name': 'Mountain Hike',
            'start_location': 'Basecamp',
            'end_location': 'Summit',
            'travel_date': '2024-09-20',
        }
        response = self.client.post(self.booking_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TripBooking.objects.count(), 1)
        self.assertEqual(TripBooking.objects.get().trip_name, 'Mountain Hike')

    def test_retrieve_trip_bookings(self):
        TripBooking.objects.create(
            user=self.user,
            trip_name='Mountain Hike',
            start_location='Basecamp',
            end_location='Summit',
            travel_date='2024-09-20'
        )
        response = self.client.get(self.booking_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
