from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings, custom_obtain_token

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('book.urls')),
                  path('api-auth/', include('rest_framework.urls')),
                  path('olcha/', include('olcha.urls')),
                  path('api-token-auth/', custom_obtain_token.CustomAuthToken.as_view()),
                  path('user/', include('user.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
