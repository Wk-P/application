from django.contrib import admin
from items.models import Item, UserCartItem, ItemImage, UserFavoriteItem, RecommendItem, HotBrand

class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 1

class ItemModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'price')
    search_fields = ('name', 'price')
    list_filter = ('name', 'price')
    inlines = [ItemImageInline]

class UserItemModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'item')
    search_fields = ('item__name', 'user__username')  # 外键字段，通过双下划线访问 item 模型的 name 字段
    list_filter = ('item__name',)    # 过滤条件同样通过双下划线访问外键字段

class HotBrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)
    search_fields = ('brand_name',)
    list_filter = ('brand_name',)


@admin.register(RecommendItem)
class RecommendItemAdmin(admin.ModelAdmin):
    list_display = ('item',)  # 显示 item 字段

# 正确注册模型与管理类
admin.site.register(Item, ItemModelAdmin)        # 注册 Item 模型及其管理类
admin.site.register(UserCartItem, UserItemModelAdmin)  # 注册 UserCartItem 模型及其管理类
admin.site.register(UserFavoriteItem, UserItemModelAdmin)
admin.site.register(HotBrand, HotBrandAdmin)