# Create your views here.
from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CommentSerializer
from rest_framework import status
from .models import Comment
from users.models import User

# Create your views here.


class CommentView(APIView):
    def post(self, request):
        request.data["name"] = User.objects.get(id=request.data["name"])
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        comments = Comment.objects.get(id=id)
        serializer = CommentSerializer(comments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        comments = Comment.objects.get(id=id)

        comments.delete()
        return Response({'message': 'Deleted', 'status': status.HTTP_204_NO_CONTENT})
