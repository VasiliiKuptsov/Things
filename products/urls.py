from django.urls import path
from products.apps import ProductsConfig

# from materials.views import MaterialListView, MaterialCreateView, MaterialDetailView, MaterialUpdateView, MaterialDeleteView

app_name = ProductsConfig.name

urlpatterns = [
    # path('create/', MaterialCreateView.as_view(), name='create'),
    # path('', MaterialListView.as_view(), name='materials'),
    # path('view/<int:pk>/', MaterialDetailView.as_view(), name='view'),
    # path('edit/<int:pk>/', MaterialUpdateView.as_view(), name='edit'),
    # path('delete/<int:pk>/', MaterialDeleteView.as_view(), name='delete'),
]
