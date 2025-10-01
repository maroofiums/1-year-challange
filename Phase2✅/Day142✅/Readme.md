# Day142

---

## 1. Install Django & DRF

```bash
pip install django djangorestframework
```

---

## 2. Create a Project & App

```bash
django-admin startproject library
cd library
python manage.py startapp books
```

Add `rest_framework` and `books` to `INSTALLED_APPS` in `library/settings.py`.

---

## 3. Define a Model (`books/models.py`)

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 4. Create a Serializer (`books/serializers.py`)

```python
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
```

---

## 5. Create Views (`books/views.py`)

```python
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

---

## 6. Add Routes (`books/urls.py`)

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

Include it in the main project’s `urls.py` (`library/urls.py`):

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books.urls')),
]
```

---

## 7. Test the API

Run server:

```bash
python manage.py runserver
```

APIs available:

* **List Books** → `GET /api/books/`
* **Retrieve Book** → `GET /api/books/{id}/`
* **Create Book** → `POST /api/books/`
* **Update Book** → `PUT /api/books/{id}/`
* **Partial Update** → `PATCH /api/books/{id}/`
* **Delete Book** → `DELETE /api/books/{id}/`

---

⚡ Boom! You now have fully functional CRUD APIs with DRF.

---
