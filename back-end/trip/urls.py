from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripBookingViewSet

router = DefaultRouter()
router.register(r'bookings', TripBookingViewSet, basename='tripbooking')

urlpatterns = [
    path('', include(router.urls)),
]
