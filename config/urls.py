from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings, custom_obtain_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('book.urls')),
                  path('api-auth/', include('rest_framework.urls')),
                  path('olcha/', include('olcha.urls')),
                  path('api-token-auth/', custom_obtain_token.CustomAuthToken.as_view()),
                  path('user/', include('user.urls')),
                  path('api/token/access/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
