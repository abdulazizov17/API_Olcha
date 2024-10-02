from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from typing import Dict, Any







class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,attrs:Dict[str,Any]) -> Dict[str, str]:
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        data['tokens'] = {
            'refresh' : str(refresh),
            'access' : str(refresh.access_token)
        }
        data['user'] =self.user.username
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
