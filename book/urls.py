
from django.contrib import admin
from django.urls import path,include

from book.views import BookListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),

]