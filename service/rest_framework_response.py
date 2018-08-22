from rest_framework.views import exception_handler
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from service.format_response import api_list_response


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['code'] = response.status_code

    return response

