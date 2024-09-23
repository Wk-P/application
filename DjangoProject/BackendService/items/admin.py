from django.contrib import admin
from items.models import Item, UserCartItem, UserCartItemSerializer

class ItemModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'price')
    search_fields = ('name', 'price')
    list_filter = ('name', 'price')

class UserItemModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'item')
    search_fields = ('item__name',)  # 外键字段，通过双下划线访问 item 模型的 name 字段
    list_filter = ('item__name',)    # 过滤条件同样通过双下划线访问外键字段

# 正确注册模型与管理类
admin.site.register(Item, ItemModelAdmin)        # 注册 Item 模型及其管理类
admin.site.register(UserCartItem, UserItemModelAdmin)  # 注册 UserCartItem 模型及其管理类
