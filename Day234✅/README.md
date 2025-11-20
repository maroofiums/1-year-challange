# Day 234

---

## 🧪 Django Unit Testing & Debugging

### 🔹 Unit Testing Overview

* Django ka built-in testing framework `unittest` pe based hai.
* Har Django app ke andar `tests.py` file hoti hai.
* Commands:

  ```bash
  python manage.py test
  ```
* Django automatically test database create karta hai, run karta hai, aur destroy karta hai after tests.

### 🔹 Example Test Case

```python
from django.test import TestCase
from django.urls import reverse
from .models import Product

class ProductViewTests(TestCase):
    def setUp(self):
        Product.objects.create(name="Laptop", price=1000)

    def test_homepage_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_shows_product(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, "Laptop")
```

**Common Errors:**

* `NameError: reverse not defined` → Fix: `from django.urls import reverse`
* `NoReverseMatch: 'home' not found` → Fix: URL name 'home' missing in urls.py

---

### 🐞 Debugging Tools

#### 🔸 Django Debug Toolbar

* Helps inspect SQL queries, cache, templates, request data, etc.
* Install:

  ```bash
  pip install django-debug-toolbar
  ```
* Add in `INSTALLED_APPS`, `MIDDLEWARE`, and `urls.py`:

  ```python
  path('__debug__/', include('debug_toolbar.urls')),
  ```
* Only works in `DEBUG=True` mode.

#### 🔸 Best Practices

* Run tests regularly before pushing code.
* Use toolbar to detect slow queries or missing indexes.
* Combine with `assertQuerysetEqual` or `assertContains` to verify templates and responses.

---

### ✅ Summary

| Topic         | Key Point                              |
| ------------- | -------------------------------------- |
| Unit Testing  | Automated validation of models & views |
| Debug Toolbar | Live insight into requests & SQL       |
| Debug Mode    | Only for local/dev environment         |
| Errors        | Use clear test names & fixtures        |

---

