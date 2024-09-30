# ~/application/DjangoProject/BackendService/items/management/commands/create_item.py
from django.core.management.base import BaseCommand
from items.models import Item, ItemImage
from pathlib import Path
from django.core.files import File
from django.conf import settings


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

            # 创建并关联 ItemImage
            media_dir_path = Path(settings.MEDIA_ROOT)
            sub_dir_path = Path('test_img/img2.png')
            image_path = media_dir_path / 'test_img' / 'img2.png'  # 设置默认图片路径
            if image_path.exists():
                with image_path.open('rb') as f:
                    try:
                        image_file = File(f)
                        image_file.name = sub_dir_path
                        ItemImage.objects.create(item=new_item, image=image_file)
                    except Exception as e:
                        print(e)
                        # print(image_path)
            else:
                print(f"Image file does not exist at: {image_path}")

            self.stdout.write(self.style.SUCCESS(
                f'Item "{item_name}" created successfully'
            ))
        else:
            self.stdout.write(self.style.WARNING(
                f'Item "{item_name}" already exists'
            ))
