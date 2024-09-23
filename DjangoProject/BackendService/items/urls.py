from django.urls import path
from items.views import FetchMarcketItems, ItemsSearch, FetchAllCartItems, ItemAddToCart, FetchItemDetails, CartItemDelete

urlpatterns = [
    path("all/", FetchMarcketItems.as_view(), name="items_list"),
    path("cart/delete/", CartItemDelete.as_view(), name='cart_items_delete'),
    path("search/<str:keywords>/", ItemsSearch.as_view(), name="items_search"),
    path("cart/<str:username>/", FetchAllCartItems.as_view()),
    path("cart/", ItemAddToCart.as_view()),
    path("details/<str:id>/", FetchItemDetails.as_view()),
]