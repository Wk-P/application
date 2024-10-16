from django.contrib import admin
from items.models import Item, UserCartItem, ItemImage, UserFavoriteItem, RecommendItem, HotBrand, Option

class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 1


@admin.register(Item)
class ItemModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'price')
    search_fields = ('name', 'price')
    list_filter = ('name', 'price')
    inlines = [ItemImageInline]


@admin.register(UserCartItem, UserFavoriteItem)
class UserItemModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'item')
    search_fields = ('item__name', 'user__username')  # 外键字段，通过双下划线访问 item 模型的 name 字段
    list_filter = ('item__name',)    # 过滤条件同样通过双下划线访问外键字段


@admin.register(HotBrand)
class HotBrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)
    search_fields = ('brand_name',)
    list_filter = ('brand_name',)


@admin.register(RecommendItem)
class RecommendItemAdmin(admin.ModelAdmin):
    list_display = ('item',)  # 显示 item 字段


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('option_type', 'option_value',)
    search_fields = ('option_type', 'option_value',)
    list_filter = ('option_type', 'option_value',)
