# Generated by Django 5.1.3 on 2025-01-05 14:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('mem', '0003_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
