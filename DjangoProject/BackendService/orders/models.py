from django.db import models
from items.models import Item
from users.models import CustomUser

# Create your models here.
class Order(models.Model):
    order_id = models.CharField(default="", max_length=255)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    total_price = models.DecimalField(max_digits=20, decimal_places=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.order_id} - {self.item.name} ({self.quantity} units)"