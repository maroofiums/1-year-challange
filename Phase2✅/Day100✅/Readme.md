# Day 100 

## Middleware integretion.

- What is Middleware?
- Middleware in Django is a framework of hooks into Django's request/response processing. it's a lightweight, low-level plugin system for globally altering Django's input or output.Let's understand how to integrate middleware into your Django project.

### Create Project and App.

```bash

django admin startproject myproject

python manage.py startapp

```
---

### Add myapp and middleware.py in settings.py 

```python

EXTERNAL_APPS = [
    'myapp',
]

EXTERNAL_MIDDLEWARE = [
    'myapp.middleware.MyMiddleware',
]

INSTALLED_APPS += EXTERNAL_APPS
MIDDLEWARE += EXTERNAL_MIDDLEWARE

```

### create middleware.py in myapp 

```python 

#middleware.py
class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Middleware started🕑")
        response = self.get_response(request)
        print("Middleware Done✅")
        return response



```