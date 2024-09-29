from django.urls import path
from user.views import UserLoginApiView, UserLogoutApiView,RegisterApiView

urlpatterns = [
    path('get-token/', UserLoginApiView.as_view()),
    path('token-delete/', UserLogoutApiView.as_view()),
    path('token-register/',RegisterApiView.as_view())
]