from django.db import models
from users.models import User
from items.models import Item
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, blank=True, null=True)
    like = models.IntegerField()
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
