
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAdminUser
)

from post.models import Post
from post.serializers import PostSerializer
from post.permissions import MyIsAuthenticated, IsAnnaPermission



class PostListView(ListCreateAPIView):
    queryset = Post.objects.select_related('user').only('id', 'title', 'created', 'user__username').all()
    serializer_class = PostSerializer
    permission_classes = [MyIsAuthenticated]


class PostDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.select_related('user').only('id', 'title', 'description', 'created', 'user__username').all()
    serializer_class = PostSerializer
    permission_classes = [IsAnnaPermission]
    lookup_field = 'pk'
