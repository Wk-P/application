from django.urls import path
from users.views import CustomLogin, CustomRegister, CustomLogout, UserStatusView, UserInfoModified
urlpatterns = [
    # 登录界面
    path("login/", CustomLogin.as_view()),
    path("register/", CustomRegister.as_view()),
    path("logout/", CustomLogout.as_view()),
    path('status/', UserStatusView.as_view()),
    path('modified/', UserInfoModified.as_view()),
]