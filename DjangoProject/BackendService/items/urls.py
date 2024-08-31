from django.urls import path
from items.views import FetchMarcketItems, ItemsSearch, ItemUpload, FetchAllCartItems, ItemAddToCart

urlpatterns = [
    path("all/", FetchMarcketItems.as_view(), name="items_list"),
    path("search/<str:keywords>/", ItemsSearch.as_view(), name="items_search"),
    path("upload/", ItemUpload.as_view(), name="items_upload"),
    path("cart/<str:username>/", FetchAllCartItems.as_view()),
    path("cart/", ItemAddToCart.as_view()),
]