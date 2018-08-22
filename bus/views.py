from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets, renderers, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.reverse import reverse
from .serializers import BusSerializer, CompanySerializer, AlarmSerializer
from .models import Bus, Company, Alarm
from service.format_response import api_list_response


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
        # 'users': reverse('user-list', request=request, format=format),
        # 'buses': reverse('bus-list', request=request, format=format),
        # 'company': reverse('company-list', request=request, format=format),
        # 'alarm': reverse('alarm-list', request=request, format=format)
    # })

#
# class UserSerializerViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all().order_by('-pk')
    serializer_class = BusSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('bus_id', 'company__company_name', 'bus_license_plate', 'bus_line', 'bus_locate')

    # def list(self, request, *args, **kwargs):
    #     super(viewsets.ModelViewSet.list())
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(
    #             api_list_response(status.HTTP_200_OK, '列表查询成功', data=serializer.data)
    #         )
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(
    #         api_list_response(status.HTTP_200_OK, '列表查询成功', data=serializer.data)
    #     )
    #
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def perform_create(self, serializer):
    #     serializer.save(create_user=self.request.username,create_user_id=self.request.userid)


class AlarmViewSet(viewsets.ModelViewSet):
    queryset = Alarm.objects.all()
    serializer_class = AlarmSerializer

    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def perform_create(self, serializer):
    #     serializer.save(create_user=self.request.username,create_user_id=self.request.userid)


from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from service.format_response import api_response
from rest_framework.views import APIView
from django.db.models import Q


class BusList(APIView):
    def get(self, request, format=None):
        queryset = Bus.objects.all()
        q = request.GET.get('q')
        if q is not None:
            queryset = queryset.filter(Q(bus_license_plate__icontains=q)|Q(bus_line__icontains=q)|Q(bus_locate__icontains=q))
        serializer = BusSerializer(queryset, many=True)
        return api_response(status.HTTP_200_OK, "公交车列表获取成功", serializer.data)

    def post(self, request, format=None):
        serializer = BusSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            if data.pk:
                return api_response(status.HTTP_201_CREATED, "公交车列表创建成功", serializer.root.data)
        return api_response(status.HTTP_400_BAD_REQUEST, "公交车列表创建失败", serializer.errors)
