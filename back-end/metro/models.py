from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class MetroBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    travel_date = models.DateField()
    travel_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.origin} to {self.destination} booking by {self.user.username}"
