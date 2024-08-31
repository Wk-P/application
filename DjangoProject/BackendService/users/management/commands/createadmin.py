# ~/application/DjangoProject/BackendService/users/management/commands/createadmin.py
from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a superuser with predefined credentials'

    def handle(self, *args, **options):
        User = get_user_model()  # 获取自定义用户模型
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin010'
            )
            self.stdout.write(self.style.SUCCESS('Superuser "admin" created with password "admin010"'))
        else:
            self.stdout.write(self.style.WARNING('Superuser "admin" already exists'))
