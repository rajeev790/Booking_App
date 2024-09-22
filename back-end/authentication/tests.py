from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthenticationTests(APITestCase):
    def test_signup(self):
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword123"
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        user = User.objects.create_user(username="testuser", password="testpassword123")
        data = {
            "username": "testuser",
            "password": "testpassword123"
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
