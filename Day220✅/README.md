# Day 220 -  Django Unit Testing & Debugging

## 1. Introduction

Unit testing aur debugging Django apps mein **code ki quality aur stability** ensure karte hain. Unit tests chhote, independent functions ya views ko test karte hain, taake future changes se bugs na aayein. Debugging se aap **real-time errors** trace kar sakte ho.

> **Tip:** "Test early, fix faster" — jitna pehle test aur debug karoge, utna complex bugs avoid honge.

---

## 2. Setting up Unit Testing in Django

### Step 1: Ensure Django Test Framework Installed

Django by default `unittest` framework provide karta hai. Agar aap custom setup chahte ho:

```bash
pip install pytest pytest-django
```

* `pytest` zyada flexible aur readable hai.
* `pytest-django` Django integration ke liye.

### Step 2: Create a Test File

Project structure example:

```
myapp/
    models.py
    views.py
    tests.py   <-- yahan unit tests likhoge
```

* Django automatically `tests.py` aur `tests/` folder ko recognize karta hai.

---

## 3. Writing Unit Tests

### Example: Model Test

```python
from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title="Python 101", author="Maroof")

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Python 101")
        self.assertEqual(self.book.author, "Maroof")
```

**Step-by-step explanation:**

1. `TestCase` inherit karo — Django test database automatically setup karta hai.
2. `setUp()` — test data create karne ke liye.
3. `test_...` — har test method `test_` se start honi chahiye.
4. `assertEqual()` — expected aur actual value compare karne ke liye.

---

### Example: View Test

```python
from django.urls import reverse
from django.test import TestCase

class HomeViewTest(TestCase):
    def test_home_status_code(self):
        url = reverse('home')  # URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
```

**Tips:**

* `self.client` — simulate HTTP requests without running server.
* Check status code, template, context data.

---

## 4. Running Tests

```bash
python manage.py test
```

* All apps ka `tests.py` detect hota hai.
* Specific app test karne ke liye:

```bash
python manage.py test myapp
```

**Best Practice:**

* Har bug fix ke baad test likho.
* Test naam clear aur descriptive rakho.

---

## 5. Debugging Django Code

### Step 1: Using `print()` (Quick & Dirty)

```python
print(request.user)
```

* Quick but not recommended for production.

### Step 2: Using Python Debugger `pdb`

```python
import pdb; pdb.set_trace()
```

* Execution yahan pause hoti hai aur aap variable inspect kar sakte ho.

### Step 3: Django Logging

```python
import logging
logger = logging.getLogger(__name__)
logger.info("User logged in: %s", request.user)
```

* Production safe, logs maintainable hote hain.

### Step 4: Debug Toolbar

```bash
pip install django-debug-toolbar
```

* SQL queries, templates, headers inspect karne ke liye.

---

## 6. Best Practices

1. **Small & Independent Tests:**
   Har test function ek feature ya logic ko cover kare.
2. **Use `setUpTestData` for Class-level data:**
   Multiple tests ke liye DB hit avoid hota hai.
3. **Clear Test Names:**
   `test_home_view_renders_correct_template` > `test_home`
4. **Test Edge Cases:**
   Null values, invalid inputs, empty queries.
5. **Automate Testing:**
   Git hooks / CI/CD me run karao.

---

## 7. Quick Summary / Tip

* **Test early & often.**
* **Debug smartly:** `pdb` > `print()` > logging > debug toolbar.
* **Follow naming & structure conventions**.
* **Edge cases matter** more than happy-path tests.

> Pro tip: Agar tests fail ho, pehle **test data aur DB isolation** check karo. Most errors yahi se aate hain.

---