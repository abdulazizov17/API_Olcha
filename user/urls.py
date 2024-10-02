from django.urls import path
from user.views import UserLoginApiView, UserLogoutApiView,RegisterApiView

urlpatterns = [
    path('login/', UserLoginApiView.as_view(), name='login'),
    path('logout/', UserLogoutApiView.as_view()),
    path('register/', RegisterApiView.as_view())
]