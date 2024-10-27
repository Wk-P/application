from django.urls import path
from orders.views import FetchAllOrders, OrderCreate, OrdersSearch, DeleteOrder

urlpatterns = [
    path("all/", FetchAllOrders.as_view(), name="orders_list"),
    path("create/", OrderCreate.as_view(), name="create_orders"),
    path("search/<str:username>/", OrdersSearch.as_view(), name="orders_search"),
    path("delete/", DeleteOrder.as_view(), name="orders_delete"),
]