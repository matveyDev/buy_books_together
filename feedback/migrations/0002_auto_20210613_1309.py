# Generated by Django 3.1 on 2021-06-13 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='feedback.reviews', verbose_name='Родитель'),
        ),
    ]
