

from django.urls import path
from products.apps import ProductsConfig
from products.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductCategoryListView, ProductsSearchView


app_name = ProductsConfig.name

urlpatterns = [

    path('', ProductListView.as_view(), name = 'products_list'),
    path('products_category/', ProductCategoryListView.as_view(), name = 'products_category'),
    path("products_search/", ProductsSearchView.as_view(),name="products_search"),
    path('products/<int:pk>/', ProductDetailView.as_view(), name = 'products_detail'),
    path('products/create', ProductCreateView.as_view(), name='products_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='products_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='products_delete')

]












