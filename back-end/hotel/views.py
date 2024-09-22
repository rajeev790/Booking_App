from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import HotelBooking
from .serializers import HotelBookingSerializer

class HotelBookingViewSet(viewsets.ModelViewSet):
    queryset = HotelBooking.objects.all()
    serializer_class = HotelBookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
