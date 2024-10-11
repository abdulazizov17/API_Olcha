from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from olcha.models import Category
from olcha.serializers import CategorySerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from django.core.cache import cache
from rest_framework.generics import ListAPIView

from olcha.models import Category, Group
from olcha.serializers import CategorySerializer, GroupSerializer

class CategoryDetailApiView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, category_slug):
        try:
            category = Category.objects.get(slug=category_slug)
            serializer = CategorySerializer(category, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

class CategoryListApiView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        cache_key = 'category-list'
        cached_data = cache.get(cache_key)
        if not cached_data:
            queryset = Category.objects.all()
            cache.set(cache_key, queryset, timeout=60 * 3)
            return queryset
        return cached_data


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'

    def get_object(self):
        cache_key = f'category-detail-{self.kwargs["pk"]}'
        cached_data = cache.get(cache_key)
        if not cached_data:
            obj = super().get_object()
            cache.set(cache_key, obj, timeout=60 * 3)  # 3 daqiqa cache
            return obj
        return cached_data