from __future__ import unicode_literals, absolute_import

from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, filters, permissions, viewsets, renderers
from rest_framework.decorators import (
    permission_classes, action
)
from rest_framework.response import Response

from .serializers import MySerializer, UserSerializer
from .models import MyModel


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer = UserSerializer
    # filter_backends = (DjangoFilterBackend,)


class ModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # filter_backends = (DjangoFilterBackend,)

    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('field', 'options')

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def plaintext(self, request, *args, **kwargs):
        model = self.get_object()
        return Response(repr(model))
