# ~/application/DjangoProject/BackendService/users/management/commands/createadmin.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from users.models import AddressReceiver
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
            )
            self.stdout.write(self.style.SUCCESS(
                f'Superuser "admin" created with password {admin_passowrd}'))
        else:
            self.stdout.write(self.style.WARNING(
                'Superuser "admin" already exists'))

        # 创建 test 用户
        if not User.objects.filter(username='test').exists():
            test_password="Test010"
            test_user = User.objects.create_user(
                username='test',
                email='test@example.com',
                password=test_password,
                uid=str(uuid.uuid4()).replace('-', ''),
                tel='01012345678',
            )
            self.stdout.write(self.style.SUCCESS(
                f'User "test" created with password {test_password}'))
        else:
            self.stdout.write(self.style.WARNING('User "test" already exists'))


        # 创建 address 
        address_text = 'address1'
        receiver_text = 'user1'
        if not AddressReceiver.objects.filter(user=test_user, address=address_text, receiver=receiver_text).exists():
            AddressReceiver.objects.create(user=test_user, address="address1", receiver='user1')
            self.stdout.write(self.style.SUCCESS(
                f"Address: {address_text} Receiver: {receiver_text} created!"
            ))    


