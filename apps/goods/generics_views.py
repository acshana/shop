from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Goods
from .ModelSerializer import GoodsModelSerializer

# 分页
class GoodsPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 10


# way1
# class GoodsListView(mixins.ListModelMixin,generics.GenericAPIView):
#     """
#     通过View实现商品列表页
#     """
#     queryset = Goods.objects.all()[:10]
#     serializer_class = GoodsModelSerializer
#
#     def get(self, request, *args,**kwargs):
#         return self.list(request,*args,**kwargs)

# way2
class GoodsListView(generics.ListAPIView):
    """
    通过View实现商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsModelSerializer
    pagination_class=GoodsPagination


