# Generated by Django 5.0.6 on 2024-06-10 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_user_profile_avatar_user_profile_bio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='name',
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]