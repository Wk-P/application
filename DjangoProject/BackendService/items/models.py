from django.db import models
from users.models import CustomUser

# Create your models here.
class Item(models.Model):
    name = models.TextField(default="noname", max_length=255)
    desc = models.TextField(default=None, max_length=2048)
    price = models.BigIntegerField(default=0)

    def __str__(self):
        return self.name

class UserItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    is_cart = models.BooleanField(default=False)
    is_favorate = models.BooleanField(default=False)