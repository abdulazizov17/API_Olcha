from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from olcha.models import Category, Group, Product
from olcha.serializers import CategorySerializer,GroupSerializer,ProductSerializer
from rest_framework import generics, mixins


# Create your views here.


class CategoryListApiView(APIView):

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


class GroupListApiView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CategoryDetailApiView(APIView):
    def get(self, request, category_slug):
        category = Category.objects.get(slug=category_slug)
        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDetail(GenericAPIView):


    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductAPIView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

