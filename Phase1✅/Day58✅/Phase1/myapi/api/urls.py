from django.urls import path
from .views import product_create,product_detail

urlpatterns = [
    path('products/',product_create),
    path('products/<int:pk>',product_detail)
]
