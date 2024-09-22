from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import MetroBooking

User = get_user_model()

class MetroBookingTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.booking_url = reverse('metrobooking-list')

    def test_create_metro_booking(self):
        data = {
            'origin': 'Station A',
            'destination': 'Station B',
            'travel_date': '2024-09-10',
            'travel_time': '09:00:00',
        }
        response = self.client.post(self.booking_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MetroBooking.objects.count(), 1)
        self.assertEqual(MetroBooking.objects.get().origin, 'Station A')

    def test_retrieve_metro_bookings(self):
        MetroBooking.objects.create(
            user=self.user,
            origin='Station A',
            destination='Station B',
            travel_date='2024-09-10',
            travel_time='09:00:00'
        )
        response = self.client.get(self.booking_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
