from django.contrib.auth.models import AbstractUser
from rest_framework import serializers
from django.db import models

# 地址字段
class Address(models.Model):
    country = models.CharField(
        max_length=255, default='South Korea', null=False, blank=False)
    city = models.CharField(
        max_length=255, default='Seoul', null=False, blank=False)
    street = models.TextField(
        max_length=2048, default='', null=True, blank=True)
    room = models.CharField(max_length=255, default='', null=False, blank=True)
    pcode = models.CharField(
        max_length=255, default='', null=False, blank=False)
    receiver = models.TextField(
        max_length=2048, default='Unknown', null=False, blank=False)

# Create your models here.


# 用户字段
class CustomUser(AbstractUser):
    email = models.CharField(max_length=255, default="", null=True, blank=True)
    uid = models.CharField(max_length=255, unique=True, blank=False)
    name = models.CharField(max_length=255, default="Unknown")
    tel = models.CharField(max_length=11, unique=True,
                           default='', null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


# 地址用户合并字段
class UserAddress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


# 序列化用户字段
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'tel', 'email', 'address', 'id']


# 序列化地址字段
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['country', 'city', 'street', 'room', 'pcode', 'receiver']


# 序列化地址用户合并字段
class UserAddressSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    address = AddressSerializer()

    class Meta:
        model = UserAddress
        fields = ['user', 'address']  # 包含 user 和 address 两个字段
