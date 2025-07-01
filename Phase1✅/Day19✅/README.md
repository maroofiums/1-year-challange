# Day 19

Welcome to Day 19 of the 365 Days of Code Challenge!
Great! Let's build your **Mini Blog System using Django** from scratch.

---

## ✅ Step-by-Step Guide to Build a Blog System in Django

---

### 📌 **Project Overview**

**Main Features**:

* Home page (blog listing)
* Blog detail page
* Create/Edit/Delete blog posts
* User authentication (login, logout, signup)
* Admin panel for management

---

### 🧱 Step 1: Create a Django Project

```bash
django-admin startproject blog_project
cd blog_project
python manage.py startapp blog
```

---

### ⚙️ Step 2: Configure `settings.py`

```python
# blog_project/settings.py

INSTALLED_APPS = [
    ...
    'blog',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
]

# Set templates and static dirs if needed
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

---

### 🗃️ Step 3: Create the Blog Post Model

```python
# blog/models.py

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

Then run:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 👩‍💻 Step 4: Admin Setup

```python
# blog/admin.py

from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

Create a superuser:

```bash
python manage.py createsuperuser
```

---

### 🧾 Step 5: Create Blog Views

```python
# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return redirect('home')
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        post.delete()
    return redirect('home')
```

---

### 📝 Step 6: Forms

```python
# blog/forms.py

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
```

---

### 🌐 Step 7: URLs

```python
# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]
```

Link in main `urls.py`:

```python
# blog_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout
    path('', include('blog.urls')),
]
```

---

### 🎨 Step 8: Templates (Basic Example)

Create the following inside `blog/templates/blog/`:

#### `home.html`

```html
{% extends "base.html" %}
{% block content %}
  <h2>All Blog Posts</h2>
  {% for post in posts %}
    <div>
      <h3><a href="{% url 'post_detail' post.pk %}">{{ post.title }}</a></h3>
      <p>By {{ post.author }} on {{ post.created_at }}</p>
    </div>
  {% endfor %}
{% endblock %}
```

#### `post_detail.html`

```html
{% extends "base.html" %}
{% block content %}
  <h2>{{ post.title }}</h2>
  <p>{{ post.content }}</p>
  <p>By {{ post.author }} | {{ post.created_at }}</p>
  {% if user == post.author %}
    <a href="{% url 'post_edit' post.pk %}">Edit</a>
    <a href="{% url 'post_delete' post.pk %}">Delete</a>
  {% endif %}
{% endblock %}
```

#### `post_form.html`

```html
{% extends "base.html" %}
{% block content %}
  <h2>New/Edit Post</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
  </form>
{% endblock %}
```

#### `base.html`

```html
<!DOCTYPE html>
<html>
<head>
  <title>Blog System</title>
</head>
<body>
  <nav>
    <a href="{% url 'home' %}">Home</a>
    {% if user.is_authenticated %}
      <a href="{% url 'post_create' %}">New Post</a>
      <a href="{% url 'logout' %}">Logout</a>
    {% else %}
      <a href="{% url 'login' %}">Login</a>
    {% endif %}
  </nav>
  <hr>
  {% block content %}{% endblock %}
</body>
</html>
```

---

### 🚀 Step 9: Run Your Site

```bash
python manage.py runserver
```

Visit: [http://localhost:8000](http://localhost:8000)

