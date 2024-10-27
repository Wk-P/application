from django.contrib import admin
from orders.models import Order, OrderItemOption

# Register your models here.
# Register your models here.
class OrderItemOptionInline(admin.TabularInline):
    model = OrderItemOption
    extra = 1
    autocomplete_fields = ('name',)


@admin.register(OrderItemOption)
class ItemOptionModelAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'value')


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    inlines = [OrderItemOptionInline]
    list_display = ('order_id', 'id', 'user', 'item', 'quantity', 'total_price')  # 在列表页面显示的字段
    search_fields = ('order_id', 'id', 'quantity', 'total_price')  # 可以搜索的字段
    list_filter = ('order_id', 'id', 'quantity', 'total_price')  # 过滤器
