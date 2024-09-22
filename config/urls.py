from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('book.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('olcha/', include('olcha.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
