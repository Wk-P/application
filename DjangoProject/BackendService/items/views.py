from rest_framework.response import Response
from rest_framework.views import APIView
from items.models import Item
from rest_framework.request import Request
from rest_framework import status
from users.models import CustomUser, CustomUserSerializer
from items.models import UserCartItem, ItemSerializer, UserCartItemSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError
# Create your views here.


class FetchMarcketItems(APIView):
    def get(self, request: Request):
        items = Item.objects.all()
        itemsList = list()
        for item in items:
            itemsList.append(ItemSerializer(item).data)
        return Response(itemsList)

class CartItemDelete(APIView):
    def delete(self, request: Request):
        error = list()
        try:
            request_body = request.data
            delete_items = request_body.get('deleteItems')
            user_id = request_body.get('user').get('id')
            try:
                user = CustomUser.objects.get(id=user_id)
            except:
                return Response({'error': f"User with id {user_id} not found"}, status=status.HTTP_404_NOT_FOUND)
            for delete_item in delete_items:
                try:
                    item_id = delete_item.get('id')
                    item = Item.objects.get(id=item_id)
                    cart_item = UserCartItem.objects.get(item=item, user=user)
                    cart_item.delete()
                except ObjectDoesNotExist:
                    error.append(f"Item with id {item_id} not found for user")
                except Exception as e:
                    error.append(f"Failed to delete item {item_id}: {str(e)}")
            if error:
                return Response({'error': error, 'message': "Some items failed to delete"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': "Delete successful"}, status=status.HTTP_200_OK)
        
        except ValidationError as ve:
            return Response({'error': f"Validation Error: {str(ve)}"}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'error': f"Unexpected Error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# search cart items
class ItemsSearch(APIView):
    def search(self, query: str):
        searchResultList = list(Item.objects.filter(
            name__icontains=query).values())
        print(searchResultList)
        return searchResultList

    def get(self, request: Request, keywords: str):
        print(request)
        if keywords == "all" or keywords == "":
            searchResults = list(Item.objects.all().values())
        else:
            searchResults = self.search(keywords)
        print(searchResults)
        return Response(searchResults)

class FetchAllCartItems(APIView):
    def get(self, request: Request, username):
        if not username:
            return Response({"error": "Username deficiency"}, status=status.HTTP_204_NO_CONTENT)

        else:
            users = CustomUser.objects.filter(username=username)
            if not users.exists():
                return Response({"error": "Username does not exist"}, status=status.HTTP_404_NOT_FOUND)

            user = users.first()
            items = UserCartItem.objects.filter(user=user)

            serialized_data = []

            user_data = None
            item_data = None

            for item in items:
                user_data = CustomUserSerializer(item.user).data
                item_data = ItemSerializer(item.item).data
            if user_data and item_data:
                serialized_data.append({
                    'user': user_data,
                    'item': item_data
                })

        return Response(serialized_data, status=status.HTTP_200_OK)

# add cart items
class ItemAddToCart(APIView):
    def get(self, request: Request):
        return Response({"message": "OK"})

    def post(self, request: Request):
        request_body = request.data
        user_id = request_body.get('userId')
        item_id = request_body.get('itemId')

        if not user_id:
            return Response({"error": "Username deficiency"}, status=status.HTTP_204_NO_CONTENT)

        if not item_id:
            return Response({"error": "Itemname deficiency"}, status=status.HTTP_204_NO_CONTENT)

        try:
            user = CustomUser.objects.get(id=user_id)
            item = Item.objects.get(id=item_id)

        except:
            return Response({"error": "Username not found"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            cart_item = UserCartItem.objects.create(user=user, item=item)
            cart_item.save()
        except:
            return Response({"error": "Item has existed"}, status=status.HTTP_200_OK)
        

        # UserItem check
        itemcheck = UserCartItem.objects.get(user=user, item=item).item
        try:
            return Response({"message": f"{itemcheck.name} has been added to cart"}, status=status.HTTP_200_OK)
        except:
            return Response({'error': f"{itemcheck.name} addation failed"}, status=status.HTTP_204_NO_CONTENT)

class FetchItemDetails(APIView):
    def get(self, request: Request, id: str):
        
        item = ItemSerializer(Item.objects.get(id=id)).data
        return Response(item, status=status.HTTP_200_OK)
