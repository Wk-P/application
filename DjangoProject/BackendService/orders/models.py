from django.db import models
from items.models import Item, ItemSerializer, Option, OptionSerializer
from users.models import CustomUser, CustomUserSerializer
from rest_framework import serializers
from django.core.validators import MinValueValidator

# Create your models here.
# 订单字段


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('unconfirmed', 'Unconfirmed'),
        ('confirmed_not_shipped', 'Confirmed, Not Shipped'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]

    order_id = models.CharField(default="", max_length=255)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    # item option    
    options = models.ManyToManyField(Option, on_delete=models.CASCADE)

    quantity = models.PositiveBigIntegerField(
        default=0, validators=[MinValueValidator(0)])
    total_price = models.DecimalField(max_digits=20, decimal_places=2)

    status = models.CharField(
        max_length=50, choices=ORDER_STATUS_CHOICES, default='unconfirmed'
    )
    # 运单号
    tracking_number = models.CharField(
        max_length=255, blank=True, null=True)  # 运单号

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.order_id} - {self.item.name} ({self.quantity} units)"


# 订单序列化字段
class OrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    user = CustomUserSerializer()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Order
        fields = ['order_id', 'item', 'user', 'quantity', 'total_price',
                  'status', 'tracking_number', 'created_at', 'updated_at']
