from django.urls import path, re_path, include
from .views import BusViewSet, CompanyViewSet, AlarmViewSet, BusList

from rest_framework.routers import DefaultRouter


# user_list = UserSerializerViewSet.as_view({'get': 'retrieve'})

bus_list = BusViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
bus_detail = BusViewSet.as_view({
    'get': 'list',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

company_list = CompanyViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
company_detail = CompanyViewSet.as_view({
    'get': 'list',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

alarm_list = AlarmViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
alarm_detail = AlarmViewSet.as_view({
    'get': 'list',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

router = DefaultRouter()
# router.register(r'user', UserSerializerViewSet)
router.register(r'bus', BusViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'alarm', AlarmViewSet)

urlpatterns = [
    re_path('^', include(router.urls)),
    # re_path('^$', api_root),
    # re_path('^user/$', user_list, name='user-list'),
    # re_path('^buses/$', BusList.as_view(), name='bus-list'),
    re_path('^bus/$', bus_list, name='bus-list1'),
    re_path('^bus/(?P<pk>[0-9]+)/$', bus_detail, name='bus-detail'),
    re_path('^company/$', company_detail, name='company-list'),
    re_path('^company/(?P<pk>[0-9]+)/$', company_detail, name='company-detail'),
    re_path('^alarm/$', alarm_list, name='alarm-detail'),
    re_path('^alarm/(?P<pk>[0-9]+)/$', alarm_detail, name='alarm-detail'),
]