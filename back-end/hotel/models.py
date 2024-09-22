from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class HotelBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.hotel_name} booking by {self.user.username}"
