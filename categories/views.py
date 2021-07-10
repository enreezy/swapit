from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer
from rest_framework import status
from .models import Category

# Create your views here.


class CategoryView(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        categories = Category.objects.get(id=id)
        serializer = CategorySerializer(categories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        categories = Category.objects.get(id=id)

        categories.delete()
        return Response({'message': 'Deleted', 'status': status.HTTP_204_NO_CONTENT})
