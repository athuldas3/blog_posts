from rest_framework.exceptions import APIException
from rest_framework import status
from django.utils.translation import gettext_lazy as _


class NotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _('The selected id not found.')
    default_code = 'id'

    def __init__(self, detail=None):
        if detail is not None:
            self.detail = {'id': detail}
        else:
            self.detail = {'id': self.default_detail}
