# Generated by Django 5.1 on 2024-08-26 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_name_customuser_tel_customuser_uid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='tel',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='uid',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
