# Author:Ac.one
# -*- coding:utf-8 -*-
# @Time:2018/1/24 15:12
from rest_framework import serializers
from .models import Goods

class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)
    click_num = serializers.IntegerField(default=0)
    goods_front_image=serializers.ImageField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Goods.objects.create(**validated_data)
