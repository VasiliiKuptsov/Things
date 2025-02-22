from django.core.cache import cache
from config.settings import CACHE_ENABLED
from products.models import Product

def get_products_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    product = cache.get(key)
    if product is not None:
        return product
    product = Product.objects.all()
    cache.set(key, product)
    return product
