# Create your views here.
from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChatSerializer
from rest_framework import status
from .models import Chat

# Create your views here.


class ChatView(APIView):
    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        chats = Chat.objects.all()
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        chats = Chat.objects.get(id=id)
        serializer = ChatSerializer(chats, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        chats = Chat.objects.get(id=id)

        chats.delete()
        return Response({'Chat': 'Deleted', 'status': status.HTTP_204_NO_CONTENT})
