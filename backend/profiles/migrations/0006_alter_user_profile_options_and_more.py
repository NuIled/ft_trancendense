# Generated by Django 4.2.14 on 2024-07-17 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_user_profile_is_valid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_profile',
            options={},
        ),
        migrations.AlterModelManagers(
            name='user_profile',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='is_superuser',
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
