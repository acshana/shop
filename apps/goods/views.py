from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Goods
from .serializer import GoodsSerializer
from .ModelSerializer import GoodsModelSerializer


# Create your views here.
class GoodsListView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsModelSerializer(goods, many=True)
        return Response(goods_serializer.data)

    def post(self, request):
        serializer = GoodsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
