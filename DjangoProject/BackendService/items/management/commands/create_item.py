# ~/application/DjangoProject/BackendService/items/management/commands/create_item.py
from django.core.management.base import BaseCommand
from items.models import Item

class Command(BaseCommand):
    help = 'Create an item with predefined credentials'

    def handle(self, *args, **options):
        item_name = 'name1'  # 可以根据需要调整
        if not Item.objects.filter(name=item_name).exists():
            # 创建新的 Item 实例
            new_item = Item.objects.create(
                name=item_name,
                brand='BrandX',  # 你可以自定义品牌名称
                desc='This is a description of item1.',
                price=1000,  # 商品价格
                title='Item1 Title',
                class_name='ClassA'  # 类别名称
            )
            
            self.stdout.write(self.style.SUCCESS(
                f'Item "{item_name}" created successfully'
            ))
        else:
            self.stdout.write(self.style.WARNING(
                f'Item "{item_name}" already exists'
            ))
