# Day104
## 🎯 **Project: PHP & Django API Integration**

### 🔥 Tumhara Mission:

> PHP wali website se Django ke API ko access karna.
> Jaise: PHP form → Django API se data lena → browser mein result dikhana.

---

## 🧱 Step 1: Django Backend Banaana (Server Side)

### 🛠️ 1. Django Install karo

```bash
pip install django djangorestframework djangorestframework-simplejwt django-cors-headers
```

> 🧠 **Yeh kya kar raha hai?**
> Django web framework hai, REST Framework APIs banane ke liye, JWT authentication ke liye, aur CORS PHP ke liye.

---

### 🛠️ 2. settings.py mein Changes karo

```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'corsheaders',
    'yourapp',  # apna app yahan likho
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...,
]

CORS_ALLOW_ALL_ORIGINS = True
```

> 💡 **CORS kya hota hai?**
> Jab PHP (ya koi aur site) Django se data mangti hai to CORS allow karta hai ki "bahar wale" client access kar saken.

---

### 🛠️ 3. Django API banani hai (simple protected API)

**views.py**

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ProtectedAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello {request.user.username}, you are logged in!"})
```

**urls.py (app level)**

```python
from django.urls import path
from .views import ProtectedAPI
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view()),  # login token
    path('api/protected/', ProtectedAPI.as_view()),     # protected data
]
```

> 🔐 Token API login karega. Protected API sirf login hone ke baad access hoti hai.

---

### 🛠️ 4. Django Superuser banao

```bash
python manage.py createsuperuser
```

> ✅ Yeh admin login banata hai — PHP use karega yeh login.

---

## 🐘 Step 2: PHP Code likhna (Client Side)

Tum PHP se Django ke token maangoge, aur fir us token se protected API call karoge.

```php
<?php
// Step 1: Login to get token
$loginUrl = 'http://127.0.0.1:8000/api/token/';
$data = ['username' => 'admin', 'password' => 'admin123'];

$options = [
    'http' => [
        'header'  => "Content-type: application/json",
        'method'  => 'POST',
        'content' => json_encode($data),
    ]
];

$context = stream_context_create($options);
$response = file_get_contents($loginUrl, false, $context);
$token = json_decode($response, true);
$accessToken = $token['access'];

// Step 2: Access protected API using token
$apiUrl = 'http://127.0.0.1:8000/api/protected/';
$options = [
    'http' => [
        'header'  => "Authorization: Bearer $accessToken",
        'method'  => 'GET',
    ]
];

$context = stream_context_create($options);
$response = file_get_contents($apiUrl, false, $context);
$data = json_decode($response, true);

echo "<h2>Response from Django:</h2>";
print_r($data);
?>
```

---

## 🔍 Real-Life Example 💡

> Jaise tumhara PHP form user login ka button dabata hai → Django JWT token deta hai → us token se tum Django ka secure API call kar ke `Welcome, Maroof!` dikhate ho.

---

## ✅ Final Result on Browser

```
Response from Django:
Array
(
    [message] => Hello admin, you are logged in!
)
```

