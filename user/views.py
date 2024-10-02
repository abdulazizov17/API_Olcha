from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView


class UserLoginApiView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            response = {
                'success': True,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': {
                    'username': user.username,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                }
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutApiView(APIView):
    authentication_classes = (TokenAuthentication, )
    parser_classes = (JSONParser, )
    def post(self, request):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({"success": True, "detail": "Logged out!"}, status=status.HTTP_200_OK)



class RegisterApiView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        token, created = Token.objects.get_or_create(user=user)

        response = {
            'success': 'True',
            'token': token.key,
            'user': user.username,
            'email': user.email,
            'created': created,
        }
        return Response(response, status=status.HTTP_201_CREATED)