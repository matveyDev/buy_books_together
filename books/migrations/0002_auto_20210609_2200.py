# Generated by Django 3.1 on 2021-06-09 22:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksforbuy',
            name='buyers',
            field=models.ManyToManyField(blank=True, related_name='books_for_buy', to=settings.AUTH_USER_MODEL, verbose_name='Покупатель'),
        ),
    ]
