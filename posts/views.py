# Create your views here.
from django.contrib.auth.models import AnonymousUser
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework import status
from .models import Post

# Create your views here.


class PostView(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        posts = Post.objects.get(id=id)
        serializer = PostSerializer(posts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        posts = Post.objects.get(id=id)

        posts.delete()
        return Response({'message': 'Deleted', 'status': status.HTTP_204_NO_CONTENT})
