from django.db import models
from users.models import CustomUser, CustomUserSerializer
from rest_framework import serializers
from pathlib import Path

# Create your models here.
# 商品字段
class Item(models.Model):
    name = models.CharField(default="noname", max_length=255)
    desc = models.TextField(default=None)
    price = models.BigIntegerField(default=0)
    title = models.CharField(default='notitle', max_length=255)
    image = models.ImageField(upload_to='item_img/', null=True, blank=True)

    def __str__(self):
        return self.name
    
# 序列化商品字段
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'desc', 'price', 'title', 'filename']


# 用户购物车商品字段
class UserCartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.BigIntegerField(default=0)
    


# 序列化用户购物车商品字段
class UserCartItemSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    item = ItemSerializer()

    class Meta:
        model = UserCartItem
        fields = ['user', 'item']