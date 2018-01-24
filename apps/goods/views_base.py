# Author:Ac.one
# -*- coding:utf-8 -*-
# @Time:2018/1/23 21:35
from goods.models import Goods
from django.views.generic.base import View
from django.forms.models import model_to_dict
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
import json


class GoodsListView(View):
    def get(self, request):
        '''
        通过View实现商品列表页
        :param request:
        :return:
        '''
        json_list = []
        goods = Goods.objects.all()[:10]
        # way1
        # for good in goods:
        #     json_dict = {}
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
        #     json_list.append(json_dict)
        # return HttpResponse(json.dumps(json_list), content_type="application/json")

        # way2
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)
        # return HttpResponse(json.dumps(json_list), content_type="application/json")

        # way3
        json_data = serialize("json", goods)
        # return HttpResponse(json_data, content_type="application/json")
        json_data=json.loads(json_data)
        print(json_data)
        print(type(json_data))
        return JsonResponse(json_data,safe=False)