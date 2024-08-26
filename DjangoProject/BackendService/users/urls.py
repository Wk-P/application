from django.urls import path
from users.views import CustomLogin, CustomRegister, CustomLogout, UserStatusView
urlpatterns = [
    # 登录界面
    path("login/", CustomLogin.as_view()),
    path("register/", CustomRegister.as_view()),
    path("logout/", CustomLogout.as_view()),
    path('status/', UserStatusView.as_view()),
]