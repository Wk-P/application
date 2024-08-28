from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from users.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from items.models import Item, UserItem
from django.forms.models import model_to_dict
from django.shortcuts import redirect
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
import uuid
# Create your views here.


class UserStatusView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get(self, request):
        # If the request is authenticated, return a positive status
        return Response({"message": "User is logged in."}, status=status.HTTP_200_OK)


class CustomLogout(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get(self, request):
         return Response({"message": "User is logged in."}, status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            if request.auth:
                request.auth.delete()
                logout(request)
                return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'No active token found.'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'detail': 'An error occurred during logout.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CustomLogin(APIView):
    def get(self, request):
        return Response({"message": "OK"})

    def post(self, request):
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
    def get(self, request):
        return Response({"message": "OK"})

    def post(self, request):

        request_body = request.data
        username = request_body.get('username')
        password = request_body.get('password')
        email = request_body.get('email')
        tel = request_body.get('tel')
        uid = str(uuid.uuid4()).replace('-', '')
        address = request_body.get('address')

        try:
            if CustomUser.objects.filter(username=username).exists():
                return Response({"error": "User already exists"}, status=status.HTTP_409_CONFLICT)
            try:
                user = CustomUser.objects.create_user(username=username, password=password, email=email, tel=tel, uid=uid, address=address)
                return Response({"message": "User registered successfully", "user": model_to_dict(user)}, status=status.HTTP_200_OK)
            except ValidationError as e:
                raise e
        except Exception as e:
            # Log the exception
            print(e)
            return Response({"error": "An error occurred during registration"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


# search cart items
class CartItems(APIView):
    def get(self, request):
        return Response({"message": "OK"})
    

    def post(self, request, username):
        if not username:
            return Response({"error": "Username deficiency"}, status=status.HTTP_204_NO_CONTENT)
        
        items = UserItem.objects.filter(username=username)
        print(items)

        return Response({"cart-items": items}, status=status.HTTP_200_OK)

        
# add cart items
class ItemAddToCart(APIView):
    def get(self, request):
        return Response({"message": "OK"})
    

    def post(self, request):
        request_body = request.data
        username = request_body.get('username')
        itemname = request_body.get('itemname')

        if not username:
            return Response({"error": "Username deficiency"}, status=status.HTTP_204_NO_CONTENT)
        
        if not itemname:
            return Response({"error": "Itemname deficiency"}, status=status.HTTP_204_NO_CONTENT)
        
        users = CustomUser.objects.filter(username=username)
        if not users.exists():
            return Response({"error": "Username not found"}, status=status.HTTP_404_NOT_FOUND)
        
        items = Item.objects
        if not items.exists():
            return Response({"error": "Username not found"}, status=status.HTTP_404_NOT_FOUND)

        user = users.first()
        item = items.first()


        # UserItem
        items = UserItem.objects.filter(user=user, item=item)

        if items.exists():
            item = items.first()
            if item.is_cart:
                return Response({"message": "Has been added to cart"}, status=status.HTTP_200_OK)
            else:
                item.is_cart = True
        # item does not exist
        else:
            cart_item = UserItem(user=user, item=item, is_cart=True)
            cart_item.save()

        updated_cart_items = UserItem.objects.filter(user=user)

        return Response({"cart-items": updated_cart_items}, status=status.HTTP_200_OK)
    

class FavoriteItems(APIView):
    def get(self, request):
        return Response({"message": "OK"})
    

    def post(self, request, username):
        if not username:
            return Response({"error": "Username deficiency"}, status=status.HTTP_204_NO_CONTENT)
        
        