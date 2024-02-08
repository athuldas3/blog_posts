# user model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from blog_app.models.base.abstract_base_model import AbstractBase
from blog_app.models.base.custom_user_manager import CustomUserManager


class User(AbstractUser, AbstractBase):
    """ The underscore character (_) is used to represent “the previous result”
        in Python’s interactive shell and doctest tests. Installing a global _()
        function causes interference. Explicitly importing gettext() as _() avoids this problem.
    """
    email = models.EmailField(_('email'), null=False, blank=False, unique=True)
    password = models.CharField(_('password'), max_length=128, null=True, blank=True)
    user_type = models.CharField(max_length=64, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']
    objects = CustomUserManager()

    class Meta:
        db_table = "User"
        verbose_name_plural = "Users"
        ordering = ('created_date',)
