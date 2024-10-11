from django.core.cache import cache
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListCreateAPIView, ListAPIView
from olcha.models import Group
from olcha.serializers import GroupSerializer
from rest_framework.generics import RetrieveAPIView


class GroupListApiView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class GroupListView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        cache_key = 'group-list'
        cached_data = cache.get(cache_key)
        if not cached_data:
            queryset = Group.objects.all().select_related('category')
            cache.set(cache_key, queryset, timeout=60 * 3)
            return queryset
        return cached_data


class GroupDetailView(RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'

    def get_object(self):
        cache_key = f'group-detail-{self.kwargs["pk"]}'
        cached_data = cache.get(cache_key)
        if not cached_data:
            obj = super().get_object()
            cache.set(cache_key, obj, timeout=60 * 3)
            return obj
        return cached_data