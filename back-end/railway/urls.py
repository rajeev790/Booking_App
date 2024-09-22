from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RailwayBookingViewSet

router = DefaultRouter()
router.register(r'bookings', RailwayBookingViewSet, basename='railwaybooking')

urlpatterns = [
    path('', include(router.urls)),
]
