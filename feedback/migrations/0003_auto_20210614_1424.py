# Generated by Django 3.1 on 2021-06-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20210613_1309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'ordering': ['-likes'], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterField(
            model_name='reviews',
            name='text',
            field=models.TextField(max_length=5000, verbose_name='Текст'),
        ),
    ]
