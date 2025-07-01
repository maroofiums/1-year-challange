# Day 8

Here's a clear explanation of **Django Views, Templates, and Static Files**, with examples:

---

## 🔹 1. **Django Views**

Views are Python functions (or classes) that handle a web request and return a web response.

### ➤ Example: Function-based View

```python
# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

This view takes a request and returns the `home.html` template.

### ➤ URL Mapping

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

---

## 🔹 2. **Django Templates**

Templates are HTML files with Django Template Language (DTL) for dynamic content.

### ➤ Example: `home.html`

```html
<!-- templates/home.html -->
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p>Hello, {{ user.username }}!</p>
</body>
</html>
```

* `{{ user.username }}` → inserts dynamic data.
* `{% static 'css/style.css' %}` → loads a static CSS file.

---

## 🔹 3. **Static Files**

Static files are CSS, JavaScript, images, etc., used in templates.

### ➤ Folder Structure:

```
yourapp/
├── static/
│   └── css/
│       └── style.css
├── templates/
│   └── home.html
```

### ➤ settings.py

Make sure this is set:

```python
# settings.py
STATIC_URL = '/static/'

# In development:
STATICFILES_DIRS = [BASE_DIR / "static"]
```

### ➤ Load Static Tag

At the top of your HTML file:

```django
{% load static %}
```

---

## ✅ Summary

| Feature      | Purpose                         | Example                               |
| ------------ | ------------------------------- | ------------------------------------- |
| **View**     | Python logic to handle requests | `return render(request, 'home.html')` |
| **Template** | HTML page with dynamic content  | `{{ user.username }}`                 |
| **Static**   | CSS, JS, images                 | `{% static 'css/style.css' %}`        |

---

Would you like a **mini project** to practice all 3 (views, templates, and static files) together?
