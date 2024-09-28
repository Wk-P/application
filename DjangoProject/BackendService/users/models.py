from django.contrib.auth.models import AbstractUser
from rest_framework import serializers
from django.db import models


# 用户字段
class CustomUser(AbstractUser):
    email = models.CharField(max_length=255, default="", null=True, blank=True)
    uid = models.CharField(max_length=255, unique=True, blank=False)
    name = models.CharField(max_length=255, default="Unknown")
    tel = models.CharField(max_length=11, unique=True,
                           default='', null=True, blank=True)

    def __str__(self):
        return self.username


# 序列化用户字段
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'uid', 'name', 'tel', 'email', 'id']


# 收件人地址字段
class AddressReceiver(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.TextField(blank=False)
    receiver = models.CharField(max_length=255, blank=False, default='')


class AddressReceirSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressReceiver
        fields = ['id', 'user', 'address', 'receiver']
        extra_kwargs = {
            'address': {'required': True}
        }
