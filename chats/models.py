from django.db import models
from users.models import User
# Create your models here.


class Chat(models.Model):
    message = models.CharField(max_length=255, blank=True)
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.message
