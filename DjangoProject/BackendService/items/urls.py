from django.urls import path
from items.views import FetchMarcketItems, ItemsSearch, ItemUpload, FetchAllCartItems

urlpatterns = [
    path("all/", FetchMarcketItems.as_view(), name="items_list"),
    path("search/<str:name>/", ItemsSearch.as_view(), name="items_search"),
    path("upload/", ItemUpload.as_view(), name="items_upload"),
    path("cart/<str:name>/", FetchAllCartItems.as_view())
]