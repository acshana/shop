from rest_framework import mixins
from rest_framework import generics
from .models import Goods
from .ModelSerializer import GoodsModelSerializer


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
    queryset = Goods.objects.all()[:10]
    serializer_class = GoodsModelSerializer
