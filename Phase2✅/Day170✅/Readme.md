## Day170

A **ModelViewSet** in Django REST Framework (DRF) is like the all-in-one bundle you get when you don’t wanna manually wire up every single CRUD endpoint. It ties your **model + serializer + queryset** into one class and automatically gives you routes for:

* `list` (GET all)
* `retrieve` (GET one)
* `create` (POST)
* `update` (PUT/PATCH)
* `destroy` (DELETE)

Basically: one class = full CRUD API, with less boilerplate.

---

### Quick Example 🚀

```python
# views.py
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

```python
# serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
```

```python
# urls.py
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = router.urls
```

Now you’ve got a whole CRUD API at `/books/` without writing extra boilerplate.

---

### When to Use It ✅

* You want **all the CRUD endpoints** out of the box.
* Your API is tightly tied to your model (classic CRUD stuff).

### When NOT to Use It ❌

* If you only need a couple of endpoints (like just list + retrieve), use a `ReadOnlyModelViewSet`.
* If your logic isn’t strictly model-based, go with `APIView` or `GenericViewSet` + mixins for more control.

---