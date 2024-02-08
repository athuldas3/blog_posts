from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from blog_app.models import Blog


def check_blog_owner(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Retrieve the blog object based on the PK
        try:
            blog = Blog.objects.filter(id=kwargs.get('pk')).first()
        except Blog.DoesNotExist:
            return Response({"detail": "Blog not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the current user is the owner of the blog
        if request.user != blog.author:
            return Response({"detail": "You do not have permission to perform this action."},
                            status=status.HTTP_403_FORBIDDEN)

        # Call the original view function
        return view_func(request, *args, **kwargs)

    return wrapper
