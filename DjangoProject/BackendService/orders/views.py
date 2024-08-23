from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from orders.models import Order
from items.models import Item
from users.models import CustomUser
from rest_framework import status
import datetime

class Orders(APIView):
    def get(self, request):
        ordersList = list(Order.objects.all().values())
        return Response(ordersList)
    

class OrderCreate(APIView):
    def post(self, request):
        request_body = request.data
        
        # print order request information for logger
        print(request_body)
        for k, v in request_body.items():
            print(k, "=",  v)

        # create order id
        order_id = str(datetime.datetime.now()).replace('-', '').replace(' ', 'TT').replace(':', 'EM').replace('.', 'OD')
        print(order_id)

        item = None
        user = None
        error = None

        item_id = request_body.get('itemId')
        items = Item.objects.filter(pk=item_id)
        users = CustomUser.objects.filter(username=request_body.get('username'))
        if items.exists():
            item = items.first()
        
        if users.exists():
            user = users.first()
        
        # print for logger
        print(users)
        print(items)
        
        try:    
            if item and user:
                quantity = int(request_body.get('orderSum'))
                
                total_price = quantity * item.price
                order = Order(order_id=order_id, item=item, user=user, quantity=quantity, total_price=total_price)
                
                # for logger
                print(order)
                
                order.save()
            else:
                error = "Order submitted failed"
        except Exception as e:
            print()

        return Response({"message": "OK", "error": error, "order_id": order_id})
    


class OrdersSearch(APIView):
    def get(self, request):
        return Response({"message": "OK"})

    def post(self, request, username):
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


            
