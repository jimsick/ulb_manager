from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Alarm, Bus, Company


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Company
        # fields = ('id', 'company_id', 'company_name', 'company_server', 'company_report_list', 'create_user', 'create_user_id')
        fields = "__all__"


class BusSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    # bus_company = serializers.SerializerMethodField(many=True, view_name='company-detail', queryset=Company.objects.all())
    # company = serializers.PrimaryKeyRelatedField(source='company.company_name', read_only=True)
    company = serializers.SlugRelatedField(read_only=False, slug_field='company_name', queryset=Company.objects.all())
    # company = serializers.StringRelatedField()

    def get_company(self, obj):
        return Company.objects.get(pk=obj.pk)

    class Meta:
        model = Bus
        # fields = ('id', 'bus_id', 'company', 'bus_license_plate', 'bus_line', 'bus_state', 'bus_locate', 'create_user', 'create_user_id')
        fields = "__all__"


class AlarmSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    bus = serializers.PrimaryKeyRelatedField(queryset=Bus.objects.all(), required=True)

    class Meta:
        model = Alarm
        # fields = ('id', 'bus', 'alarm_time', 'alarm_locate', 'create_user', 'create_user_id')
        fields = "__all__"


# class UserSerializer(serializers.ModelSerializer):
#     alarms_create_user = serializers.HyperlinkedIdentityField(many=True, view_name='alarm-detail', read_only=True)
#     bus_create_user = serializers.HyperlinkedRelatedField(many=True, view_name='bus-detail', queryset=Bus.objects.all())
#     company_create_user = serializers.HyperlinkedRelatedField(many=True, view_name='company-detail', queryset=Company.objects.all())
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'alarms_create_user', 'bus_create_user', 'company_create_user') or "__all__"
