from django.urls import path, re_path, include
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    # re_path(),
    re_path(r'^auth/', obtain_jwt_token),
]