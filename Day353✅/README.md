# Day 353

# 🚀 MySockets — Django WebSocket Chat App

A real-time chat application built using **Django** and **Django Channels**, enabling bidirectional communication via WebSockets.

---

## 📌 Features

* Real-time messaging using WebSockets
* Django backend with async support
* Simple frontend (HTML + JavaScript)
* Clean and minimal architecture
* Easy to extend (groups, authentication, Redis)

---

## 🧠 Tech Stack

* Python
* Django
* Django Channels
* WebSockets
* HTML, JavaScript

---

## 🏗️ Project Structure

```bash
mysockets/
│
├── myapp/                 # Main App
│   ├── consumers.py       # WebSocket logic
│   ├── routing.py         # WebSocket routes
│   ├── views.py           # Django views
│   ├── urls.py
│   └── templates/myapp/
│       └── index.html     # Frontend
│
├── mysockets/
│   ├── asgi.py            # ASGI config (WebSockets entry)
│   ├── settings.py
│   └── urls.py
│
└── manage.py
```
---

## 🔧 Configuration

### Add to `settings.py`

```python
INSTALLED_APPS = [
    "channels",
    "myapp",
]

ASGI_APPLICATION = "mysockets.asgi.application"
```

---

## ▶️ Run the Project

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🔌 How It Works

1. Client connects via WebSocket
2. Django Channels handles connection
3. Consumer receives message
4. Server sends response back instantly

---

## 📡 WebSocket Flow

```
Client (Browser)
    ⇄ WebSocket
ASGI Server
    ⇄
Django Channels
    ⇄
Consumer (Business Logic)
```

---

## 🧪 Example Message Flow

* User sends message
* `receive()` method processes it
* `send()` returns response
* UI updates instantly

---

## 🚀 Future Improvements

* Multi-user chat (groups)
* Username support
* Persistent chat (database)
* Redis for scaling
* Authentication system
* UI improvements

---

## 📚 Learnings

* Difference between WSGI and ASGI
* Real-time communication concepts
* Django async architecture
* WebSocket lifecycle

---

## 🤝 Contributing

Feel free to fork this project and improve it.

---

## 📜 License

This project is open-source and available under the MIT License.
