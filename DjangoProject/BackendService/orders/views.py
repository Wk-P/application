from django.shortcuts import render
import typing
# Create your views here.
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from orders.models import Order, OrderSerializer
from items.models import Item, UserCartItem, ItemSerializer
from users.models import CustomUser, CustomUserSerializer
from rest_framework import status
import datetime

# 订单控制
class Orders(APIView):
    def get(self, request: Request):
        ordersSet = Order.objects.all()

        result_list = list()
        for order in ordersSet:
            result_list.append(OrderSerializer(order).data)

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