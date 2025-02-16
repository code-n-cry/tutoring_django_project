# Generated by Django 3.2.17 on 2025-02-16 21:24

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=user.models.avatar_image_path,
                verbose_name='Аватарка',
            ),
        ),
    ]
