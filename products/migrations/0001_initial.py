# Generated by Django 4.2.5 on 2025-02-14 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='введите название категории', max_length=200, verbose_name='наименование категории')),
                ('description', models.TextField(blank=True, help_text='опишите категорию', null=True, verbose_name='описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='введите название продукта', max_length=200, verbose_name='наименование')),
                ('description', models.TextField(blank=True, help_text='опищите продукт', null=True, verbose_name='описание')),
                ('image', models.ImageField(blank=True, help_text='введите изображение продукта', null=True, upload_to='products/photo', verbose_name='изображение')),
                ('price', models.IntegerField(blank=True, help_text='укахите цену продукта', null=True, verbose_name='цена за покупку')),
                ('updated_at', models.DateField(blank=True, help_text='введите последнего изменения продукта', null=True, verbose_name='дата последнего изменения')),
                ('views_counter', models.PositiveIntegerField(default=0, help_text='Укахите количество просмотров', verbose_name='Счетчик просмотров')),
                ('category', models.ForeignKey(blank=True, help_text='введите категорию продукта', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'db_table': 'custom_table_name',
                'ordering': ['name'],
            },
        ),
    ]
