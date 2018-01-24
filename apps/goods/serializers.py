# Author:Ac.one
# -*- coding:utf-8 -*-
# @Time:2018/1/24 15:12
from rest_framework import serializers


class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)
    click_num = serializers.IntegerField(default=0)
    goods_front_image=serializers.ImageField()
