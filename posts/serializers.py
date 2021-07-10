from rest_framework import serializers
from .models import Post
from users.models import User
from items.models import Item


class PostSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='name')

    item = serializers.SlugRelatedField(
        queryset=Item.objects.all(), slug_field='id')

    class Meta:
        model = Post
        fields = '__all__'
