from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from users.models import CustomUser, CustomUserSerializer, AddressReceiver, AddressReceirSerializer
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

# 用户信息修改


class UserInfoModified(APIView):
    def post(self, request: Request, user_id):
        request_body: dict = request.data
        print(request_body)

        try:
            user = CustomUser.objects.get(id=user_id)
        except Exception as e:
            print(e)
            error_code = 1
            return Response({"error": 1, "error_code": error_code, "error": "User not exists"}, status=status.HTTP_404_NOT_FOUND)

        name = request_body.get('name')
        tel = request_body.get('telephone')
        email = request_body.get('email')

        if email:
            user.email = email

        if tel:
            user.tel = tel

        if name:
            user.name = name
        user.save()  # update use profile

        return Response({"message": "Modified successfully!"}, status=status.HTTP_200_OK)

# 修改已存在的 Address Receiver 数据


class ModifyUserAddressReceiverInfo(APIView):
    def post(self, request: Request, user_id, addr_recv_id):
        request_body: dict = request.data
        print(request_body)
        address = request_body.get('address')
        receiver = request_body.get('receiver')
        try:
            user = CustomUser.objects.get(id=user_id)
            print(user)

            address_receiver = AddressReceiver.objects.get(id=addr_recv_id)

            if address:
                address_receiver.address = address
            if receiver:
                address_receiver.receiver = receiver
            address_receiver.save()

            return Response({"message": "Modified successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            error_code = 1
            return Response({"code": error_code, "error": "Infomation does not exists"}, status=status.HTTP_404_NOT_FOUND)


# 新增 Address Receiver 数据
class AddUserAddressReceiverInfo(APIView):
    def post(self, request: Request, user_id):
        try:
            request_body: dict = request.data
            print(request_body)

            user = CustomUser.objects.get(id=user_id)

            address = request_body.get('address')
            receiver = request_body.get('receiver')

            if address and receiver:
                new_address_receiver = AddressReceiver.objects.create(user=user, receiver=receiver, address=address)
                new_address_receiver.save()

                return Response({"message": "Create new address and receiver successfully!"}, status=status.HTTP_200_OK)
            else:
                raise Exception("No infomation")

        except Exception as e:
            print(e)
            error_code = 1
            return Response({"code": error_code, "error": "Server Handle Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FetchUserAllAddressReceiver(APIView):
    def get(self, request: Request, user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
            response_list = list()
            for address_receiver in AddressReceiver.objects.filter(user=user):
                response_list.append(AddressReceirSerializer(address_receiver).data)
            
            return Response(response_list, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            error_code = 1
            return Response({"error_code": error_code, "error": "User does not exists"}, status=status.HTTP_404_NOT_FOUND)
