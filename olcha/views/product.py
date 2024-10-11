from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from olcha.models import Product, Image
from olcha.serializers import ProductSerializer, ImageSerializer


class ProductListApiView(ListCreateAPIView):
    permission_classes = [AllowAny,]
    # authentication_classes = [JWTAuthentication, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ImageListApiView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

from django.core.cache import cache
from rest_framework.generics import ListAPIView
from olcha.models import Product
from olcha.serializers import ProductSerializer

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        cache_key = 'product-list'
        cached_data = cache.get(cache_key)
        if not cached_data:
            queryset = Product.objects.all().select_related('category')
            cache.set(cache_key, queryset, timeout=60 * 3) 
            return queryset
        return cached_data
