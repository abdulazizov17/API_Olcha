from rest_framework import viewsets
from olcha.models import AttributeKey, AttributeValue, ProductAttribute
from olcha.serializers import AttributeKeySerializer, AttributeValueSerializer, ProductAttributeSerializer

class AttributeKeyViewSet(viewsets.ModelViewSet):
    queryset = AttributeKey.objects.all()
    serializer_class = AttributeKeySerializer

class AttributeValueViewSet(viewsets.ModelViewSet):
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerializer

class ProductAttributeViewSet(viewsets.ModelViewSet):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer
