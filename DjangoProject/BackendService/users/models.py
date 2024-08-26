from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    email = models.CharField(max_length=255, default="")
    uid = models.CharField(max_length=255, unique=True, blank=False)
    name = models.CharField(max_length=255, default="Unknown")
    tel = models.CharField(max_length=11, unique=True, default='')

    def __str__(self):
        return self.username