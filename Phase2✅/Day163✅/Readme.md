# **Day163**

---

## 🔹 Django Middleware

Middleware in Django is like a pipeline of hooks that process **requests and responses** before they hit your views or after they leave them.

### How Middleware Works

Each request goes through this sequence:

1. **Request comes in →** middleware chain processes it (top to bottom in `MIDDLEWARE` setting).
2. **View executes →** returns response.
3. **Response goes out →** middleware processes it again (bottom to top).

### Middleware Example

Say you want to log request times:

```python
import time
from django.utils.deprecation import MiddlewareMixin

class SimpleLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):
        duration = time.time() - request.start_time
        print(f"{request.path} took {duration:.2f}s")
        return response
```

Then register it in `settings.py`:

```python
MIDDLEWARE = [
    ...,
    "myapp.middleware.SimpleLogMiddleware",
]
```

👉 Middleware use cases:

* Authentication
* CSRF protection
* Caching
* Request logging
* Security headers

---

## 🔹 Django Caching

Caching speeds up Django apps by storing **expensive results** (DB queries, rendered templates, or even full responses).

### Cache Backends Django Supports

* **In-memory** (default, for dev)
* **File-based**
* **Database caching**
* **Memcached / Redis** (best for production)

### Levels of Caching

1. **Per-view caching**

   ```python
   from django.views.decorators.cache import cache_page

   @cache_page(60 * 15)  # cache for 15 minutes
   def my_view(request):
       ...
   ```

2. **Template fragment caching**

   ```django
   {% load cache %}
   {% cache 600 sidebar %}
       <!-- expensive sidebar HTML -->
   {% endcache %}
   ```

3. **Low-level caching (manual)**

   ```python
   from django.core.cache import cache

   def my_view(request):
       data = cache.get("my_key")
       if not data:
           data = expensive_function()
           cache.set("my_key", data, 300)  # 5 minutes
       return JsonResponse({"data": data})
   ```

4. **Per-site caching** (cache entire pages)
   Add to `settings.py`:

   ```python
   MIDDLEWARE = [
       "django.middleware.cache.UpdateCacheMiddleware",
       ...,
       "django.middleware.cache.FetchFromCacheMiddleware",
   ]
   CACHE_MIDDLEWARE_SECONDS = 600
   ```

---

## 🔑 Big Picture

* **Middleware = intercept request/response → modify, check, or log**
* **Caching = store results → avoid recomputing/rendering**
* They can work together (e.g., cache middleware stores responses globally).

---

