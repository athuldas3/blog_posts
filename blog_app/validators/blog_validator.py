from blog_app.models import Blog
from blog_app.serializers.blog_serializer import CreateBlogSerializer, UpdateBlogSerializer, CreateBlogCommentSerializer
from blog_app.utilities.exceptions import NotFound


class BlogValidator:

    @staticmethod
    def custom_create(data: dict) -> dict:
        serializer = CreateBlogSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return {"serializer": serializer}

    @staticmethod
    def custom_update(data: dict, blog_id) -> dict:
        blog = Blog.objects.filter(id=blog_id).first()
        if not blog:
            raise NotFound
        serializer = UpdateBlogSerializer(data=data, instance=blog)
        serializer.is_valid(raise_exception=True)
        return {"serializer": serializer}

    @staticmethod
    def create_blog_comments(data: dict) -> dict:
        serializer = CreateBlogCommentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return {"serializer": serializer}
