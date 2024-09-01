from rest_framework.response import Response
from rest_framework.views import APIView
from items.models import Item
from rest_framework.request import Request
from rest_framework import status
from users.models import CustomUser
from items.models import UserCartItem
from rest_framework.parsers import MultiPartParser, FormParser
from pathlib import Path
# Create your views here.


class FetchMarcketItems(APIView):
    def get(self, request):
        itemsList = list(Item.objects.all().values())
        return Response(itemsList)


# search cart items
class ItemsSearch(APIView):
    def search(self, query: str):
        searchResultList = list(Item.objects.filter(
            name__icontains=query).values())
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
    parser_classes = (MultiPartParser, FormParser)  # 确保支持多部分表单数据解析

    def get(self, request: Request):
        directory = Path.home() / 'application' / 'VueProject' / 'public' / 'img'
        all_file_names = [f.name for f in directory.iterdir() if f.is_file()]
        return Response(all_file_names)


    def post(self, request: Request, *args, **kwargs):
        uploaded_file = request.FILES.get('file')  # 获取上传的文件
        if uploaded_file:
            # 使用 pathlib 处理路径
            save_dir = Path.home() / 'application' / 'VueProject' / 'public' / 'img'

            # 确保目标目录存在
            save_dir.mkdir(parents=True, exist_ok=True)

            # 保存文件
            file_path = save_dir / uploaded_file.name
            with file_path.open('wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            return Response({"message": "File uploaded successfully!", "file_name": uploaded_file.name}, status=200)
        else:
            return Response({"error": "No file uploaded"}, status=400)

    def delete(self, request: Request, *args, **kwargs):
        file_name = request.data.get('file_name')  # 获取要删除的文件名
        if not file_name:
            return Response({"error": "File name not provided"}, status=400)

        # 使用 pathlib 处理路径
        file_path = Path.home() / 'application' / 'VueProject' / 'public' / 'img' / file_name

        # 检查文件是否存在并删除
        if file_path.exists():
            file_path.unlink()  # 删除文件
            return Response({"message": f"File '{file_name}' deleted successfully!"}, status=200)
        else:
            return Response({"error": f"File '{file_name}' not found"}, status=404)


class FetchAllCartItems(APIView):
    def get(self, request, username):
        if not username:
            return Response({"error": "Username deficiency"}, status=status.HTTP_204_NO_CONTENT)

        else:
            users = CustomUser.objects.filter(username=username)
            if not users.exists():
                return Response({"error": "Username does not exist"})

            user = users.first()
            items = UserCartItem.objects.filter(user=user).values_list
            print(items)

        return Response(items, status=status.HTTP_200_OK)


# add cart items
class ItemAddToCart(APIView):
    def get(self, request):
        return Response({"message": "OK"})

    def post(self, request: Request):
        request_body = request.data
        username = request_body.get('username')
        itemname = request_body.get('itemname')

        if not username:
            return Response({"error": "Username deficiency"}, status=status.HTTP_204_NO_CONTENT)

        if not itemname:
            return Response({"error": "Itemname deficiency"}, status=status.HTTP_204_NO_CONTENT)

        users = CustomUser.objects.filter(username=username)
        if not users.exists():
            return Response({"error": "Username not found"}, status=status.HTTP_404_NOT_FOUND)

        items = Item.objects
        if not items.exists():
            return Response({"error": "Username not found"}, status=status.HTTP_404_NOT_FOUND)

        user = users.first()
        item = items.first()

        # UserItem
        items = UserCartItem.objects.filter(user=user, item=item)

        if items.exists():
            return Response({"message": "Has been added to cart"}, status=status.HTTP_200_OK)

        # item does not exist
        else:
            cart_item = UserCartItem(user=user, item=item)
            cart_item.save()

        updated_cart_items = UserCartItem.objects.filter(user=user)

        return Response({"cart-items": updated_cart_items}, status=status.HTTP_200_OK)
