# Day 5

Welcome to Day 5 of the 365 Days of Code Challenge!
Sure! Here's the **full Django CRUD Task Manager app code**, separated file-by-file for clarity:

---

## 🗂 **1. models.py**

```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

---

## 🗂 **2. forms.py**

```python
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'is_completed']
```

---

## 🗂 **3. views.py**

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
```

---

## 🗂 **4. urls.py (inside your app folder)**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
]
```

---

## 🗂 **5. Templates (inside `templates/tasks/`)**

### 📄 task\_list.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Task List</title>
</head>
<body>
    <h1>Tasks</h1>
    <a href="{% url 'task_create' %}">Add New Task</a>
    <hr>
    {% for task in tasks %}
        <h3>{{ task.title }} {% if task.is_completed %}(Done){% endif %}</h3>
        <p>{{ task.description }}</p>
        <p>Due: {{ task.due_date }}</p>
        <a href="{% url 'task_update' task.pk %}">Edit</a> |
        <a href="{% url 'task_delete' task.pk %}">Delete</a>
        <hr>
    {% empty %}
        <p>No tasks available.</p>
    {% endfor %}
</body>
</html>
```

### 📄 task\_form.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Task Form</title>
</head>
<body>
    <h1>{% if form.instance.pk %}Update{% else %}Create{% endif %} Task</h1>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</button>
    </form>
    <a href="{% url 'task_list' %}">Back to Task List</a>
</body>
</html>
```

### 📄 task\_confirm\_delete.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Delete Task</title>
</head>
<body>
    <h1>Are you sure you want to delete '{{ task.title }}'?</h1>
    <form method="POST">
        {% csrf_token %}
        <button type="submit">Yes, delete</button>
    </form>
    <a href="{% url 'task_list' %}">Cancel</a>
</body>
</html>
```

---

## 🗂 **6. Main Project urls.py**

Inside your main project folder (e.g., `project/urls.py`):

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('your_app_name.urls')),  # Replace with your app name
]
```

---

### ✅ Final Notes:

* Don’t forget to run:

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver
  ```
* Your app will be accessible at `http://localhost:8000/`

