from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from items.models import Item

# Create your views here.
class Items(APIView):
    def get(self, request):
        itemsList = list(Item.objects.all().values())
        return Response(itemsList)
    

class ItemsSearch(APIView):
    def search(self, query: str):
        searchResultList = list(Item.objects.filter(name__icontains=query).values())
        print(searchResultList)
        return searchResultList


    def get(self, request, name):
        if name == "all":
            searchResults = list(Item.objects.all().values())
        else:
            searchResults = self.search(name)
        print(searchResults)
        return Response(searchResults)


class ItemUpload(APIView):
    def post(self, request):
        request_body = request.data
        imgLink = request_body.get('imgLink')
        # 创建或者修改item文件
        print(imgLink)
        return Response({'imgLink': imgLink}, status=200)