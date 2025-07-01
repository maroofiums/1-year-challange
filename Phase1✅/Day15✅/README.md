Zaroor Maroof bhai! Agar tum `from django.contrib.auth import views as auth_views` **use nahi** karna chahte aur **har cheez khud se banana chahte ho** (custom views), to mai tumhe **register, login, logout** ka **pure Django custom code** deta hoon — bilkul step-by-step.

---

## 🔐 **Django Auth System — Custom Views Se (Bina `auth_views`)**

### 📁 File Structure (for idea)

```
project/
│
├── myapp/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       ├── login.html
│       ├── register.html
│       └── dashboard.html
```

---

## ✅ Step-by-Step Code

### 🔸 1. `urls.py` (App wali)

```python
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='dashboard'),  # after login
]
```

---

### 🔸 2. `views.py`

```python
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
            return redirect('register')
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('dashboard')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
```

---

## 📄 Templates (HTML)

### 🔸 `register.html`

```html
<h2>Register</h2>
<form method="post">
  {% csrf_token %}
  <input type="text" name="username" placeholder="Username" required><br>
  <input type="password" name="password" placeholder="Password" required><br>
  <button type="submit">Register</button>
</form>
```

---

### 🔸 `login.html`

```html
<h2>Login</h2>
<form method="post">
  {% csrf_token %}
  <input type="text" name="username" placeholder="Username" required><br>
  <input type="password" name="password" placeholder="Password" required><br>
  <button type="submit">Login</button>
</form>
```

---

### 🔸 `dashboard.html`

```html
<h2>Welcome, {{ request.user.username }}</h2>
<a href="{% url 'logout' %}">Logout</a>
```

---

## 🧪 Extra: Message Show Karna (in HTML)

```html
{% if messages %}
  {% for message in messages %}
    <p style="color: red;">{{ message }}</p>
  {% endfor %}
{% endif %}
```

---

## 🛠️ Settings:

### `settings.py`

```python
LOGIN_URL = '/login/'       # Redirect for @login_required
LOGIN_REDIRECT_URL = '/'    # Not needed here, we use custom redirect
```

---

## 🎯 Ab Tum:

✅ `Register`, `Login`, `Logout`, `Session`
✅ Sab kuch **custom view se bana diya**
❌ Koi `auth_views` use nahi kiya

---

### 💬 Agla step:

Chaho to mai is code ka **full zip project** bana ke de du ya
ab tum **is base pe project banana chahte ho?**

Batao bhai, next kya karein?
