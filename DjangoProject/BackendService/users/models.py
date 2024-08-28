from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    email = models.CharField(max_length=255, default="", null=True, blank=True)
    uid = models.CharField(max_length=255, unique=True, blank=False)
    name = models.CharField(max_length=255, default="Unknown")
    tel = models.CharField(max_length=11, unique=True, default='', null=True, blank=True)
    address = models.CharField(max_length=255, default='', null=True, blank=True)

    def __str__(self):
        return self.username