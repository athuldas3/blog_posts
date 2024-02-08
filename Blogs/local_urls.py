from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# swagger imports
from drf_spectacular.views import SpectacularAPIView,\
    SpectacularRedocView, SpectacularSwaggerView

admin.site.site_header = "blog APIs"
admin.site.site_title = "blog swagger"
admin.site.index_title = ""


urlpatterns = [
    path('admin/', admin.site.urls),

    # Home - redirecting to swagger (swagger urls)
    path('', lambda request: redirect('blog-service/docs/', permanent=False)),
    path('blog-service/docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('blog-service/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('blog-service/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]