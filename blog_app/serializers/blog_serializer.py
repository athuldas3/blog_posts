from rest_framework import serializers
from blog_app.models import Blog, Comment
from datetime import datetime


class CreateBlogSerializer(serializers.ModelSerializer):

    created_date = serializers.DateTimeField(default=datetime.now)

    class Meta:
        model = Blog
        exclude = ('is_deleted', 'deleted_date', 'is_active')


class UpdateBlogSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=150, required=True)
    content = serializers.CharField(required=True)

    class Meta:
        model = Blog
        exclude = ('is_deleted', 'deleted_date', 'is_active', 'author')


class CreateBlogCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        exclude = ('is_deleted', 'deleted_date', 'is_active')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment']


class ListBlogCommentsSerializer(serializers.ModelSerializer):

    blog_comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        exclude = ('is_deleted', 'deleted_date', 'is_active')
