# Generated by Django 4.2.5 on 2025-02-16 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='publication',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
    ]
