from __future__ import unicode_literals, absolute_import
import pickle

from django.db import models
from django.contrib.auth.models import User


class MyModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='mymodels', on_delete=models.CASCADE)
    field = models.CharField(max_length=100)
    options = models.CharField(max_length=100)