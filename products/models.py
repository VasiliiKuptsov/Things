from django.db import models
from users.models import User
class Category(models.Model):

    name = models.CharField(
        max_length=200,
        verbose_name="наименование категории",
        help_text="введите название категории",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="описание категории",
        help_text="опишите категорию",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:

        verbose_name = "Категория"
        verbose_name_plural = "Категории"



class Product(models.Model):

    name = models.CharField(
        max_length=200,
        verbose_name="наименование",
        help_text="введите название продукта",
    )

    description = models.TextField(
        blank=True, null=True, verbose_name="описание", help_text="опищите продукт",
    )
    image = models.ImageField(
        upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="изображение",
        help_text="введите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="категория",
        help_text="введите категорию продукта",
        blank=True,
        null=True,
        related_name='products',
    )

    price = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="цена за покупку",
        help_text="укахите цену продукта",
    )

    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="дата последнего изменения",
        help_text="введите последнего изменения продукта",
    )

    views_counter = models.PositiveIntegerField(
        verbose_name='Счетчик просмотров',
        help_text='Укахите количество просмотров',
        default=0,
    )
    
    owner = models.ForeignKey(
        User,
        verbose_name='Купец',
        help_text='Укажите продавца товараэ',
        blank=True, null=True,
        on_delete=models.SET_NULL,
    )


    publication = models.BooleanField(
        default=False, 
        verbose_name='Опубликовано',
    )
    
    def __str__(self):
        return f"{self.name}({self.category}){self.price}"

    class Meta:

        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]
        db_table = "custom_table_name"
        managed=True
        permissions =[
            ("can_publication_product", "Can publication product"),
            ("can_delete_product", "Can delete product"),
        ]


