# Generated by Django 4.2.3 on 2023-07-22 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_remove_customuser_address_remove_customuser_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_staff',
        ),
    ]