from rest_framework import mixins, status
from blog_app.custom_decorators.blog_owner_check import check_blog_owner
from blog_app.custom_decorators.required_decorrator import required_fields
from blog_app.serializers.blog_serializer import CreateBlogSerializer, UpdateBlogSerializer, \
    CreateBlogCommentSerializer, ListBlogCommentsSerializer
from blog_app.services.blog_services import BlogServices
from blog_app.sub_views.base.custom_base_viewset import CustomBaseViewSet
from blog_app.models.blog_model import Blog
from rest_framework.permissions import IsAuthenticated
from injector import inject
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.decorators import action


# Implement views  to: Allow users to create, edit, and delete blog posts.
class BlogViewSet(mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  CustomBaseViewSet):
    """
        Creates, Updates, Retrieves and List - Product
    """

    queryset = Blog.objects.filter(is_deleted=False).all()

    serializers = {
        'default': CreateBlogSerializer,
        'list': ListBlogCommentsSerializer,
        'update': UpdateBlogSerializer,
        'create_blog_comment': CreateBlogCommentSerializer,
    }
    permission_classes_by_action = {
        'default': [IsAuthenticated],
    }

    service = None

    @inject
    def setup(self, request, service: BlogServices, **kwargs):
        self.service = service
        super().__init__()

    @method_decorator(required_fields(['title', 'content', 'author']))
    def create(self, request, *args, **kwargs):
        """
            Create Blog
        """
        response = self.service.custom_create(request.data)
        return Response(response, status=status.HTTP_201_CREATED)

    @method_decorator(check_blog_owner)
    @method_decorator(required_fields([]))
    def update(self, request, *args, **kwargs):
        """
            Update Blog
        """
        product_id = kwargs.get('pk')
        response = self.service.custom_update(request.data, product_id)
        return Response(response, status=status.HTTP_200_OK)

    # Allow users to comment on blog posts.
    @action(detail=False, methods=['post'], url_path='create/comments', url_name='category')
    def create_blog_comment(self, request):
        """
            Create Comments on Blog
        """
        response = self.service.create_blog_comment(request.data)
        return Response(response, status=status.HTTP_200_OK)
