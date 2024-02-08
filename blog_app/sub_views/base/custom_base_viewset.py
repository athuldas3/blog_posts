from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class CustomBaseViewSet(viewsets.GenericViewSet):
    """ Custom Permission class determines permission for each viewset action """
    permission_classes_by_action = {"default": [AllowAny]}
    serializers = {}

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action.get(
                self.action, self.permission_classes_by_action['default'])]

        except:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        try:
            return self.serializers.get(self.action, self.serializers['default'])
        except:
            return self.serializer_class
