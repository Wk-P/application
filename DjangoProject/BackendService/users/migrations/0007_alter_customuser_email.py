# Generated by Django 5.1 on 2024-08-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customuser_email_alter_customuser_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.CharField(default='', max_length=255),
        ),
    ]
