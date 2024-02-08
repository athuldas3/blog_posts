import uuid
from django.db import models


class AbstractBase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # auto_now_add will set the timezone. now() when the instance is created
    created_date = models.DateTimeField(auto_now_add=True)
    # auto_now will update the field everytime the save method is called
    updated_date = models.DateTimeField(auto_now=True)
    deleted_date = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)  # for soft delete
    is_active = models.BooleanField(default=True)    # for block

    class Meta:
        abstract = True

