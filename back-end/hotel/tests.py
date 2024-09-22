from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import HotelBooking

User = get_user_model()

class HotelBookingTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.booking_url = reverse('hotelbooking-list')

    def test_create_hotel_booking(self):
        data = {
            'hotel_name': 'Grand Hotel',
            'location': 'New York',
            'check_in_date': '2024-09-10',
            'check_out_date': '2024-09-15',
        }
        response = self.client.post(self.booking_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(HotelBooking.objects.count(), 1)
        self.assertEqual(HotelBooking.objects.get().hotel_name, 'Grand Hotel')

    def test_retrieve_hotel_bookings(self):
        HotelBooking.objects.create(
            user=self.user,
            hotel_name='Grand Hotel',
            location='New York',
            check_in_date='2024-09-10',
            check_out_date='2024-09-15'
        )
        response = self.client.get(self.booking_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
