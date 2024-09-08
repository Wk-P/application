from rest_framework.response import Response
from rest_framework.views import APIView
from items.models import Item
from rest_framework.request import Request
from rest_framework import status
from users.models import CustomUser, CustomUserSerializer
from items.models import UserCartItem, ItemSerializer
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from pathlib import Path
import platform
from django.core import serializers
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

    def get(self, request: Request, keywords: str):
        print(request)
        if keywords == "all" or keywords == "":
            searchResults = list(Item.objects.all().values())
        else:
            searchResults = self.search(keywords)
        print(searchResults)
        return Response(searchResults)


class ItemFileUpload(APIView):
    # 支持处理多部分表单数据（用于文件上传）和 JSON 数据
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        system = platform.system()

        if system == 'Windows':
            self.directory = Path.cwd() / 'VueProject' / 'public' / 'item_img'
        elif system in ['Linux', 'Darwin']:  # 适用于 Unix 和 macOS
            self.directory = Path.home() / 'application' / 'VueProject' / 'public' / 'item_img'
        else:
            raise NotImplementedError(
                f"Unsupported operating system: {system}")

    def delete(self, request: Request):
        file_name = request.data.get('file_name')  # 从请求中获取文件名
        if not file_name:
            return Response({"error": "File name not provided"}, status=status.HTTP_400_BAD_REQUEST)

        file_path = self.directory / file_name

        if file_path.exists() and file_path.is_file():
            try:
                file_path.unlink()  # 删除文件
                return Response({"message": f"File '{file_name}' deleted successfully!"}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"error": f"File '{file_name}' not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request: Request):
        all_file_names = [
            f.name for f in self.directory.iterdir() if f.is_file()]
        return Response(all_file_names, status=status.HTTP_200_OK)

    def post(self, request: Request, *args, **kwargs):
        uploaded_file = request.FILES.get('file')  # 获取上传的文件
        request_data = request.data.get('')
        if uploaded_file:
            # 使用 pathlib 处理路径
            file_path = self.directory / uploaded_file.name

            # 确保目标目录存在
            self.directory.mkdir(parents=True, exist_ok=True)

            # 保存文件
            try:
                with file_path.open('wb+') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)
                return Response({"message": "File uploaded successfully!", "file_name": uploaded_file.name}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)


class FetchAllCartItems(APIView):
    def get(self, request: Request, username):
        if not username:
            return Response({"error": "Username deficiency"}, status=status.HTTP_204_NO_CONTENT)

        else:
            users = CustomUser.objects.filter(username=username)
            if not users.exists():
                return Response({"error": "Username does not exist"})

            user = users.first()
            items = UserCartItem.objects.filter(user=user)

            serialized_data = []

            user_data = None
            item_data = None

            for item in items:
                user_data = CustomUserSerializer(item.user).data
                item_data = ItemSerializer(item.item).data

            serialized_data.append({
                'user': user_data,
                'item': item_data
            })

        return Response(serialized_data, status=status.HTTP_200_OK)


# add cart items
class ItemAddToCart(APIView):
    def get(self, request):
        return Response({"message": "OK"})

    def post(self, request: Request):
        request_body = request.data
        username = request_body.get('username')
        item_id = request_body.get('item_id')

        print(item_id, username)

        if not username:
            return Response({"error": "Username deficiency"}, status=status.HTTP_204_NO_CONTENT)

        if not item_id:
            return Response({"error": "Itemname deficiency"}, status=status.HTTP_204_NO_CONTENT)

        users = CustomUser.objects.filter(username=username)
        if not users.exists():
            return Response({"error": "Username not found"}, status=status.HTTP_404_NOT_FOUND)

        items = Item.objects.filter(id=item_id)
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

        updated_cart_items = UserCartItem.objects.filter(
            user=user).values()

        return Response({"cart-items": updated_cart_items}, status=status.HTTP_200_OK)


class FetchItemDetails(APIView):
    def get(self, request: Request):
        pass
