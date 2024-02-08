# imports
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# development environment
DEBUG = True
ALLOWED_HOSTS = ['*']
# time zone
TIME_ZONE = "UTC"
USE_TZ = True
# language
LANGUAGE_CODE = "en-us"
USE_I18N = True

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # apps
    'blog_app',
    # imports
    'rest_framework',
    'django_filters',
    'django_injector',
    # swagger
    'drf_spectacular'

]

# swagger settings
SPECTACULAR_SETTINGS = {
    'TITLE': 'Blog API',
    'DESCRIPTION': 'Blog Application',
    'VERSION': '1.0.0',
    # OTHER SETTINGS
    # 'SERVE_PERMISSIONS': ['rest_framework.permissions.IsAuthenticated'],
}

# database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
