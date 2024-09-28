from django.urls import path
from users.views import CustomLogin, CustomRegister, CustomLogout, UserStatusView, UserInfoModified, FetchUserAllAddressReceiver, ModifyUserAddressReceiverInfo, AddUserAddressReceiverInfo
urlpatterns = [
    # 登录界面
    path("login/", CustomLogin.as_view()),
    path("register/", CustomRegister.as_view()),
    path('logout/', CustomLogout.as_view()),
    path('status/', UserStatusView.as_view()),
    path('modified/<str:user_id>/', UserInfoModified.as_view()),
    path('address/modified/<str:user_id>/<str:addr_recv_id>/',
         ModifyUserAddressReceiverInfo.as_view()),
    path('address/<str:user_id>/', FetchUserAllAddressReceiver.as_view()),
    path('address/add/<str:user_id>/', AddUserAddressReceiverInfo.as_view())
]
