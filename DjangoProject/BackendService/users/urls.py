from django.urls import path
from users.views import CustomLogin, CustomRegister
urlpatterns = [
    # 登录界面
    path("login/", CustomLogin.as_view()),
    path("register/", CustomRegister.as_view()),
]