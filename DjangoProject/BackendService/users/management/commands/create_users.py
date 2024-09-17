# ~/application/DjangoProject/BackendService/users/management/commands/createadmin.py
from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth import get_user_model
from users.models import Address
import uuid


class Command(BaseCommand):
    help = 'Create a superuser with predefined credentials'

    def handle(self, *args, **options):
        User = get_user_model()  # 获取自定义用户模型
        if not User.objects.filter(username='admin').exists():
            admin_passowrd="Admin010"
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password=admin_passowrd,
                uid=str(uuid.uuid4()).replace('-', ''),
                address=Address.objects.create(
                    country='South Korea', city='seoul', street='abc 123', room='101', pcode='42444', receiver='admin'),
                tel="",
            )
            self.stdout.write(self.style.SUCCESS(
                f'Superuser "admin" created with password {admin_passowrd}'))
        else:
            self.stdout.write(self.style.WARNING(
                'Superuser "admin" already exists'))

        # 创建 test 用户
        if not User.objects.filter(username='test').exists():
            test_password="Test010"
            User.objects.create_user(
                username='test',
                email='test@example.com',
                password=test_password,
                uid=str(uuid.uuid4()).replace('-', ''),
                address=Address.objects.create(country='South Korea', city='seoul',
                                street='abc 123', room='101', pcode='42444', receiver='test'),
                tel='01012345678',
            )
            self.stdout.write(self.style.SUCCESS(
                f'User "test" created with password {test_password}'))
        else:
            self.stdout.write(self.style.WARNING('User "test" already exists'))
