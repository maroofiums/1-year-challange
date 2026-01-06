from django.db import connection
from django.shortcuts import render

def home(request):
    from .models import Product
    products = Product.objects.all()
    print("Queries:", len(connection.queries))  # optional
    return render(request, 'home.html', {'products': products})
