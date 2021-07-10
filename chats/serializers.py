from rest_framework import serializers
from .models import Chat
from users.models import User


class ChatSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='id')
    receiver = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='id')

    class Meta:
        model = Chat
        fields = '__all__'
