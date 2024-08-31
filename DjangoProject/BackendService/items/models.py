from django.db import models
from users.models import CustomUser

# Create your models here.
class Item(models.Model):
    name = models.CharField(default="noname", max_length=255)
    desc = models.TextField(default=None)
    price = models.BigIntegerField(default=0)
    title = models.CharField(default='notitle', max_length=255)
    def __str__(self):
        return self.name

class UserCartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)