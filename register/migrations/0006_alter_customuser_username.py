# Generated by Django 4.2.3 on 2023-07-22 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_customuser_date_joined_customuser_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=255, unique=True, verbose_name='username'),
        ),
    ]
