from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ItemSerializer
from categories.serializers import CategorySerializer
from users.serializers import UserSerializer
from rest_framework import status
from .models import Item
from users.models import User
from categories.models import Category

# Create your views here.


class ItemView(APIView):
    def post(self, request):
        request.data["user"] = User.objects.get(id=request.data["user"]).id
        request.data["category"] = Category.objects.get(
            id=request.data["category"]).id

        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        items = Item.objects.get(id=id)
        serializer = ItemSerializer(items, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        items = Item.objects.get(id=id)
        items.delete()
        return Response({'message': 'Deleted', 'status': status.HTTP_204_NO_CONTENT})
