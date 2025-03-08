from products.models import Category, Product
from config.settings import CACHE_ENABLED
from django.core.cache import cache

def get_products_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'products_list'  # кэщ включен
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.get(key)
    return products

def get_product_from_category(category_id):

    return Product.objects.filter(category_id=category_id)