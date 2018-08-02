from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',TemplateView.as_view(template_name="index.html")),
    re_path(r'^api/', include('backend.urls')),
    re_path(r'^docs/', get_schema_view())
]
