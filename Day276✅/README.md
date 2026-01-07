
## Day276

> Django mein **real-time communication** samajhna
> Aur end tak tum confidently keh sako:
> **“WebSocket kya hota hai, HTTP se kyun different hai, aur Django Channels ka role kya hai.”**

---

## 🧠 Step 1: HTTP vs WebSocket (Root concept)

### ❌ HTTP (Normal Django)

* Request → Response → Connection close
* Refresh karna parta hai
* One-way communication

Example:
Instagram page refresh → new likes dikhein

---

### ✅ WebSocket (Real-Time)

* Connection **open rehti hai**
* Server khud data bhej sakta hai
* Two-way communication

Example:

* WhatsApp message aata hai
* Tumne refresh nahi kiya
  🔥 = WebSocket

👉 **Key idea:**

> WebSocket = *“always connected pipe”*

---

## 🧩 Step 2: Django Channels kya karta hai?

Django by default **HTTP only** samajhta hai
WebSockets ke liye hume chahiye:

### 👉 **Django Channels**

Channels = Django ko bolta hai:

> “Bro, sirf request-response nahi, real-time bhi handle karo”

---

## 🧱 Step 3: Architecture (simple diagram in words)

```
Browser
   ↕ WebSocket
Consumer (Channels)
   ↕
Django App
```

* **Consumer** = WebSocket ka view
* Jaise views.py HTTP ke liye hota hai
* Waise hi **consumers.py** WebSocket ke liye

---

## 🛠️ Step 4: Minimal Working Setup (No Overkill)

### 📦 Install

```bash
pip install channels
```

---

### ⚙️ settings.py

```python
INSTALLED_APPS = [
    ...
    'channels',
]

ASGI_APPLICATION = 'project.asgi.application'
```

⚠️ Notice:
WSGI ❌
ASGI ✅ (because async)

---

### 📄 asgi.py

```python
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        app.routing.websocket_urlpatterns
    ),
})
```

---

## 🔀 Step 5: Routing (WebSocket ka URL)

### app/routing.py

```python
from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path("ws/chat/", ChatConsumer.as_asgi()),
]
```

---

## 🧠 Step 6: Consumer (Heart of WebSocket)

### app/consumers.py

```python
from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            "message": "Connected successfully"
        }))

    def receive(self, text_data):
        self.send(text_data=json.dumps({
            "message": text_data
        }))

    def disconnect(self, close_code):
        pass
```

🔥 Yeh sabse simple **echo server** hai
Jo aayega → wapas bhej dega

---

## 🧪 Step 7: Testing (Browser se)

Browser console open karo:

```javascript
let socket = new WebSocket("ws://127.0.0.1:8000/ws/chat/");

socket.onmessage = (e) => console.log(e.data);

socket.send("Hello Django");
```

Agar message wapas aaye →
🎉 **WebSocket working**

---
