"""
ASGI config for mysite project.
"""

import os
from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import uvicorn

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Create Django ASGI application
django_app = get_asgi_application()

# Create FastAPI wrapper
app = FastAPI(title="Django + FastAPI Hello World", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# FastAPI routes
@app.get("/api/hello")
async def fastapi_hello():
    """FastAPI hello world endpoint"""
    return {"message": "Hello World from FastAPI!", "framework": "FastAPI"}

@app.get("/api/hello/{name}")
async def fastapi_hello_name(name: str):
    """FastAPI hello with name parameter"""
    return {"message": f"Hello {name} from FastAPI!", "framework": "FastAPI"}

@app.get("/", response_class=HTMLResponse)
async def root():
    """Root endpoint with links to both Django and FastAPI"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Django + FastAPI Hello World</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
            .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
            h1 { color: #333; text-align: center; }
            .section { margin: 20px 0; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }
            .django { background: #092e20; color: white; }
            .fastapi { background: #0d1117; color: white; }
            a { color: #4CAF50; text-decoration: none; }
            a:hover { text-decoration: underline; }
            .endpoint { background: #f9f9f9; padding: 10px; margin: 10px 0; border-radius: 3px; font-family: monospace; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Django + FastAPI Hello World</h1>
            
            <div class="section django">
                <h2>🐍 Django Endpoints</h2>
                <p>Traditional Django views and templates</p>
                <div class="endpoint">
                    <a href="/django/">Django Hello World</a>
                </div>
                <div class="endpoint">
                    <a href="/django/hello/john/">Django Hello with Name</a>
                </div>
            </div>
            
            <div class="section fastapi">
                <h2>⚡ FastAPI Endpoints</h2>
                <p>Modern FastAPI with automatic API documentation</p>
                <div class="endpoint">
                    <a href="/api/hello">FastAPI Hello World</a>
                </div>
                <div class="endpoint">
                    <a href="/api/hello/jane">FastAPI Hello with Name</a>
                </div>
                <div class="endpoint">
                    <a href="/docs">FastAPI Interactive Docs</a>
                </div>
            </div>
            
            <div class="section">
                <h2>📚 How to Run</h2>
                <p>1. Install dependencies: <code>pip install -r requirements.txt</code></p>
                <p>2. Run migrations: <code>python manage.py migrate</code></p>
                <p>3. Start the server: <code>python manage.py runserver</code></p>
                <p>4. Or use uvicorn: <code>uvicorn mysite.asgi:app --reload</code></p>
            </div>
        </div>
    </body>
    </html>
    """

# Mount Django app under /django/ path
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware

# Create a new FastAPI app for Django integration
main_app = FastAPI(title="Django + FastAPI Integration")

# Add the same CORS middleware
main_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount Django app
main_app.mount("/django", django_app)

# Include FastAPI routes
main_app.include_router(app.router)

# Export the main app
application = main_app 