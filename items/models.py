from django.db import models
from users.models import User
from categories.models import Category


class Item(models.Model):
    itemname = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(blank=True)
    image = models.FileField(upload_to='images', blank='true')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.itemname
