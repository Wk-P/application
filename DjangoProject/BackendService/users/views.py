from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from users.models import CustomUser, CustomUserSerializer
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.forms.models import model_to_dict
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
import uuid
# Create your views here.


class UserStatusView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get(self, request):
        # If the request is authenticated, return a positive status
        return Response({"message": "User is logged in."}, status=status.HTTP_200_OK)


class CustomLogout(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get(self, request: Request):
        return Response({"message": "User is logged in."}, status=status.HTTP_200_OK)

    def post(self, request: Request):
        try:
            if request.auth:
                request.auth.delete()
                return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'No active token found.'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'detail': 'An error occurred during logout.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CustomLogin(APIView):
    def get(self, request: Request):
        return Response({"message": "OK"})

    def post(self, request: Request):
        request_body = request.data
        username = request_body.get('username')
        password = request_body.get('password')
        try:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                user_dict = model_to_dict(user)
                return Response({"message": "User login successful", "user": user_dict}, status=status.HTTP_200_OK)
            else:
                # 手动实现登录验证失败
                return Response({"error": "User not exists"}, status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class CustomRegister(APIView):
    def get(self, request: Request):
        return Response({"message": "OK"})

    def post(self, request: Request):

        request_body = request.data
        username = request_body.get('username')
        password = request_body.get('password')
        email = request_body.get('email')
        tel = request_body.get('tel')
        name = request_body.get('name')
        uid = str(uuid.uuid4()).replace('-', '')
        address = request_body.get('address')

        try:
            if CustomUser.objects.filter(username=username).exists():
                return Response({"error": "User already exists"}, status=status.HTTP_409_CONFLICT)
            try:
                user = CustomUser.objects.create_user(
                    username=username, name=name, password=password, email=email, tel=tel, uid=uid, address=address)
                user_data = CustomUserSerializer(user).data
                return Response({"message": "User registered successfully", "user": user_data}, status=status.HTTP_200_OK)
            except ValidationError as e:
                raise e
        except Exception as e:
            # Log the exception
            print(e)
            if str(e) == 'UNIQUE constraint failed: users_customuser.tel':
                # tel number conflict
                error_code = 1
            return Response({"error": 1, 'error_code': error_code}, status=status.HTTP_409_CONFLICT)


class UserInfoModified(APIView):
    def post(self, request: Request):
        request_body: dict = request.data.get('user')
        username = request_body.get('username')
        password = request_body.get('password')
        email = request_body.get('email')
        tel = request_body.get('tel')
        name = request_body.get('name')
        address = request_body.get('address')

        if CustomUser.objects.filter(username=username).exists():
            user = CustomUser.objects.filter(username=username)
            if user.exists():
                user = user.first()
                # 更新用户信息
                if password:
                    # 使用 Django 的 set_password 方法来处理密码
                    user.set_password(password)
                user.email = email
                user.tel = tel
                user.name = name
                user.address = address
                user.save()  # 保存用户的更新
                return Response({"message": "Modified successfully"}, status=status.HTTP_200_OK)
            else:
                error_code = 1
                return Response({"error": 1, 'error_code': error_code}, status=status.HTTP_409_CONFLICT)
        else:
            return Response({"error": 1, "error_code": 1, "error": "User not exists"}, status=status.HTTP_409_CONFLICT)
