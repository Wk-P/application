from django.urls import path
from items.views import FetchMarcketItems, ItemsSearch, FetchAllCartItems, ItemAddToCart, FetchItemDetails, CartItemDelete, FetchAllFavoriteItems, ItemAddToFavorite, FetchRecommendItem

urlpatterns = [
    path("all/", FetchMarcketItems.as_view(), name="items_list"),
    path("cart/delete/", CartItemDelete.as_view(), name='cart_items_delete'),
    path("favorite/<str:username>/", FetchAllFavoriteItems.as_view(), name='favorite_items'),
    path("search/<str:keywords>/", ItemsSearch.as_view(), name="items_search"),
    path("cart/<str:username>/", FetchAllCartItems.as_view()),
    path("cart_add/", ItemAddToCart.as_view(), name='cart_add'),
    path("favorite_add/", ItemAddToFavorite.as_view(), name='favorite_add'),
    path("details/<str:id>/", FetchItemDetails.as_view()),
    path("recommend/", FetchRecommendItem.as_view()),
]