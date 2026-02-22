from django.shortcuts import render,redirect
from .models import Product

# Create your views here.

def list_products(request):
    products = Product.objects.all()
    return render(request, 'myapp/list_products.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'myapp/product_detail.html', {'product': product})

def create_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        Product.objects.create(name=name, price=price, description=description)
        return redirect('list_products')    
    return render(request, 'myapp/create_product.html')

def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.description = request.POST['description']
        product.save()
        return redirect('product_detail', product_id=product.id)
    return render(request, 'myapp/update_product.html', {'product': product})

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
    return render(request, 'myapp/delete_product.html', {'product': product})
