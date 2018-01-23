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

from goods.models import GoodsCategory#必须在django初始化之后才能引入
from db_tools.data.category_data import row_data

for lev1_cat in row_data:
    lev1_obj=GoodsCategory()
    lev1_obj.code=lev1_cat["code"]
    lev1_obj.name=lev1_cat["name"]
    lev1_obj.category_type=1
    lev1_obj.save()

    for lev2_cat in lev1_cat["sub_categorys"]:
        lev2_obj = GoodsCategory()
        lev2_obj.code = lev2_cat["code"]
        lev2_obj.name = lev2_cat["name"]
        lev2_obj.category_type = 2
        lev2_obj.parent_category=lev1_obj
        lev2_obj.save()

        for lev3_cat in lev2_cat["sub_categorys"]:
            lev3_obj = GoodsCategory()
            lev3_obj.code = lev3_cat["code"]
            lev3_obj.name = lev3_cat["name"]
            lev3_obj.category_type = 3
            lev3_obj.parent_category = lev2_obj
            lev3_obj.save()