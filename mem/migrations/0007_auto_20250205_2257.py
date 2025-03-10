# Generated by Django 3.2.17 on 2025-02-05 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mem', '0006_delete_mymodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
    ]
