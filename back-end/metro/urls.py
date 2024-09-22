from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MetroBookingViewSet

router = DefaultRouter()
router.register(r'bookings', MetroBookingViewSet, basename='metrobooking')

urlpatterns = [
    path('', include(router.urls)),
]
