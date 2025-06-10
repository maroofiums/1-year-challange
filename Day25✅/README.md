# Day 25

Welcome to Day 25 of the 365 Days of Code Challenge!
Here’s a **simple Django CRUD (Create, Read, Update, Delete) app** you can build called **Project Manager**. This app allows users to manage projects and their details (like title, description, status, and deadline).

---

### 💡 **Project Name**: Project Manager

**Tech Stack**: Django, SQLite, Bootstrap (optional for UI)
**Features**:

* Create a new project
* View all projects
* Update project details
* Delete a project

---

### 🧱 Step-by-Step Guide

#### 1. **Create Django Project**

```bash
django-admin startproject project_manager
cd project_manager
python manage.py startapp projects
```

#### 2. **Register App**

Add `'projects'` to `INSTALLED_APPS` in `settings.py`.

---

#### 3. **Define Model**

In `projects/models.py`:

```python
from django.db import models

class Project(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    deadline = models.DateField()

    def __str__(self):
        return self.title
```

---

#### 4. **Create Forms**

In `projects/forms.py`:

```python
from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
```

---

#### 5. **Create Views**

In `projects/views.py`:

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectForm

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_create(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('project_list')
    return render(request, 'projects/project_form.html', {'form': form})

def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('project_list')
    return render(request, 'projects/project_form.html', {'form': form})

def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'projects/project_confirm_delete.html', {'project': project})
```

---

#### 6. **URLs**

In `projects/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('create/', views.project_create, name='project_create'),
    path('update/<int:pk>/', views.project_update, name='project_update'),
    path('delete/<int:pk>/', views.project_delete, name='project_delete'),
]
```

Include it in `project_manager/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
]
```

---

#### 7. **Templates**

Create a folder `templates/projects/` and add:

* `project_list.html`
* `project_form.html`
* `project_confirm_delete.html`

Basic example for `project_list.html`:

```html
<h1>Project List</h1>
<a href="{% url 'project_create' %}">Create New Project</a>
<ul>
  {% for project in projects %}
    <li>
      <strong>{{ project.title }}</strong> - {{ project.status }} | {{ project.deadline }}
      <a href="{% url 'project_update' project.pk %}">Edit</a>
      <a href="{% url 'project_delete' project.pk %}">Delete</a>
    </li>
  {% endfor %}
</ul>
```

---

### ✅ Final Steps:

* Run migrations:

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

* Create a superuser:

  ```bash
  python manage.py createsuperuser
  ```

* Run server:

  ```bash
  python manage.py runserver
  ```

---

Would you like me to generate all the template files or ZIP the full project structure for you?
