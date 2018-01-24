"""Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from Shop.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from goods.views_base import GoodsListView as good1
from goods.views import GoodsListView as good2
from goods.generics_views import GoodsListView as good3

# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),  # 使图片正确显示
    url(r'^api-auth/', include('rest_framework.urls')),

    # 商品列表
    url(r'^goods1/$', good1.as_view(), name="goods-list1"),
    url(r'^goods2/$', good2.as_view(), name="goods-list2"),
    url(r'^goods3/$', good3.as_view(), name="goods-list3"),

    url(r'^docs/', include_docs_urls(title='shop文档')),
]
