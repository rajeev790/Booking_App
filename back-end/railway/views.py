from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import RailwayBooking
from .serializers import RailwayBookingSerializer

class RailwayBookingViewSet(viewsets.ModelViewSet):
    queryset = RailwayBooking.objects.all()
    serializer_class = RailwayBookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
