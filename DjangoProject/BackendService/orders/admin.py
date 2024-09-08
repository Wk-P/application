from django.contrib import admin
from orders.models import Order

# Register your models here.
# Register your models here.
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'item', 'order_id', 'quantity', 'total_price')  # 在列表页面显示的字段
    search_fields = ('id', 'order_id', 'quantity', 'total_price')  # 可以搜索的字段
    list_filter = ('id', 'order_id', 'quantity', 'total_price')  # 过滤器

admin.site.register(Order, OrderModelAdmin)