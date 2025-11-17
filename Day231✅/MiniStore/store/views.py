from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem

def get_cart(request):
    session_key = request.session.session_key or request.session.save()
    cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)
    return cart

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'store/product_detail.html', {'product': product})

def add_to_cart(request, id):
    cart = get_cart(request)
    product = get_object_or_404(Product, id=id)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('cart')

def cart_view(request):
    cart = get_cart(request)
    items = CartItem.objects.filter(cart=cart)
    total = sum([item.total_price() for item in items])
    return render(request, 'store/cart.html', {'items': items, 'total': total})

def checkout(request):
    cart = get_cart(request)
    CartItem.objects.filter(cart=cart).delete()  # simple clear
    return render(request, 'store/checkout.html')
