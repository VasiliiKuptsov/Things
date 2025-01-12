from django.core.management.base import BaseCommand
from products.models import Category, Product

class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        category, _ = Category.objects.get_or_create(name='крупы', description='с полей')

        products = [
            {'name': 'Греча', 'description': 'диетическая', 'category': category},
            {'name': 'Овсянка', 'description': 'детская', 'category': category},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))