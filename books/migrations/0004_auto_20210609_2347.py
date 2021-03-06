# Generated by Django 3.1 on 2021-06-09 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_booksforfree_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksforfree',
            name='book_url',
            field=models.URLField(null=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='booksforfree',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Просмотры'),
        ),
    ]
