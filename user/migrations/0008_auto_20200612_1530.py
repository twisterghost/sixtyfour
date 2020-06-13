# Generated by Django 3.0.7 on 2020-06-12 20:30

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20200612_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, max_length=128, upload_to=user.models.user_avatar_path),
        ),
        migrations.AlterField(
            model_name='profile',
            name='banner',
            field=models.ImageField(blank=True, max_length=128, upload_to=user.models.user_banner_path),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile',
            field=models.TextField(blank=True),
        ),
    ]
