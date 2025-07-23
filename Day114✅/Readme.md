# Day114

---

## 🔄 **Django Middleware**

### ✅ What is Middleware?

Middleware in Django is a **layer between the request and response** phases. It lets you **process requests before they reach the view** and **modify responses before they're returned to the client**.

Think of it as a pipeline where each middleware component performs a specific task.

### 📦 Common Built-in Middlewares:

| Middleware                 | Purpose                                 |
| -------------------------- | --------------------------------------- |
| `SecurityMiddleware`       | Adds security headers (HSTS, XSS, etc.) |
| `SessionMiddleware`        | Manages sessions across requests        |
| `AuthenticationMiddleware` | Associates users with requests          |
| `CommonMiddleware`         | Normalizes URLs, adds headers           |
| `CsrfViewMiddleware`       | Protects against CSRF attacks           |
| `MessageMiddleware`        | Supports messaging framework            |

---

### 🛠️ How to Create Custom Middleware

```python
# myapp/middleware.py
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Pre-processing: before view
        print("Before view")
        
        response = self.get_response(request)
        
        # Post-processing: after view
        print("After view")
        return response
```

### 🔗 Add it to `settings.py`

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'myapp.middleware.SimpleMiddleware',  # Add custom middleware here
    ...
]
```

---

## ⚡ **Django Caching**

Caching improves performance by **storing expensive computations, like database queries or template rendering**, so they don’t have to run on every request.

---

### 🚀 Types of Caching in Django:

#### 1. **Per-View Caching**

Cache the output of entire views.

```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)  # Cache for 15 minutes
def my_view(request):
    ...
```

#### 2. **Template Fragment Caching**

Cache parts of templates.

```django
{% load cache %}
{% cache 300 sidebar %}
    ... expensive sidebar HTML ...
{% endcache %}
```

#### 3. **Low-Level Caching (Custom keys)**

Use Django's cache API directly.

```python
from django.core.cache import cache

data = cache.get('my_key')
if not data:
    data = expensive_operation()
    cache.set('my_key', data, timeout=300)
```

---

### 🔧 Cache Backends:

Configure in `settings.py`:

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',  # Default in-memory
        'LOCATION': 'unique-snowflake',
    }
}
```

✅ Other options:

* `FileBasedCache`
* `MemcachedCache`
* `RedisCache` *(best for production)*

---

### 🧪 Useful Cache Utilities:

```bash
# Clear cache
from django.core.cache import cache
cache.clear()
```

---

## 💡 When to Use Middleware vs Caching?

| Use Case                                  | Middleware | Caching |
| ----------------------------------------- | ---------- | ------- |
| Request/response transformation           | ✅ Yes      | ❌ No    |
| User authentication                       | ✅ Yes      | ❌ No    |
| Preventing duplicate expensive DB queries | ❌ No       | ✅ Yes   |
| Security headers, CSRF                    | ✅ Yes      | ❌ No    |
| Reducing template rendering time          | ❌ No       | ✅ Yes   |

---
