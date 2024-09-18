from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book

# def index(request):
#     data = {
#         'message': 'Hello World!',
#         'status_code': 201,
#         'user':'John'
#
#     }
#     return JsonResponse(data)

#
# class UserListView(APIView):
#     permission_classes = [AllowAny]
#
#     def get(self, request):
#         # usernames = [user.username for user in User.objects.all()]
#         data = [
#             {
#                 'username': user.username,
#                 'is_active': user.is_active,
#                 'is_superuser': user.is_superuser,
#                 'password': user.password
#
#             }
#             for user in User.objects.all()
#         ]
#         return Response(data)
#

class BookListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = [
            {
                'title': book.title,
                'author': book.author,
                'publication_date': book.publication_date
            }
            for book in Book.objects.all()
        ]
        return Response(data)