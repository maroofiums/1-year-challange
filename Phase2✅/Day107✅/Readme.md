# Day 107


---

## 🚀 Django REST Framework (CRUD APIs) – Full Code

We'll create an API for a model called `Product` with full CRUD operations.

---

### ✅ Step 1: Install DRF

```bash
pip install djangorestframework
```

Add to `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'your_app_name',
]
```

---

### ✅ Step 2: Create the Model

**`models.py`**

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### ✅ Step 3: Create the Serializer

**`serializers.py`**

```python
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
```

---

### ✅ Step 4: Create the API Views (CRUD)

You have 3 options: **Function-Based Views (FBV)**, **Class-Based Views (CBV)**, or **ViewSets**.

Let’s use **Class-Based Generic Views (CBV)** for clarity.

**`views.py`**

```python
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

# List & Create
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Retrieve, Update & Delete
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

---

### ✅ Step 5: Configure URLs

**`urls.py` in your app**

```python
from django.urls import path
from .views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
]
```

**`urls.py` in your main project**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('your_app_name.urls')),  # your app url
]
```

---

### ✅ API Endpoints

| Method | Endpoint           | Action         |
| ------ | ------------------ | -------------- |
| GET    | `/api/products/`   | List products  |
| POST   | `/api/products/`   | Create product |
| GET    | `/api/products/1/` | Retrieve       |
| PUT    | `/api/products/1/` | Update         |
| DELETE | `/api/products/1/` | Delete         |

---

### ✅ Bonus: Test API

Use **Postman**, **curl**, or **DRF’s built-in browsable API** at:

```
http://127.0.0.1:8000/api/products/
```

---

Would you like:

* 💡 ViewSets + Routers version?
* 🔐 JWT authentication with this?
* 🧪 Unit testing for the API?
* ✅ Swagger API docs?

