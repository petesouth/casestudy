from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics, status, renderers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.views import exception_handler

from datetime import datetime, timedelta
from casedomain.serializers import (ChangePasswordSerializer)

from casedomain.getwords import numberToWord, makeNumberPretty

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    return response

class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class NumberConverterView(APIView):
    permission_classes = [AllowAny, ]
    renderer_classes = [renderers.JSONRenderer]

    def post(self, request, format=None):
        dataNumber = request.data.get("number")
        content = {'converted': numberToWord(dataNumber),
                   'original': makeNumberPretty(dataNumber) }
        return Response(content)

    def get(self, request):
        dataNumber = int(request.query_params.get('number'))
        content = {'converted': numberToWord(dataNumber),
                   'original': makeNumberPretty(dataNumber) }
        return Response(content)
