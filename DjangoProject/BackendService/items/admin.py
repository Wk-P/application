from django.contrib import admin
from items.models import Item, UserCartItem, ItemImage, UserFavoriteItem, RecommendItem, HotBrand, OptionName, ItemOption, CartItemOption


class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 1


class ItemOptionInline(admin.TabularInline):
    model = ItemOption
    extra = 1
    autocomplete_fields = ('name',)


class CartItemOptionInline(admin.TabularInline):
    model = CartItemOption
    extra = 1
    autocomplete_fields = ('name',)


@admin.register(ItemOption)
class ItemOptionModelAdmin(admin.ModelAdmin):
    list_display = ('item', 'name', 'value')


@admin.register(Item)
class ItemModelAdmin(admin.ModelAdmin):
    inlines = [ItemOptionInline, ItemImageInline]
    list_display = ('name', 'desc', 'price', 'brand', 'title', 'class_name')
    search_fields = ('name', 'desc', 'price', 'brand', 'title', 'class_name')
    list_filter = ('name', 'desc', 'price', 'brand', 'title', 'class_name')


@admin.register(OptionName)
class OptionNameModelAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(UserCartItem)
class UserCartItemModelAdmin(admin.ModelAdmin):
    inlines = [CartItemOptionInline]
    list_display = ('user', 'item', )
    # 外键字段，通过双下划线访问 item 模型的 name 字段
    search_fields = ('item__name', 'user__username')
    list_filter = ('item__name',)    # 过滤条件同样通过双下划线访问外键字段


@admin.register(UserFavoriteItem)
class UserFavoriteItemModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'item',)
    search_fields = ('item__name', 'user__username')
    list_filter = ('item__name',) 


@admin.register(HotBrand)
class HotBrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)
    search_fields = ('brand_name',)
    list_filter = ('brand_name',)


@admin.register(RecommendItem)
class RecommendItemAdmin(admin.ModelAdmin):
    list_display = ('item',)  # 显示 item 字段
