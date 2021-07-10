from django.db import models
from users.models import User
from posts.models import Post
# Create your models here.


class Comment(models.Model):
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.comment
