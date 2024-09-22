from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class RailwayBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    train_name = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    travel_date = models.DateField()
    seat_class = models.CharField(max_length=50, choices=[('AC', 'AC'), ('Sleeper', 'Sleeper'), ('General', 'General')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.train_name} booking by {self.user.username}"
