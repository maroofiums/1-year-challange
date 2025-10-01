# Day 121

## 🧩 1. Django Middleware

### 🔹 What is Middleware?

Middleware is a **lightweight plugin** that processes **requests and responses** globally **before** views or **after** views run.

### 🔧 Common Use Cases:

* Authentication (e.g., user session check)
* Logging
* Modifying requests/responses
* Caching
* Custom security checks

---

### ✅ How Middleware Works (Lifecycle):

1. `Request` comes in
2. Django passes the request through each middleware in order
3. View is called
4. Response is passed through middleware in **reverse order**

---

### 🔨 Example: Custom Middleware

**`middleware.py`**

```python
from django.utils.deprecation import MiddlewareMixin

class SimpleLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f"User accessed: {request.path}")

    def process_response(self, request, response):
        print("Response status:", response.status_code)
        return response
```

### 🔗 Enable it in `settings.py`:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    ...
    'myapp.middleware.SimpleLogMiddleware',
]
```

---

## 🚀 2. Django Caching

### 🔹 What is Caching?

Caching means storing **expensive computations or database results** temporarily so future requests are faster.

---

### ✅ Types of Caching in Django:

| Type                    | Description                                       |
| ----------------------- | ------------------------------------------------- |
| **Per-site cache**      | Cache entire site                                 |
| **Per-view cache**      | Cache specific views                              |
| **Template fragment**   | Cache a portion of template                       |
| **Low-level cache API** | Manual key-value caching (e.g., Redis, Memcached) |

---

### 🔧 1. Per-view Caching

**views.py**

```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)  # cache for 15 minutes
def my_view(request):
    return render(request, 'my_template.html')
```

---

### 🔧 2. Template Fragment Caching

**template.html**

```django
{% load cache %}
{% cache 600 sidebar %}
    {% include "sidebar.html" %}
{% endcache %}
```

---

### 🔧 3. Low-Level Caching (Manual)

**views.py**

```python
from django.core.cache import cache

def expensive_view(request):
    data = cache.get('expensive_data')
    if not data:
        data = compute_heavy_data()
        cache.set('expensive_data', data, timeout=60 * 10)
    return JsonResponse(data)
```

---

### 🔧 Setup Cache Backend in `settings.py`:

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',  # For testing
        'LOCATION': 'unique-snowflake',
    }
}
```

✅ You can also use Redis or Memcached:

```python
# Redis Example
'BACKEND': 'django_redis.cache.RedisCache',
'LOCATION': 'redis://127.0.0.1:6379/1',
```

---

## 🔁 Middleware + Caching Together?

Yes! Middleware like `UpdateCacheMiddleware` and `FetchFromCacheMiddleware` can be used to implement **site-wide caching**.

**settings.py**

```python
MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    ...
    'django.middleware.cache.FetchFromCacheMiddleware',
]
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_ALIAS = 'default'
```

---

## 🧠 Summary

| Feature        | Use it when...                              |
| -------------- | ------------------------------------------- |
| Middleware     | You need global request/response processing |
| View Cache     | You want to cache whole view results        |
| Fragment Cache | Part of the page is expensive to render     |
| Low-level      | You want full control over caching logic    |

---
