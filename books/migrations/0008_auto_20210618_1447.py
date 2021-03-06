# Generated by Django 3.1 on 2021-06-18 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_remove_booksforfree_book_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksforbuy',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=255, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='booksforfree',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=255, null=True, unique=True, verbose_name='URL'),
        ),
    ]
