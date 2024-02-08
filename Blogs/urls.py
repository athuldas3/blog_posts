from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('blog-service/api/',
         include(('blog_app.urls', 'blog_app_api'), namespace='blog_app+api')),

    # Auth API
    path('token/', TokenObtainPairView.as_view(), name="token_obtain"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
]


try:
    from Blogs.local_urls import urlpatterns as lurls
    urlpatterns += lurls
except Exception as ex:
    print(ex)
    print('Not added local urls')
