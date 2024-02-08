from rest_framework.routers import DefaultRouter
from django.urls import path

from blog_app.sub_views.blog_views import BlogViewSet

business_service_router = DefaultRouter()
business_service_router.register('blog', BlogViewSet),


urlpatterns = []
urlpatterns += business_service_router.urls
