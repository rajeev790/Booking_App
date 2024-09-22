from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import MetroBooking
from .serializers import MetroBookingSerializer

class MetroBookingViewSet(viewsets.ModelViewSet):
    queryset = MetroBooking.objects.all()
    serializer_class = MetroBookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
