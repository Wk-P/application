from django.urls import path
from items.views import Items, ItemsSearch

urlpatterns = [
    path("all/", Items.as_view(), name="items_list"),
    path("search/<str:name>/", ItemsSearch.as_view(), name="items_search"),
]