from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import RailwayBooking

User = get_user_model()

class RailwayBookingTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.booking_url = reverse('railwaybooking-list')

    def test_create_railway_booking(self):
        data = {
            'train_name': 'Express Train',
            'origin': 'Station A',
            'destination': 'Station B',
            'travel_date': '2024-09-10',
            'seat_class': 'AC',
        }
        response = self.client.post(self.booking_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RailwayBooking.objects.count(), 1)
        self.assertEqual(RailwayBooking.objects.get().train_name, 'Express Train')

    def test_retrieve_railway_bookings(self):
        RailwayBooking.objects.create(
            user=self.user,
            train_name='Express Train',
            origin='Station A',
            destination='Station B',
            travel_date='2024-09-10',
            seat_class='AC'
        )
        response = self.client.get(self.booking_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
