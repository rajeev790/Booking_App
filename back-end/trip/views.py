from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import TripBooking
from .serializers import TripBookingSerializer

class TripBookingViewSet(viewsets.ModelViewSet):
    queryset = TripBooking.objects.all()
    serializer_class = TripBookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
