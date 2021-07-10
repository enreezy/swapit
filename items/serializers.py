from datetime import datetime
from rest_framework import serializers
from .models import Item
from categories.models import Category
from users.models import User


class ItemSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field='name')
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='id')

    class Meta:
        model = Item
        fields = '__all__'
        extra_kwargs = {
            'itemname': {'required': True, 'allow_null': False}
        }
