from .views import list_products, product_detail, create_product, update_product, delete_product
from django.urls import path

urlpatterns = [
    path('products/', list_products, name='list_products'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('products/create/', create_product, name='create_product'),
    path('products/<int:product_id>/update/', update_product, name='update_product'),
    path('products/<int:product_id>/delete/', delete_product, name='delete_product'),
]