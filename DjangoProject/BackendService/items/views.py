from rest_framework.response import Response
from rest_framework.views import APIView
from items.models import Item
from rest_framework.request import Request
from rest_framework import status
from users.models import CustomUser, CustomUserSerializer
from items.models import UserCartItem, ItemSerializer, UserCartItemSerializer, UserFavoriteItem, RecommendItem, RecommendItemSerializer, ItemOption, ItemOptionSerializer, CartItemOption, CartItemOptionSerializer, OptionName
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError
# Create your views here.

def get_item_options(item: Item):
    options = ItemOption.objects.filter(item=item)
    options_data = [ItemOptionSerializer(option).data for option in options]

    name_set = set()
    options = list()

    for option_data in options_data:
        option_name = option_data.get('name')['name']
        option_value = option_data['value']

        if option_name not in name_set:
            name_set.add(option_name)
            option = {
                "name": option_name,
                "values": list()
            }
            options.append(option)
        option.get('values').append(option_value)

    return options


class FetchMarcketItems(APIView):
    def get(self, request: Request):
        items = Item.objects.all()
        itemsList = list()
        for item in items:
            itemsList.append(ItemSerializer(item).data)
        return Response(itemsList)


class CartItemDelete(APIView):
    def delete(self, request: Request):
        error = None
        try:
            request_body = request.data

            delete_item: dict = request_body.get('deleteItem')
            user_id = request_body.get('user').get('id')
            try:
                user = CustomUser.objects.get(id=user_id)
            except:
                return Response({'error': f"User with id {user_id} not found"}, status=status.HTTP_404_NOT_FOUND)

            try:
                item_id = delete_item.get('item').get('id')
                item = Item.objects.get(id=item_id)
                cart_item = UserCartItem.objects.get(item=item, user=user)
                cart_item.delete()
            except ObjectDoesNotExist:
                error = f"Item with id {item_id} not found for user"
            except Exception as e:
                error = f"Failed to delete item {item_id}: {str(e)}"

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
            user_data = CustomUserSerializer(user).data

            cart_items = UserCartItem.objects.filter(user=user)

            selected_options_data = []
            serialized_data = []

            for cart_item in cart_items:
                cart_item_data = UserCartItemSerializer(cart_item).data

                # options 添加
                selected_options = CartItemOption.objects.filter(cart_item=cart_item)
                for selected_option in selected_options:
                    selected_options_data.append({
                        "option_key": selected_option.name.name,
                        "value": selected_option.value
                    })

                item_options_data = get_item_options(cart_item.item)

                print(selected_options_data)
                print(item_options_data)
                if user_data and cart_item_data:
                    serialized_data.append({
                        'item': cart_item_data,
                        'options': item_options_data,
                        'selected_options': selected_options_data,
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
        selected_options: dict = request_body.get('options')

        print("1", selected_options)
        # 添加cart options
        # options_list: list[dict] = request_body.get('options')

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

            if UserCartItem.objects.filter(user=user, item=item).exists():
                return Response({"error": "Item has existed"}, status=status.HTTP_200_OK)

            # 创建新 CartItem 对象
            new_cart_item = UserCartItem.objects.create(user=user, item=item)
            
            # 循环，修改每一组键值
            for selected_option_name, selected_option_value in selected_options.items():
                print(new_cart_item)
                print(selected_option_name, selected_option_value)
                # 获取对应的 OptionName 对象, 由于是键值，使用第一个就可以
                db_option_name = OptionName.objects.filter(name=selected_option_name)
                
                # 不存在就创建一个键值出来，一般来说是存在的
                if not db_option_name.exists():
                    db_option_name = OptionName.objects.create(name=selected_option_name)
                else:
                    db_option_name = db_option_name.first()
                

                print("db_option_name", db_option_name)

                # 筛选出实际已经存在的键对应的 options value 对象，匹配 name 键，理论上 CartItem Option 中的每一个键值只会有一个值
                # 这里理论上一定是不存在的，因为保证 CartItem 在一个键对应中只能有一个 OptionName 键值对象，所以相同key， value 只会有一个，我们筛选出这个 key ，然后改变它的值
                db_cart_item_option = CartItemOption.objects.filter(name=db_option_name, value=selected_option_name)

                # 不存在则创建新键值
                if not db_cart_item_option.exists():
                    db_cart_item_option = CartItemOption.objects.create(cart_item=new_cart_item, name=db_option_name, value=selected_option_value)
                else:  # 存在则
                    db_cart_item_option = db_cart_item_option.first()
                    print("db_cart_item_option", db_cart_item_option)
                    db_cart_item_option.value = selected_option_value

                print(db_cart_item_option)

                # 如果这个参数不存在， 创建这个数据行
                # if not db_cart_item_options.exists():
                #     CartItemOption.objects.create(cart_item=new_cart_item, name=db_option_name, value=selected_option_value)
                # else:
                #     # 这里是更改已有的db_option_name_obj
                #     db_cart_item_options.first().value = selected_option_value
        except Exception as e:
            print(e)
            new_cart_item.delete()
            return Response({"error": "Server error"}, status=status.HTTP_400_BAD_REQUEST)

        # UserItem check
        itemcheck = UserCartItem.objects.get(user=user, item=item).item
        try:
            return Response({"message": f"{itemcheck.name} has been added to cart"}, status=status.HTTP_200_OK)
        except:
            return Response({'error': f"{itemcheck.name} addation failed"}, status=status.HTTP_204_NO_CONTENT)

    def patch(self, request: Request):
        request_body = request.data
        user_id = request_body.get('userId')
        item_id = request_body.get('itemId')
        update_selected_options: dict = request_body.get('options')

        print(update_selected_options)
        # 更新options
        try:
            user = CustomUser.objects.get(id=user_id)
            item = Item.objects.get(id=item_id)
        except:
            return Response({"error": "Username not found"}, status=status.HTTP_404_NOT_FOUND)

        try:

            cart_item = UserCartItem.objects.get(user=user, item=item)
            # cart_item.selected_options = update_selected_options
            return Response({"message": "Test"}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Item has existed"}, status=status.HTTP_200_OK)




class FetchItemDetails(APIView):
    def get(self, request: Request, id: str):

        item = Item.objects.get(id=id)
        item_data = ItemSerializer(item).data
       
        response_data = {
            "item": item_data,
            "options": list()           # [{"name": KEY, "values": ["value1", "value2", "value3"]}]
        }

        response_data['options'] = get_item_options(item)
        print(response_data)
        return Response(response_data, status=status.HTTP_200_OK)


class FetchAllFavoriteItems(APIView):
    def get(self, request: Request, username):
        if not username:
            return Response({"error": "Username deficiency"}, status=status.HTTP_204_NO_CONTENT)

        try:
            user = CustomUser.objects.get(username=username)
            items = UserCartItem.objects.filter(user=user)

            serialized_data = []

            # 用户数据
            user_data = CustomUserSerializer(user).data
            serialized_data = {
                'user': user_data,
                'items': [ItemSerializer(item.item).data for item in items]
            }

            return Response(serialized_data, status=status.HTTP_200_OK)
        except Exception:
            return Response({"error": "Username does not exist"}, status=status.HTTP_404_NOT_FOUND)


class ItemAddToFavorite(APIView):
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
            favorite_item = UserFavoriteItem.objects.create(
                user=user, item=item)
            favorite_item.save()
        except:
            return Response({"error": "Item has existed"}, status=status.HTTP_200_OK)

        # UserItem check
        itemcheck = UserFavoriteItem.objects.get(user=user, item=item).item
        try:
            return Response({"message": f"{itemcheck.name} has been added to cart"}, status=status.HTTP_200_OK)
        except:
            return Response({'error': f"{itemcheck.name} addation failed"}, status=status.HTTP_204_NO_CONTENT)


class FetchRecommendItem(APIView):
    def get(self, request: Request):
        recommendItems = RecommendItem.objects.all()
        return Response([RecommendItemSerializer(item).data.get('item') for item in recommendItems], status=status.HTTP_200_OK)
