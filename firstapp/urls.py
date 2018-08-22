from __future__ import unicode_literals, absolute_import

from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from . import views


# as_view 方法生成 view
# 可以非常方便的指定 `{Http Method: View Method}`
user_detail = views.UserViewSet.as_view({'get': 'retrieve'})
user_list = views.UserViewSet.as_view({'get': 'list', 'post': 'create'})

modal_plain = views.ModelViewSet.as_view({'get': 'plaintext'})
model_detail = views.ModelViewSet.as_view({'get': 'retrieve', 'post': 'create'})
model_list = views.ModelViewSet.as_view({'get': 'list', 'post': 'create'})

# router 的作用就是自动生成 Api Root 页面
router = DefaultRouter()
router.register(r'models', views.ModelViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls')),  # Api Root
    re_path(r'^models/$', model_list, name='model-list'),
    re_path(r'^models/(?P<pk>[0-9]+)/$', model_detail, name='model-detail'),
    re_path(r'^models/(?P<pk>[0-9]+)/plain/$', modal_plain, name='modal-plain'),
    re_path(r'^users/$', user_list, name='user-list'),
    re_path(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
]
