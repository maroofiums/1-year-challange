# Day 39

Welcome to Day 39 of the 365 Days of Code Challenge!
Here is the **full Django Blog Project** with:

✅ CRUD operations
✅ Bootstrap 5 styling
✅ Working forms with `django-widget-tweaks`

---

## 🔧 Step-by-Step Setup

---

### 🗂️ Project Structure

```
blog_project/
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   └── blog/
│   │       ├── base.html
│   │       ├── post_list.html
│   │       ├── post_detail.html
│   │       ├── post_form.html
│   │       └── post_confirm_delete.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── blog_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

---

## 🛠 Install Required Packages

```bash
pip install django django-widget-tweaks
```

---

## 1️⃣ `settings.py` (relevant part)

```python
INSTALLED_APPS = [
    ...
    'blog',
    'widget_tweaks',
]
```

---

## 2️⃣ `urls.py`

### Project `blog_project/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

---

### App `blog/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_update, name='post_update'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]
```

---

## 3️⃣ `models.py`

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

---

## 4️⃣ `forms.py`

```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
```

---

## 5️⃣ `views.py`

```python
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})
```

---

## 6️⃣ Templates

### `base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}My Blog{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
        <div class="container">
            <a class="navbar-brand" href="{% url 'post_list' %}">My Blog</a>
            <a class="btn btn-outline-light ms-auto" href="{% url 'post_create' %}">+ New Post</a>
        </div>
    </nav>
    <div class="container">
        {% block content %}
        {% endblock %}
    </div>
</body>
</html>
```

---

### `post_list.html`

```html
{% extends 'blog/base.html' %}
{% block title %}All Posts{% endblock %}
{% block content %}
<h2 class="mb-4">Blog Posts</h2>
<div class="list-group">
    {% for post in posts %}
    <a href="{% url 'post_detail' post.pk %}" class="list-group-item list-group-item-action">
        <div class="d-flex justify-content-between">
            <h5>{{ post.title }}</h5>
            <small>{{ post.created_at|date:"M d, Y H:i" }}</small>
        </div>
        <p class="text-muted">{{ post.content|truncatewords:20 }}</p>
    </a>
    {% empty %}
    <p>No posts yet.</p>
    {% endfor %}
</div>
{% endblock %}
```

---

### `post_detail.html`

```html
{% extends 'blog/base.html' %}
{% block title %}{{ post.title }}{% endblock %}
{% block content %}
<h2>{{ post.title }}</h2>
<p class="text-muted">Posted on {{ post.created_at }}</p>
<p>{{ post.content }}</p>
<hr>
<a href="{% url 'post_update' post.pk %}" class="btn btn-primary">Edit</a>
<a href="{% url 'post_delete' post.pk %}" class="btn btn-danger">Delete</a>
<a href="{% url 'post_list' %}" class="btn btn-secondary">Back</a>
{% endblock %}
```

---

### `post_form.html`

```html
{% extends 'blog/base.html' %}
{% load widget_tweaks %}
{% block title %}Create/Edit Post{% endblock %}
{% block content %}
<h2 class="mb-4">{{ form.instance.pk|yesno:"Edit Post,Create Post" }}</h2>
<form method="post">
    {% csrf_token %}
    <div class="mb-3">
        {{ form.title.label_tag }}
        {{ form.title|add_class:"form-control" }}
    </div>
    <div class="mb-3">
        {{ form.content.label_tag }}
        {{ form.content|add_class:"form-control" }}
    </div>
    <button type="submit" class="btn btn-success">Save</button>
    <a href="{% url 'post_list' %}" class="btn btn-secondary">Cancel</a>
</form>
{% endblock %}
```

---

### `post_confirm_delete.html`

```html
{% extends 'blog/base.html' %}
{% block title %}Delete Post{% endblock %}
{% block content %}
<div class="alert alert-danger">
    <h4>Are you sure you want to delete "{{ post.title }}"?</h4>
    <form method="post">
        {% csrf_token %}
        <button type="submit" class="btn btn-danger">Yes, delete</button>
        <a href="{% url 'post_detail' post.pk %}" class="btn btn-secondary">Cancel</a>
    </form>
</div>
{% endblock %}
```

---

## ✅ Final Steps

1. **Make migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

2. **Create superuser (optional)**

```bash
python manage.py createsuperuser
```

3. **Run the server**

```bash
python manage.py runserver
```

---

Would you like me to:

* Add **authentication (login/signup)?**
* Add **comments system?**
* Add **image upload** to posts?

Let me know!
