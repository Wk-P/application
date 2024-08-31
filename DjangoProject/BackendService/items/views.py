from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from items.models import Item
from rest_framework.request import Request
from rest_framework import status
from users.models import CustomUser
from items.models import UserCartItem

# Create your views here.
class FetchMarcketItems(APIView):
    def get(self, request):
        itemsList = list(Item.objects.all().values())
        return Response(itemsList)
    

class ItemsSearch(APIView):
    def search(self, query: str):
        searchResultList = list(Item.objects.filter(name__icontains=query).values())
        print(searchResultList)
        return searchResultList


    def get(self, request, name):
        if name == "all":
            searchResults = list(Item.objects.all().values())
        else:
            searchResults = self.search(name)
        print(searchResults)
        return Response(searchResults)


class ItemUpload(APIView):
    def post(self, request: Request):
        request_body = request.data
        imgLink = request_body.get('imgLink')
        # 创建或者修改item文件
        print(imgLink)

        return Response({'imgLink': imgLink}, status=200)
    

# search cart items
class FetchAllCartItems(APIView):
    def get(self, request, username):
        if not username:
            return Response({"error": "Username deficiency"}, status=status.HTTP_204_NO_CONTENT)

        else:
            users = CustomUser.objects.filter(username=username)
            if not users.exists():
                return Response({"error": "Username does not exist"})

            user = users.first()
            items = UserCartItem.objects.filter(user=user).values_list
            print(items)

        return Response(items, status=status.HTTP_200_OK)


# add cart items
class ItemAddToCart(APIView):
    def get(self, request):
        return Response({"message": "OK"})
    

    def post(self, request: Request):
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
        items = UserCartItem.objects.filter(user=user, item=item)

        if items.exists():
            return Response({"message": "Has been added to cart"}, status=status.HTTP_200_OK)
        
        # item does not exist
        else:
            cart_item = UserCartItem(user=user, item=item)
            cart_item.save()

        updated_cart_items = UserCartItem.objects.filter(user=user)

        return Response({"cart-items": updated_cart_items}, status=status.HTTP_200_OK)