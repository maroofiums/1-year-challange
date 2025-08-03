# **Day 125**

## Django + FastAPI Hello World

A demonstration project showing how to integrate Django and FastAPI in a single application. This project showcases both traditional Django views with templates and modern FastAPI endpoints with automatic API documentation.

## 🚀 Features

- **Django Views**: Traditional Django views with beautiful templates
- **FastAPI Endpoints**: Modern REST API with automatic OpenAPI documentation
- **Unified ASGI Application**: Both frameworks running in the same application
- **Beautiful UI**: Modern, responsive design with gradients and animations
- **Interactive Documentation**: FastAPI's automatic API docs at `/docs`

## 📁 Project Structure

```
django_fastapi_app/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── README.md                # This file
├── mysite/                  # Django project settings
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py             # WSGI configuration
│   └── asgi.py             # ASGI configuration (Django + FastAPI)
└── hello/                   # Django app
    ├── __init__.py
    ├── apps.py             # App configuration
    ├── urls.py             # App URL patterns
    ├── views.py            # Django views
    └── templates/          # Django templates
        └── hello/
            ├── index.html   # Hello world template
            └── hello_name.html  # Hello with name template
```

## 🛠️ Installation

1. **Clone or create the project** (if you haven't already):
   ```bash
   # If starting from scratch, create the files as shown above
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Django migrations**:
   ```bash
   python manage.py migrate
   ```

## 🚀 Running the Application

### Option 1: Using Django's development server
```bash
python manage.py runserver
```

### Option 2: Using Uvicorn (recommended for ASGI)
```bash
uvicorn mysite.asgi:application --reload
```

The application will be available at `http://localhost:8000`

## 🌐 Available Endpoints

### Root Page (`/`)
- Beautiful landing page with links to all endpoints
- Modern UI with gradient backgrounds

### Django Endpoints
- `/django/` - Django Hello World page
- `/django/hello/{name}/` - Django Hello with custom name

### FastAPI Endpoints
- `/api/hello` - FastAPI Hello World (JSON response)
- `/api/hello/{name}` - FastAPI Hello with custom name (JSON response)
- `/docs` - Interactive API documentation (Swagger UI)
- `/redoc` - Alternative API documentation (ReDoc)

## 🎨 Features

### Django Features
- Traditional Django views with templates
- Beautiful, responsive HTML templates
- JSON responses when `Accept: application/json` header is sent
- Bootstrap-style styling with custom CSS

### FastAPI Features
- Modern async/await syntax
- Automatic OpenAPI documentation
- Type hints and validation
- Interactive API explorer
- CORS middleware enabled

### Integration Features
- Single ASGI application serving both frameworks
- Django mounted under `/django/` path
- FastAPI serving API endpoints and root page
- Shared CORS configuration
- Unified error handling

## 🔧 Development

### Adding New Django Views
1. Add view functions to `hello/views.py`
2. Add URL patterns to `hello/urls.py`
3. Create templates in `hello/templates/hello/`

### Adding New FastAPI Endpoints
1. Add route functions to `mysite/asgi.py`
2. Use FastAPI decorators (`@app.get`, `@app.post`, etc.)
3. Automatic documentation will be generated

### Database Integration
- Django ORM available for database operations
- SQLite database by default (can be changed in settings)
- Run `python manage.py makemigrations` and `python manage.py migrate` for model changes

## 📚 Learning Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [ASGI Specification](https://asgi.readthedocs.io/)

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is open source and available under the [MIT License](LICENSE). 