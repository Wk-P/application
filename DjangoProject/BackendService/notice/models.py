from django.db import models
from users.models import CustomUser, CustomUserSerializer
from rest_framework import serializers

# Create your models here.
class Notice(models.Model):
    title = models.TextField(default='Untitled')
    content = models.TextField(default='No content')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class NoticeSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d')
    updated_at = serializers.DateTimeField(format='%Y-%m-%d')
    class Meta:
        model = Notice
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']


class UserComment(models.Model):
    content = models.TextField(default='')
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserCommentSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer()
    notice = NoticeSerializer()
    
    class Meta:
        model = UserComment
        fields = ['id', 'notice', 'author', 'content', 'created_at', 'updated_at']