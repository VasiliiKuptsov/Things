from products.models import Category, Product


def get_product_from_category(category_id):
    print(category_id)
    #category = Category.objects.filter(name=name)
    #products = Product.objects.filter(category=category)
    return Product.objects.filter(category_id=category_id)