# Day273
---

## 🛍️ MiniStore – A Mini E-Commerce App built with Django

### ⚙️ Overview

**MiniStore** is a lightweight e-commerce web app built with Django.
Users can browse products, add items to their cart, and checkout — all without authentication (guest mode).
It’s the perfect base to extend into a full-blown store later with login, payments, and orders.

---

### 🧩 Features

✅ Browse products
✅ Add to cart (session-based)
✅ View & update cart
✅ Checkout (clears cart)
✅ Django Admin for managing products
✅ Bootstrap 5 responsive UI

---

### 🗂️ Project Structure

```
MiniStore/
│
├── manage.py
├── requirements.txt
│
├── MiniStore/               # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── store/                   # Core app
│   ├── migrations/
│   ├── templates/store/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── product_detail.html
│   │   ├── cart.html
│   │   └── checkout.html
│   ├── static/store/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
└── db.sqlite3
```

---

### 🧠 Tech Stack

* **Backend:** Django 5+
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Database:** SQLite3 (default)
* **Media Storage:** Local file system

---

### 🚀 Setup Instructions

#### 1️⃣ Clone the repository

```bash
git clone https://github.com/maroof2424/MiniStore.git
cd MiniStore
```

#### 2️⃣ Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # (Windows)
# OR
source venv/bin/activate  # (Mac/Linux)
```

#### 3️⃣ Install dependencies

```bash
pip install django pillow
```

#### 4️⃣ Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 5️⃣ Create superuser (for admin access)

```bash
python manage.py createsuperuser
```

#### 6️⃣ Run the development server

```bash
python manage.py runserver
```

Visit 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 💻 Admin Panel

Add and manage products from Django’s built-in admin:
🧭 URL → `/admin/`
Use your superuser credentials.

---

### 🛠️ Models Overview

| Model        | Purpose                                               |
| ------------ | ----------------------------------------------------- |
| **Product**  | Stores product info (name, price, image, description) |
| **Cart**     | Session-based cart for each visitor                   |
| **CartItem** | Links products to carts with quantities               |

---

### 🖼️ Screenshots (optional placeholders)

| Page           | Preview                                                             |
| -------------- | ------------------------------------------------------------------- |
| Home Page      | ![Home](https://via.placeholder.com/400x250?text=Home+Page)         |
| Product Detail | ![Detail](https://via.placeholder.com/400x250?text=Product+Detail)  |
| Cart           | ![Cart](https://via.placeholder.com/400x250?text=Cart+Page)         |
| Checkout       | ![Checkout](https://via.placeholder.com/400x250?text=Checkout+Page) |

---

### 🌱 Future Upgrades

🚀 User authentication (login/signup)
🚀 Persistent carts (linked to users)
🚀 Product categories and search
🚀 Order history & invoice generation
🚀 Stripe / PayPal payment integration
🚀 Deploy on Render or PythonAnywhere

---

### 🧑‍💻 Author

**Maroof** — Python Developer
GitHub: [@maroof2424](https://github.com/maroof2424)

---
