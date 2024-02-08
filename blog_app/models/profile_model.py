# profile
from blog_app.models.base.abstract_base_model import AbstractBase
from django.db import models

from blog_app.models.user_model import User


# User Profiles with additional information (e.g., profile picture, bio).
class UserProfile(AbstractBase):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="profile_user")
    file = models.FileField(upload_to='profile/uploads/')
    name = models.CharField(max_length=150, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "user_profile"
        verbose_name_plural = "user_profiles"
        ordering = ('created_date', )
