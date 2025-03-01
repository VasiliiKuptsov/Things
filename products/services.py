from products.models import Category, Product


def get_product_from_category(category_id):

    return Product.objects.filter(category_id=category_id)