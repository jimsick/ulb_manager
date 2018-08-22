from __future__ import unicode_literals, absolute_import
import json

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import MyModel


class MyCustField(serializers.CharField):
    def to_representation(self, value):
        """将从 Model 取出的数据 parse 给 Api"""
        return value

    def to_internal_value(self, data):
        """将客户端传来的 json 数据 parse 给 Model"""
        return json.loads(data.encode('utf-8'))


class UserSerializer(serializers.ModelSerializer):
    mymodels = serializers.HyperlinkedRelatedField(many=True, view_name='model-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'mymodels')  #制定返回的fields

    # 这句话的作用是为 MyModel 中的外键建立超链接，依赖于 urls 中的 name 参数


class MySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = MyModel 
        fields = ('id', 'owner', 'field', 'options')
        read_only_fields = ('owner',)  # 指定只读的field

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return MyModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """响应put请求"""
        instance.field = validated_data.get('field', instance.field)
        instance.save()
        return instance
