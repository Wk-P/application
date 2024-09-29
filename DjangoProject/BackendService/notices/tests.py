from django.test import TestCase
from users.models import CustomUser
from users.models import CustomUserSerializer

class CustomUserSerializerTest(TestCase):
    def setUp(self):
        # 创建一个测试用户
        self.user = CustomUser.objects.create(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )

    def test_custom_user_serializer(self):
        # 序列化用户对象
        serializer = CustomUserSerializer(self.user)
        # 打印序列化的数据
        print(serializer.data)
        
        # 断言序列化的数据是否包含期望的字段和值
        self.assertEqual(serializer.data['username'], 'testuser')
        self.assertEqual(serializer.data['email'], 'testuser@example.com')
