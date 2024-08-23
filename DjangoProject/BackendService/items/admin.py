from django.contrib import admin
from items.models import Item

# Register your models here.
class ItemModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'price')  # 在列表页面显示的字段
    search_fields = ('name', 'price')  # 可以搜索的字段
    list_filter = ('name', 'price')  # 过滤器

admin.site.register(Item, ItemModelAdmin)