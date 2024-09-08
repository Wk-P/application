from django.db import models
from users.models import CustomUser
from rest_framework import serializers
from pathlib import Path
import platform

# Create your models here.
class Item(models.Model):
    name = models.CharField(default="noname", max_length=255)
    desc = models.TextField(default=None)
    price = models.BigIntegerField(default=0)
    title = models.CharField(default='notitle', max_length=255)
    filename = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        # 根据平台设置默认的 urlLink
        if not self.filename:  # 只有当 urlLink 为空时才设置
            system = platform.system()
            if system == 'Windows':
                self.urlLink = str(Path.cwd() / 'VueProject' / 'public' / 'item_img' / {self.filename})
            elif system == 'Linux':
                self.urlLink = str(Path.cwd() / 'VueProject' / 'public' / 'item_img' / {self.filename})
            else:
                # 如果平台不在支持的范围内，抛出异常以阻止保存
                raise ValueError("Unsupported platform: " + system)

        # 调用父类的 save 方法以完成实际的保存操作
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'desc', 'price', 'title', 'filename']



class UserCartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.BigIntegerField(default=0)