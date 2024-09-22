from django.urls import path, include
from olcha import views

urlpatterns = [
    path('categories/', views.CategoryListApiView.as_view(), name='categories'),
    path('groups/', views.GroupListApiView.as_view(), name='groups'),
    path('category/<slug:slug>/', views.CategoryDetail.as_view(), name='category'),
    path('products/', views.ProductAPIView.as_view(), name='product_list_create'),
    path('products/<int:pk>/', views.ProductAPIView.as_view(), name='product_detail'),

]