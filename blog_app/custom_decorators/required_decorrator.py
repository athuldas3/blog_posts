from django.core.files.uploadedfile import InMemoryUploadedFile, \
    TemporaryUploadedFile
from functools import wraps
from rest_framework.response import Response
from rest_framework import status
import numpy as np


def required_fields(fields=[]):

    def decorator(fn):
        @wraps(fn)
        def start(request, *args, **kwargs):
            missing_params = []

            if request.data:

                data = request.data
                for field in fields:

                    if type(field) == str:
                        if field not in data:
                            missing_params.append(field)

                    if type(field) == dict:
                        for key, value in field.items():
                            check_lists = field.get(key, [])
                            test_list = data.get(key, [])
                            test_list = list(test_list.keys())
                            miss_list = list(np.setdiff1d(check_lists, test_list))
                            missing_params += miss_list

                            if not test_list:
                                missing_params += check_lists
            else:
                for field in fields:

                    if type(field) == str:
                        field_check = [field]
                        missing_params += field_check

                    if type(field) == dict:
                        for key, value in field.items():
                            check_lists = field.get(key, [])
                        missing_params += check_lists

            missing_params = list(set(missing_params))
            missing_params = list(filter(None, missing_params))

            if missing_params:
                response = {}
                for missing_field in missing_params:
                    response[f'{missing_field}'] = ["This filed is required"]

                return Response(response,
                                status=status.HTTP_400_BAD_REQUEST)

            return fn(request, *args, **kwargs)
        return start
    return decorator
