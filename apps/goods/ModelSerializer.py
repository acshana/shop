# Author:Ac.one
# -*- coding:utf-8 -*-
# @Time:2018/1/24 15:12
from rest_framework import serializers
from .models import Goods


class GoodsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields="__all__"
