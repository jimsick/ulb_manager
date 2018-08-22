from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qq = models.IntegerField()
    mobile = models.IntegerField()

    def __str__(self):
        return "%s" % self.user.username