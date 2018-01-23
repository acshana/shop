#Author:Ac.one
# -*- coding:utf-8 -*-
#@Time:2018/1/23 17:11

import sys
import os
import django

pwd=os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")

#django初始化
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Shop.settings")
django.setup()

from goods.models import Goods,GoodsCategory,GoodsImage#必须在django初始化之后才能引入
from db_tools.data.product_data import row_data

for goods_detail in row_data:
    goods=Goods()
    goods.name=goods_detail["name"]
    goods.market_price=float(int(goods_detail["market_price"].replace("￥","").replace("元","")))
    goods.shop_price=float(int(goods_detail["sale_price"].replace("￥","").replace("元","")))
    goods.goods_brief=goods_detail['desc'] if goods_detail['desc'] is not None else ""
    goods.desc=goods_detail['goods_desc'] if goods_detail['goods_desc'] is not None else ""
    goods.goods_front_image=goods_detail['images'][0] if goods_detail['images'] else ""
    category_name=goods_detail['categorys'][-1]
    category=GoodsCategory.objects.filter(name=category_name)
    if category:
        goods.category=category[0]
    goods.save()

    for goods_image in goods_detail['images']:
        goods_image_obj=GoodsImage()
        goods_image_obj.goods=goods
        goods_image_obj.image=goods_image
        goods_image_obj.save()