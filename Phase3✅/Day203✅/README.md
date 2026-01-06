# Day 203


## 📁 Project Structure

```
mini_ecommerce/
│
├── mini_ecommerce/          # Main project folder (settings, urls, wsgi)
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── accounts/                # User authentication (login, logout, register)
│   ├── templates/accounts/
│   ├── views.py
│   ├── urls.py
│
├── store/                   # Main store app (products, cart, etc.)
│   ├── templates/store/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── static/                  # CSS, JS, images
│
├── templates/               # Base templates
│   ├── base.html
│
├── db.sqlite3               # Local database
│
├── manage.py
└── README.md
```

---

## 🚀 Features

✅ User Registration & Login (Django Auth)
✅ Product Listing and Detail Pages
✅ Add to Cart Functionality
✅ Simple Cart Page
✅ Logout and Authentication Redirects
✅ Admin Panel for Product Management
✅ Responsive Bootstrap UI

---

## ⚙️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/maroof2424/mini_ecommerce.git
cd mini_ecommerce
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # For Windows
source venv/bin/activate  # For Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6. Run the Server

```bash
python manage.py runserver
```

Now visit 👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🧭 URL Patterns Overview

| URL                  | Description                 |
| -------------------- | --------------------------- |
| `/`                  | Home page (product listing) |
| `/product/<id>/`     | Product detail page         |
| `/add-to-cart/<id>/` | Add a product to the cart   |
| `/cart/`             | View shopping cart          |
| `/accounts/login/`   | Login page                  |
| `/accounts/logout/`  | Logout                      |
| `/admin/`            | Django admin panel          |

---

## 🧑‍💻 Tech Stack

| Layer          | Technology                    |
| -------------- | ----------------------------- |
| Backend        | Django 5.x                    |
| Frontend       | HTML, CSS, Bootstrap          |
| Database       | SQLite                        |
| Authentication | Django’s built-in auth system |

---

## 🧰 Future Improvements

🔹 Add checkout & order system
🔹 Add product categories and filters
🔹 Add payment gateway integration (Stripe/PayPal)
🔹 Add user profiles & order history

---



## ❤️ Author

**Maroof**
📍 Python Developer (ML, Backend, Arduino)
🔗 [GitHub: maroof2424](https://github.com/maroof2424)

---

## ✨ Quick Summary

| Step | Action                                        |
| ---- | --------------------------------------------- |
| 1️⃣  | Setup environment & install packages          |
| 2️⃣  | Configure models and URLs                     |
| 3️⃣  | Run migrations                                |
| 4️⃣  | Add sample products from Admin                |
| 5️⃣  | Test login + cart system                      |
| ✅    | Done! Your mini e-commerce is live locally 🎉 |

---

