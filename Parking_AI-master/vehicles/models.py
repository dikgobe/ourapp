from django.db import models
from users.models import CustomUser

class Vehicle(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    license_plate = models.CharField(max_length=20)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner}"