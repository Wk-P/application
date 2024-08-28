from django.urls import path
from items.views import Items, ItemsSearch, ItemUpload

urlpatterns = [
    path("all/", Items.as_view(), name="items_list"),
    path("search/<str:name>/", ItemsSearch.as_view(), name="items_search"),
    path("upload/", ItemUpload.as_view(), name="items_upload"),
]