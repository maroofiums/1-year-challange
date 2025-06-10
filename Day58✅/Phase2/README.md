Great Maroof! 🔐 Let's start **Phase 2: JWT Authentication** using Django REST Framework (DRF).

---

## ✅ **Phase 2: JWT Authentication (Step-by-Step)**

### 📌 **Goal**:

Implement login, register, and token-based authentication system using **JWT (JSON Web Tokens)** in Django REST Framework.

---

## 📦 Step 1: Install Required Packages

Run this in terminal:

```bash
pip install djangorestframework-simplejwt
```

---

## 🧠 Step 2: Update `settings.py`

Add `'rest_framework_simplejwt'` in `INSTALLED_APPS` (optional but recommended).

Then add this in `REST_FRAMEWORK` settings:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
```

---

## 🔁 Step 3: Update `urls.py`

In your main `urls.py` (e.g., `myapi/urls.py`):

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

---

## 👤 Step 4: Create Register API

### `api/views.py`:

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already taken'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    refresh = RefreshToken.for_user(user)

    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    })
```

---

## 🔗 Step 5: Add to `api/urls.py`

```python
from django.urls import path
from .views import register_user

urlpatterns = [
    path('register/', register_user, name='register'),
]
```

---

## 🚀 Step 6: Test It!

### ➕ Register:

* POST to `http://127.0.0.1:8000/api/register/`
* Body:

```json
{
  "username": "maroof",
  "password": "1234"
}
```

### 🔐 Get Token:

* POST to `http://127.0.0.1:8000/api/token/`
* Body:

```json
{
  "username": "maroof",
  "password": "1234"
}
```

---

## ✅ Token Use

Now for protected APIs, add this in request header:

```
Authorization: Bearer <access_token>
```

---

## 🔒 Next Step?

* Want to protect a view so only logged-in users can access it?
* Want logout / blacklist token?
* Want user profile view?

Let me know which one and I’ll guide you perfectly like Phase 1 🔥
