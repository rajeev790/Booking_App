from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class TripBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip_name = models.CharField(max_length=255)
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    travel_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Trip: {self.trip_name} by {self.user.username}"
