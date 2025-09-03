# Day156

## **Django ViewSets**.

---

### 🚀 Why use a ViewSet?

* Less boilerplate code
* Organizes related views together
* Works great with DRF **Routers** (automatic URL generation)

---

### 🔑 Basic Example

```python
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

Here:

* `ModelViewSet` gives you **list, retrieve, create, update, partial\_update, and destroy** out of the box.
* You only specify the `queryset` and `serializer_class`.

---

### ⚡ Router Setup (urls.py)

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

👉 This automatically generates routes like:

* `GET /books/` → list
* `POST /books/` → create
* `GET /books/{id}/` → retrieve
* `PUT /books/{id}/` → update
* `PATCH /books/{id}/` → partial update
* `DELETE /books/{id}/` → destroy

---

### 🔧 Types of ViewSets

* `ViewSet` → Base class, you must define actions manually.
* `GenericViewSet` → Adds DRF’s mixin support (e.g. `ListModelMixin`, `CreateModelMixin`).
* `ModelViewSet` → Combines `GenericViewSet` with all CRUD mixins.

---

### 🎯 Custom Action Example

```python
from rest_framework.decorators import action
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['get'])
    def details(self, request, pk=None):
        book = self.get_object()
        return Response({"title": book.title, "author": book.author})
```

This adds a custom endpoint:

* `GET /books/{id}/details/`

---

👉 Do you want me to show you how to **build a ViewSet manually** (without `ModelViewSet`), so you can see what’s happening under the hood?
