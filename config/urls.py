from django.contrib import admin
from django.urls import path, include
from django.conf import settings
#from catalog import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("products.urls", namespace="products")),
    # path('products/', views.contacts, name='contact'),
    # Путь напрямую с главной страницы home
    # т.к. предложенные нам страницы home и contacts одинаковые
    # path('catalog/', include('catalog.urls', namespace='catalog'))
]
