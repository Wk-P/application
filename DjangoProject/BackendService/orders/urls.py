from django.urls import path
from orders.views import Orders, OrderCreate, OrdersSearch, DeleteOrder

urlpatterns = [
    path("all/", Orders.as_view(), name="orders_list"),
    path("create/", OrderCreate.as_view(), name="orders_list"),
    path("search/<str:username>/", OrdersSearch.as_view(), name="orders_search"),
    path("delete/", DeleteOrder.as_view(), name="orders_delete"),
]