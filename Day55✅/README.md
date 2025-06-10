Here's a **step-by-step tutorial** on how to set up **authentication in Django**, including **user login, logout, registration, and protected views**.

---

## 🔐 Django Authentication Tutorial

### ✅ Prerequisites

* Python installed
* Django installed (`pip install django`)
* Basic Django project structure

---

## 1. 🎯 Start a New Project & App

```bash
django-admin startproject auth_project
cd auth_project
python manage.py startapp accounts
```

Add the new app to `INSTALLED_APPS` in `auth_project/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'accounts',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    ...
]
```

---

## 2. 🛠 Create User Authentication Views

### accounts/views.py

```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login')
    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')
```

---

## 3. 🧭 URL Routing

### accounts/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
```

### auth\_project/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]
```

---

## 4. 🧩 Templates

Create a folder: `accounts/templates/accounts/`

### register.html

```html
<h2>Register</h2>
<form method="post">
  {% csrf_token %}
  <input type="text" name="username" placeholder="Username" required>
  <input type="password" name="password" placeholder="Password" required>
  <button type="submit">Register</button>
</form>
<a href="{% url 'login' %}">Already have an account? Login</a>
```

### login.html

```html
<h2>Login</h2>
<form method="post">
  {% csrf_token %}
  <input type="text" name="username" placeholder="Username" required>
  <input type="password" name="password" placeholder="Password" required>
  <button type="submit">Login</button>
</form>
<a href="{% url 'register' %}">Register</a>
```

### dashboard.html

```html
<h2>Welcome, {{ user.username }}!</h2>
<a href="{% url 'logout' %}">Logout</a>
```

---

## 5. 🧪 Run and Test

```bash
python manage.py migrate
python manage.py runserver
```

* Go to `/register/` to create an account
* Log in at `/login/`
* See protected view at `/dashboard/`

---

## 🔒 Bonus: Redirect Unauthenticated Users

In `settings.py`, you can define:

```python
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
```

---

Would you like this turned into a downloadable or visual guide (like PDF or diagram)?
