from django.urls import path

from olcha.views import category,group,product,comment
urlpatterns = [
    path('api/categories/', category.CategoryListApiView.as_view(), name='category-list'),
    path('api/groups/', group.GroupListApiView.as_view(), name='group-list'),
    path('api/categories/<slug:category_slug>/', category.CategoryDetailApiView.as_view(), name='category-detail'),
    path('all-products/', product.ProductListApiView.as_view(), name='all-products'),
    path('all-images/', product.ImageListApiView.as_view(),name='all-products'),
    path('all-comment/', comment.CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('all-comments/', comment.CommentDetailAPIView.as_view(), name='comment-detail'),

]
