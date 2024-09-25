from django.db import models
from users.models import CustomUser, CustomUserSerializer
from rest_framework import serializers
from pathlib import Path
import os

# Create your models here.
# 商品字段


class Item(models.Model):
    name = models.CharField(default="Noname", max_length=255)
    brand = models.CharField(default='Unknown', max_length=255)
    desc = models.TextField(default=None)
    price = models.BigIntegerField(default=0)
    title = models.CharField(default='Notitle', max_length=255)
    class_name = models.CharField(default='Unknown', max_length=255)

    def __str__(self):
        return self.name

# 商品对应图片
class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')  # 关联到 Item
    image = models.ImageField(upload_to='item_img/')

    def delete(self, *args, **kwargs):
        if self.image:
            image_path = self.image.path
            if os.path.isfile(os.path.normpath(image_path)):
                os.remove(os.path.normpath(image_path))
        super(ItemImage, self).delete(*args, **kwargs)

    def __str__(self):
        return f"Image for {self.item.name}"

    def delete(self, *args, **kwargs):
        if self.image:
            image_path = self.image.path
            if os.path.isfile(os.path.normpath(image_path)):
                os.remove(os.path.normpath(image_path))
        super(Item, self).delete(*args, **kwargs)


class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ['image']


# 序列化商品字段

class ItemSerializer(serializers.ModelSerializer):
    images = ItemImageSerializer(many=True, read_only=True)  # 添加关联图片的序列化

    class Meta:
        model = Item
        fields = ['id', 'name', 'desc', 'price', 'brand', 'title', 'class_name', 'images']  # 包含 images 字段


# 用户购物车商品字段
class UserCartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.BigIntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'item'], name='unique_user_item')
        ]


# 序列化用户购物车商品字段
class UserCartItemSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    item = ItemSerializer()

    class Meta:
        model = UserCartItem
        fields = ['user', 'item']
