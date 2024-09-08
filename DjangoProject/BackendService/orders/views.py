from django.shortcuts import render
import typing
# Create your views here.
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from orders.models import Order
from items.models import Item, UserCartItem, ItemSerializer
from users.models import CustomUser, CustomUserSerializer
from rest_framework import status
import datetime

class Orders(APIView):
    def get(self, request: Request):
        ordersSet = Order.objects.all().values('id', 'order_id', 'user_id', 'item_id', 'quantity')

        result_list = list()
        for order in ordersSet:
            item_info = ItemSerializer(Item.objects.filter(id=order.get('item_id')).first()).data
            user_info = CustomUserSerializer(CustomUser.objects.filter(id=order.get('user_id')).first()).data

            result_list.append({
                "item_info": item_info,
                "user_info": user_info,
                "order_id": order.get("order_id"),
                "totalQuantity": order.get("quantity")
            })

        print(result_list)
        return Response(result_list, status=status.HTTP_200_OK)


class OrderCreate(APIView):
    def post(self, request: Request):
        request_body: dict = request.data

        orders: typing.List[dict[str, str]] = request_body.get('newOrders')
        # print order request information for logger

        # 遍历 orders 生成订单
        for order in orders:
            item = order.get("item")
            userId = order.get("userId")
            quantity = order.get("totalQuantity")

            user = CustomUser.objects.filter(id=userId)
            if user.exists():
                user = user.first()
            else:
                return Response({"error": "User does not exist!"}, status=status.HTTP_204_NO_CONTENT)
            
            # 为每一个item生成新的订单
            item = Item.objects.filter(id=item['id'])

            if item.exists():
                item = item.first()

                # UserCartItem 删除
                cartItem = UserCartItem.objects.filter(item=item, user=user)
                if cartItem.exists():
                    cartItem = cartItem.first()
                    cartItem.delete()

                # create order id
                order_id = str(item.id) + str(datetime.datetime.now()).replace(
                '-', '').replace(' ', 'TT').replace(':', 'EM').replace('.', 'OD')
                order = Order.objects.create(
                    order_id=order_id, item=item, user=user, quantity=int(quantity),
                    total_price=int(quantity) * item.price
                )
                order.save()
                return Response({"message": "ok"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Item does not exist"}, status=status.HTTP_200_OK)


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