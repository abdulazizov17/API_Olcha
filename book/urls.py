from django.contrib import admin

from book.views import BookListView, BookCreateView,CategoryView
from django.urls import path

urlpatterns = [
    path('all/books/', BookListView.as_view(), name='book-list'),
    path('detail/', BookCreateView.as_view(), name='book-detail'),
    path('categories/', CategoryView.as_view(), name='category-list'),
    # path('api/categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

]
