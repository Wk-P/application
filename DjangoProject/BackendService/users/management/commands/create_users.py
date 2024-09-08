# ~/application/DjangoProject/BackendService/users/management/commands/createadmin.py
from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth import get_user_model
import uuid

class Command(BaseCommand):
    help = 'Create a superuser with predefined credentials'

    def handle(self, *args, **options):
        User = get_user_model()  # 获取自定义用户模型
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin010',
                uid = str(uuid.uuid4()).replace('-', ''),
                address = "",
                tel = "",
            )
            self.stdout.write(self.style.SUCCESS('Superuser "admin" created with password "admin010"'))
        else:
            self.stdout.write(self.style.WARNING('Superuser "admin" already exists'))

        # 创建 test 用户
        if not User.objects.filter(username='test').exists():
            User.objects.create_user(
                username='test',
                email='test@example.com',
                password='Test010',
                uid=str(uuid.uuid4()).replace('-', ''),
                address='',
                tel='01012345678',
            )
            self.stdout.write(self.style.SUCCESS('User "test" created with password "test010"'))
        else:
            self.stdout.write(self.style.WARNING('User "test" already exists'))