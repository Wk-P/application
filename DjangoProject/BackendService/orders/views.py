from django.shortcuts import render
import typing
# Create your views here.
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from orders.models import Order, OrderSerializer, OrderItemOption, OrderItemOptionSerializer
from items.models import Item, UserCartItem, ItemSerializer, CartItemOption, OptionName
from users.models import CustomUser, CustomUserSerializer
from rest_framework import status
import datetime


def get_order_item_selected_options(order: Order):
    selected_options = OrderItemOption.objects.filter(order=order)
    selected_options_data = [OrderItemOptionSerializer(option).data for option in selected_options]

    selected_option_name_set = set()
    response_selected_options = list()

    for selected_option_data in selected_options_data:
        selected_option_name = selected_option_data.get('name')['name']
        selected_option_value = selected_option_data['value']

        if selected_option_name not in selected_option_name_set:
            selected_option_name_set.add(selected_option_name)
            selected_option = {
                "name": selected_option_name,
                "values": list()
            }
            response_selected_options.append(selected_option)
        selected_option.get('values').append(selected_option_value)

    return response_selected_options


def test_response():
    return Response({"test": "ok"}, status=status.HTTP_400_BAD_REQUEST)

# 订单控制
class FetchAllOrders(APIView):
    def get(self, request: Request):
        ordersSet = Order.objects.all()
        result_list = list()

        for order in ordersSet:
            order_selected_options = get_order_item_selected_options(order=order)
            result_list.append({
                "order": OrderSerializer(order).data,
                "selected_options": order_selected_options
            })

        return Response(result_list, status=status.HTTP_200_OK)


class OrderCreate(APIView):
    def post(self, request: Request):
        request_body: dict = request.data

        try:
            orders: typing.List[dict[str, str]] = request_body.get('newOrders')
            # print order request information for logger
            print(orders)
            
            # 遍历 orders 生成订单
            for order in orders:
                item_id = order.get("item").get('id')
                user_id = order.get("user").get('id')
                quantity = order.get("quantity")
                total_price = order.get("totalPrice")
                user = CustomUser.objects.get(id=user_id)
                item = Item.objects.get(id=item_id)
                selected_options = order.get('selected_options')

                print(item_id)
                if (not item_id) or (not user_id) or (quantity <= 0) or (total_price <= 0):
                    raise Exception('Error')
                
                # UserCartItem 删除
                cartItems = UserCartItem.objects.filter(item=item, user=user)
                print(cartItems.values())
                if cartItems.exists():
                    cartItems.delete()

                # create order id
                order_id = str(item_id) + str(datetime.datetime.now()).replace(
                '-', '').replace(' ', 'TT').replace(':', 'EM').replace('.', 'OD')
                order = Order.objects.create(
                    order_id=order_id, item=item, user=user, quantity=int(quantity),
                    total_price=float(total_price)
                )
                order.save()

                # create order-item-selected-options

                for selected_option in selected_options:
                    selected_option_name = selected_option['option_key']
                    selected_option_value = selected_option['value']
                    
                    # check objects
                    selected_option_name_obj = None
                    if not OptionName.objects.filter(name=selected_option_name).exists():
                        selected_option_name_obj = OptionName.objects.create(name=selected_option_name)

                    selected_option_name_obj = OptionName.objects.filter(name=selected_option_name).first()
                    OrderItemOption.objects.create(order=order, name=selected_option_name_obj, value=selected_option_value)
                    

            return Response({"message": "ok"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error": "Error"}, status=status.HTTP_400_BAD_REQUEST)
            


class OrdersSearch(APIView):
    def get(self, request: Request):
        return Response({"message": "OK"})

    def post(self, request: Request, username):
        # response data
        userId = None

        print(username)
        if username:
            # user search
            users = CustomUser.objects.filter(username=username)
            print(users)
            if not users.exists():
                return Response({"result": None}, status=status.HTTP_204_NO_CONTENT)
            
            # response data
            user = users.first()
            userId = user.id
            ordersList = list()
            
            orders = Order.objects.filter(user=user)
            if not orders.exists():
                return Response({"result": None}, status=status.HTTP_204_NO_CONTENT)
                # to list for response

            for order in orders:
                order_object = dict()
                order_object['item-name'] = order.item.name
                order_object['updated-time'] = order.updated_at
                order_object['created-time'] = order.created_at
                order_object['quantity'] = order.quantity
                order_object['price'] = order.item.price
                order_object['total-price'] = order.total_price
                order_object['order-id'] = order.order_id
                
                ordersList.append(order_object)

            return Response({"userId": userId, "username": username, "orders": ordersList}, status=status.HTTP_200_OK)
        else:
            return Response({"result": None}, status=status.HTTP_404_NOT_FOUND)

class DeleteOrder(APIView):
    def post(self, request: Request):
        request_body = request.data
        deleteOrders = request_body.get("deleteOrders")

        for order in deleteOrders:
            order = Order.objects.filter(order_id=order.get("orderId"))
            if order.exists():
                order.first().delete()
            else:
                Response({"error": "", "error_code": 1}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({"message": "OK"}, status=status.HTTP_200_OK)