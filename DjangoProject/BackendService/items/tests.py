from django.test import TestCase
from items.models import Item, ItemImage
from django.conf import settings
from django.core.files import File
from pathlib import Path
# Create your tests here.

class TestCaseAPPDIR(TestCase):
    def test_app_dir_exists(self):
        item_name = 'name1' 
        new_item = Item.objects.create(
                name=item_name,
                brand='BrandX',  # 你可以自定义品牌名称
                desc='This is a description of item1.',
                price=1000,  # 商品价格
                title='Item1 Title',
                class_name='ClassA'  # 类别名称
            )

        # 使用 pathlib.Path 处理路径拼接
        media_dir_path = Path(settings.MEDIA_ROOT)  # MEDIA_ROOT 的根目录
        sub_dir_path = Path('test_img/img2.png')
        image_path = media_dir_path / 'test_img' / 'img2.png'  # 目标图片路径

        # 检查路径是否存在，并处理图片文件
        if image_path.exists():
            with image_path.open('rb') as f:
                try:
                    image_file = File(f)

                    # create function
                    image_file.name = sub_dir_path
                    ItemImage.objects.create(item=new_item, image=image_file)
                    
                    # save function
                    # item_image = ItemImage(item=new_item)
                    # item_image.image.save(item_name, image_file)
                    # item_image.save()
                    print("Create success")
                except Exception as e:
                    print(e)
                    # print(image_path)
        else:
            print(f"Image file does not exist at: {image_path}")
       
