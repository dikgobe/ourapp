from django.db import models
from users.models import CustomUser

class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)  # e.g., pending, completed, failed

    def __str__(self):
        return f"{self.user}"
