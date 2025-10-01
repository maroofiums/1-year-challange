# 📘 <u>**Day 177**</u> Django Middleware & Caching 

## 🔹 Middleware

### What is Middleware?

Middleware = ek **layer/filter** jo request aur response ke beech kaam karta hai.
Har request → middleware chain → view → middleware chain → client.

### Why Middleware?

* Global logic add karna without repeating code in views.
* Security, authentication, session management.
* Logging, performance tracking.

### Example: Custom Middleware

```python
# myproject/middleware.py
import time
from django.utils.deprecation import MiddlewareMixin

class SimpleLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()
        print(f"👉 Request URL: {request.path}")

    def process_response(self, request, response):
        duration = time.time() - request.start_time
        print(f"👈 Response Status: {response.status_code}")
        print(f"⚡ Execution Time: {duration:.4f} sec")

        response["X-Custom-Header"] = "MaroofLearning"
        return response
```

### `settings.py`

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    # custom middleware
    'myproject.middleware.SimpleLogMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]
```

---

## 🔹 Caching

### What is Caching?

Caching = **temporary data storage** taake baar-baar DB query ya expensive computation na ho.
Result → fast response 🚀

### Cache Setup (File-based)

```python
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': 'C:/tmp/django_cache',  # change path accordingly
    }
}
```

---

### Types of Caching

#### 1. Per-view cache

```python
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
import time

@cache_page(60)  # cache for 60s
def slow_view(request):
    time.sleep(2)  # heavy computation
    return HttpResponse("This was a slow response ⏳")
```

#### 2. Low-level cache API

```python
from django.core.cache import cache
from django.http import HttpResponse
import time

def cached_data(request):
    data = cache.get("my_data")
    if not data:
        print("⚡ Cache MISS: computing...")
        time.sleep(3)
        data = "Heavy Data Calculated!"
        cache.set("my_data", data, timeout=30)
    else:
        print("✅ Cache HIT: serving from cache")
    return HttpResponse(data)
```

#### 3. Template Fragment Cache

```html
{% load cache %}
{% cache 300 sidebar %}
    {% include "sidebar.html" %}
{% endcache %}
```

---

### `urls.py`

```python
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("slow/", views.slow_view, name="slow"),
    path("cache/", views.cached_data, name="cache"),
]
```

---

## ✅ Test

1. Run server: `python manage.py runserver`
2. Open `/slow/` → first load = slow, second load = instant (cached)
3. Open `/cache/` → first load = cache miss, next loads = cache hit
4. Check console logs for middleware (URL, status, execution time)

---
