from rest_framework import serializers
from .models import Comment
from users.models import User
from posts.models import Post
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    name = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='id')
    post = serializers.SlugRelatedField(
        queryset=Post.objects.all(), slug_field='id')
    comment = serializers.SlugRelatedField(
        queryset=Comment.objects.all(), slug_field='id')

    class Meta:
        model = Comment
        fields = '__all__'
