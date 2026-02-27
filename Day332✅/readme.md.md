# Django Interview Cheatsheet

> Covers: MVT · ORM · Views · Auth · DRF · Migrations · Caching · Security · Deployment

---

## 01 — Core Concepts

**What is Django and what is its architecture?**
Django is a high-level Python web framework following the **MVT** (Model-View-Template) pattern — similar to MVC but Django's "View" handles logic and "Template" handles presentation. It emphasizes DRY, rapid development, and a batteries-included philosophy.

**What's the Django request/response lifecycle?**
`Request` → Middleware → URL Resolver → View → Template/Serializer → `Response`
Middleware runs for both request and response phases (top-down for request, bottom-up for response).

**What are Django signals?**
Allow decoupled components to get notified of events. Common signals: `pre_save`, `post_save`, `pre_delete`, `post_delete`, `request_started`. Use `@receiver` decorator or `Signal.connect()`.

**Difference between `null=True` and `blank=True`?**
- `null=True` → database level (stores NULL in the column)
- `blank=True` → form/validation level (allows empty input)
- Use both together for optional text fields.

**What is `__str__` and why does it matter?**
Defines the human-readable string representation of a model instance. Used in the Django admin, shell, and anywhere the object is printed/logged.

---

## 02 — ORM & QuerySets

**What is QuerySet lazy evaluation?**
QuerySets are lazy — no DB hit occurs until they are evaluated. A QuerySet is evaluated by: iteration, slicing, `list()`, `bool()`, `len()`, printing, or calling `.get()` / `.count()` / `.first()`.

**`select_related` vs `prefetch_related`?**
- `select_related` → SQL JOIN, for `ForeignKey`/`OneToOne` (single query)
- `prefetch_related` → separate queries + Python join, for `ManyToMany` / reverse FK

```python
# select_related (JOIN — efficient for FK/O2O)
Post.objects.select_related('author').all()

# prefetch_related (separate query — for M2M or reverse FK)
Author.objects.prefetch_related('books').all()
```

**How to avoid N+1 queries?**
Use `select_related()` or `prefetch_related()`. Use `only()` / `defer()` to limit fetched fields. Use `values()` or `values_list()` for raw dicts/tuples when you don't need model instances.

**`F()` and `Q()` objects?**
- `F()` → reference a DB column in queries without fetching it: `F('price') * 1.1`
- `Q()` → complex OR/AND filters: `Q(name='a') | Q(name='b')`

```python
from django.db.models import F, Q

# Update price without fetching the row
Product.objects.update(price=F('price') * 1.1)

# OR filter
Product.objects.filter(Q(stock=0) | Q(discontinued=True))
```

**Useful QuerySet methods to know:**

| Method | Purpose |
|---|---|
| `.filter()` / `.exclude()` | Conditional filtering |
| `.annotate()` | Add computed fields per row |
| `.aggregate()` | Compute a single value across rows |
| `.order_by()` | Sort results |
| `.distinct()` | Remove duplicate rows |
| `.bulk_create()` | Insert many rows in one query |
| `.update()` | Update rows without fetching |
| `.exists()` | Efficient boolean check |
| `.only()` / `.defer()` | Limit fetched columns |

---

## 03 — Views & URLs

**FBV vs CBV — when to use each?**
- **FBV (Function-Based Views):** Simple logic, one-off views, explicit and easy to read.
- **CBV (Class-Based Views):** CRUD operations, reusability, generic views like `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`.

**What is middleware?**
A callable that hooks into Django's request/response processing. Common built-in middleware: `AuthenticationMiddleware`, `SessionMiddleware`, `CsrfViewMiddleware`, `SecurityMiddleware`. Order matters in `settings.MIDDLEWARE`.

**How does Django handle URL routing?**
```python
# urls.py
from django.urls import path, include

urlpatterns = [
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('api/', include('api.urls')),
]
```

**Common view decorators:**

| Decorator | Purpose |
|---|---|
| `@login_required` | Redirect unauthenticated users |
| `@permission_required('app.perm')` | Check specific permission |
| `@require_http_methods(['GET','POST'])` | Restrict HTTP methods |
| `@cache_page(60 * 15)` | Cache view response |
| `@csrf_exempt` | Disable CSRF (use cautiously) |

CBVs use mixins instead: `LoginRequiredMixin`, `PermissionRequiredMixin`.

---

## 04 — Auth & Permissions

**Django's built-in authentication system:**
Provides the `User` model, `authenticate()`, `login()`, `logout()`, session-based auth, password hashing (PBKDF2 + SHA256 by default), and a permission/group system out of the box.

**How to extend the User model?**

| Approach | When to use |
|---|---|
| `AbstractUser` | Add fields, keep built-in auth — **recommended default** |
| `AbstractBaseUser` | Full custom auth logic needed |
| `OneToOneField` profile | Avoid — but fine for minor additions to existing projects |

> ⚠️ Always set `AUTH_USER_MODEL` in settings **before your first migration**.

**What is CSRF and how does Django handle it?**
Cross-Site Request Forgery protection. Django uses a token-based approach via `CsrfViewMiddleware`. HTML forms need `{% csrf_token %}`. AJAX requests need the token in the `X-CSRFToken` header. Use `@csrf_exempt` sparingly (APIs typically use token/JWT auth instead).

**Object-level permissions?**
Django's built-in permissions are model-level only. For object-level permissions, use `django-guardian` or override `has_object_permission()` in DRF permission classes.

---

## 05 — Django REST Framework (DRF)

**Serializer vs ModelSerializer?**
- `Serializer` → full manual control of fields and validation
- `ModelSerializer` → auto-generates fields from model, includes default `create()` and `update()`. Use for standard CRUD; use `Serializer` for complex non-model data.

**APIView vs ViewSet?**
- `APIView` → map HTTP methods manually (`get`, `post`, `put`, `delete`)
- `ViewSet` → actions (`list`, `retrieve`, `create`, `update`, `destroy`) + Router for automatic URL generation

```python
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'users', UserViewSet)
```

**DRF Authentication options:**

| Class | Use case |
|---|---|
| `SessionAuthentication` | Browser-based (Django sessions) |
| `TokenAuthentication` | Simple static token in header |
| `JWTAuthentication` | Via `djangorestframework-simplejwt` |
| `OAuth2` | Via `django-oauth-toolkit` |

**DRF Pagination types:**

| Class | Best for |
|---|---|
| `PageNumberPagination` | Simple page=1,2,3 |
| `LimitOffsetPagination` | limit/offset params |
| `CursorPagination` | Large datasets; opaque cursor, most efficient |

**Serializer validation:**
```python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body']

    def validate_title(self, value):
        if 'spam' in value.lower():
            raise serializers.ValidationError("No spam allowed.")
        return value
```

---

## 06 — Migrations & Database

**Key migration commands:**
```bash
python manage.py makemigrations      # detect model changes
python manage.py migrate             # apply pending migrations
python manage.py showmigrations      # list all + applied status
python manage.py sqlmigrate app 0001 # show raw SQL for a migration
python manage.py migrate app 0001    # rollback to a specific state
```

**What are data migrations?**
Migrations that manipulate data rather than schema. Created with `makemigrations --empty` and use `RunPython` to execute custom Python logic against the database.

```python
from django.db import migrations

def populate_slugs(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    for post in Post.objects.all():
        post.slug = post.title.lower().replace(' ', '-')
        post.save()

class Migration(migrations.Migration):
    operations = [migrations.RunPython(populate_slugs)]
```

**Database transactions:**
```python
from django.db import transaction

with transaction.atomic():
    user.save()
    profile.save()
    # Both saved or both rolled back

@transaction.atomic
def transfer_funds(from_acc, to_acc, amount):
    from_acc.balance -= amount
    to_acc.balance += amount
    from_acc.save()
    to_acc.save()
```

**How to optimize slow queries?**
1. Use `django-debug-toolbar` to identify and count queries
2. Add DB indexes (`db_index=True`, `Meta.indexes`)
3. Use `select_related()` / `prefetch_related()`
4. Use `only()` / `defer()` to limit fetched columns
5. Use `.explain()` on slow QuerySets
6. Use `bulk_create()` / `bulk_update()` for mass operations

---

## 07 — Caching & Performance

**Django caching backends:**

| Backend | Use case |
|---|---|
| Redis (`django-redis`) | Production standard |
| Memcached | Built-in support, no persistence |
| LocMemCache | Dev/testing (in-process only) |
| FileBasedCache | Simple file storage |

**Cache levels:**
```python
# Per-view (decorator)
@cache_page(60 * 15)  # 15 minutes
def my_view(request): ...

# Template fragment
{% load cache %}
{% cache 500 sidebar user.id %}
  ... expensive content ...
{% endcache %}

# Low-level API
from django.core.cache import cache
cache.set('my_key', value, timeout=300)
value = cache.get('my_key')
cache.delete('my_key')
```

**Celery with Django:**
Async task queue for background work (emails, image processing, scheduled jobs). Uses Redis or RabbitMQ as broker.

```python
# tasks.py
from celery import shared_task

@shared_task
def send_welcome_email(user_id):
    user = User.objects.get(id=user_id)
    # send email...

# Call it
send_welcome_email.delay(user.id)
```

---

## 08 — Security

**Django's built-in security features:**

| Protection | Mechanism |
|---|---|
| CSRF | Token-based via `CsrfViewMiddleware` |
| XSS | Auto-escaping in Django templates |
| SQL Injection | ORM uses parameterized queries |
| Clickjacking | `X-Frame-Options: DENY` header |
| Password hashing | PBKDF2 + SHA256 (configurable) |
| Signed cookies | Session data signed with `SECRET_KEY` |

**Production security settings:**
```python
DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = ['yourdomain.com']

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
X_FRAME_OPTIONS = 'DENY'
```

**Preventing SQL injection in raw queries:**
```python
# ✅ Safe — parameterized
cursor.execute("SELECT * FROM users WHERE id = %s", [user_id])

# ❌ Unsafe — never do this
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
```

> Run `python manage.py check --deploy` to get a security audit before going live.

---

## 09 — Deployment & Settings

**Typical production stack:**

| Component | Role |
|---|---|
| Nginx | Reverse proxy + serve static files |
| Gunicorn | WSGI server (sync workloads) |
| Uvicorn / Daphne | ASGI server (async / WebSockets) |
| PostgreSQL | Production database |
| Redis | Cache + Celery message broker |
| Docker | Containerization |

**WSGI vs ASGI?**
- `WSGI` → synchronous, traditional standard (Gunicorn). Fine for most apps.
- `ASGI` → async, supports WebSockets, long-polling, HTTP/2 (Daphne, Uvicorn). Use for real-time features. Django 3.1+ supports ASGI natively.

**Managing settings per environment:**
```
myproject/settings/
  __init__.py
  base.py       # shared settings
  local.py      # development overrides
  production.py # production overrides
```

```bash
# Set via environment variable
export DJANGO_SETTINGS_MODULE=myproject.settings.production
```

Use `python-decouple` or `django-environ` to pull secrets from `.env` files or environment variables.

**Static files in production:**
```bash
python manage.py collectstatic  # gather to STATIC_ROOT
```
Serve via Nginx, AWS S3/CloudFront, or use `whitenoise` for simpler setups. Configure cloud storage via `STORAGES` setting (Django 4.2+).

---

## Quick Reference — Common Gotchas

| Gotcha | Fix |
|---|---|
| Forgot `makemigrations` | Always run after model changes |
| `related_name` clash | Set unique `related_name` on FK fields |
| `__all__` in serializer exposes sensitive fields | Explicitly list fields |
| Mutable default arguments in models | Use `default=list` not `default=[]` |
| Time zones | Set `USE_TZ = True`, use `timezone.now()` not `datetime.now()` |
| Circular imports | Use `apps.get_model()` in migrations / signals |
| Large file uploads | Use `FileField` with chunked reading or direct-to-S3 |
| Secret key in code | Always load from environment variable |

---

*Django Interview Cheatsheet — Core concepts through deployment*
