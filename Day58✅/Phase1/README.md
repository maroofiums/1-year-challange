Bohat khoob Maroof bhai! 🔥
Ab chalo **REST API ka poora code implementation** karte hain — **line by line**, **samajh ke**, aur **professional style** mein.
Hum bana rahe hain:
🎯 **Product API using Django REST Framework (DRF)**

---

## 🗂 Folder Structure:

```
myapi/                 ← Django Project
│
├── api/               ← App (Product API yahan banegi)
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py      ← Product model
│   ├── serializers.py ← DRF serializer
│   ├── views.py       ← API views
│   └── urls.py        ← App-specific URLs
│
├── myapi/             ← Main project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py        ← Root URLConf
│   └── wsgi.py
│
└── manage.py
```

---

## 🧱 Step-by-Step Implementation

---

### 🧩 Step 1: Install & Setup Project

```bash
pip install django djangorestframework
django-admin startproject myapi
cd myapi
python manage.py startapp api
```

---

### ⚙️ Step 2: settings.py me add karo

```python
# myapi/settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'api',
]
```

---

### 🧠 Step 3: Create Product Model

```python
# api/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name
```

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 🪄 Step 4: Create Serializer

```python
# api/serializers.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
```

---

### 🧠 Step 5: API Views (Function-Based Views)

```python
# api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET', 'POST'])
def product_list_create(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == 'DELETE':
        product.delete()
        return Response({"message": "Product deleted successfully"})
```

---

### 🛣️ Step 6: Setup URLs

```python
# api/urls.py
from django.urls import path
from .views import product_list_create, product_detail

urlpatterns = [
    path('products/', product_list_create),
    path('products/<int:pk>/', product_detail),
]
```

```python
# myapi/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
```

---

## 🚀 Step 7: Run & Test

```bash
python manage.py runserver
```

Now test API using browser or Postman:

### Example Endpoints:

| Method | URL                | Action             |
| ------ | ------------------ | ------------------ |
| GET    | `/api/products/`   | List all products  |
| POST   | `/api/products/`   | Create new product |
| GET    | `/api/products/1/` | Get product by ID  |
| PUT    | `/api/products/1/` | Update product     |
| DELETE | `/api/products/1/` | Delete product     |

---

## 🧪 Sample JSON for POST:

```json
{
  "name": "Ice Cream",
  "price": 250
}
```

---

## ✅ Phase 1 Completed 💥

Tum ne ab banaliya:

* Fully working Django REST API
* CRUD operations
* JSON input/output support
* Professional coding pattern

---

### 🔐 Ready for Phase 2? JWT Auth?

Tum bolo bhai:

* JWT Auth start karun?
* Ya Phase 1 me aur koi doubt hai?

Main yahin hoon, tumhare sath step-by-step. 💯
