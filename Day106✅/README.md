# Day 106




# 🔐 PHP Authentication System (Sessions + JWT)

A simple and secure user authentication system built using **PHP** and **MySQLi**, supporting both:

- ✅ **Session-Based Authentication** – Standard login/logout with PHP sessions.
- ✅ **JWT-Based Authentication** – Token-based login for APIs and SPAs.

## 📂 Folder Structure

```

/php-auth/
│
├── config/
│   └── db.php                 # Database connection
│
├── jwt/
│   ├── generate-jwt.php       # JWT creation logic
│   └── validate-jwt.php       # JWT validation
│
├── auth/
│   ├── register.php           # User registration
│   ├── login.php              # Session login
│   ├── logout.php             # Logout (Session destroy)
│   ├── jwt-login.php          # JWT login endpoint
│
├── protected/
│   ├── dashboard.php          # Protected session page
│   └── jwt-protected.php      # Protected JWT API route
│
├── assets/
│   └── style.css              # Optional styling
│
├── index.php                  # Home / Login form
└── register.html              # Registration form


```
## ⚙️ Setup Instructions

### 1. Requirements

- PHP 7.x or 8.x
- MySQL
- XAMPP/WAMP or Live Server
- Composer (for JWT)

### 2. Clone or Download

```bash
git clone https://github.com/yourusername/php-auth.git
cd php-auth
````

### 3. Setup Database

Import this SQL into your MySQL:

```sql
CREATE DATABASE auth_demo;

USE auth_demo;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100) UNIQUE,
  password VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 4. Configure `config/db.php`

```php
$host = 'localhost';
$user = 'root';
$pass = '';
$dbname = 'auth_demo';

$conn = new mysqli($host, $user, $pass, $dbname);
```

### 5. Install Firebase PHP-JWT (For JWT)

```bash
composer require firebase/php-jwt
```

---

## 🧪 How to Use

### 🔐 Session-Based

* `index.php` → Login
* `register.html` → Register
* `dashboard.php` → Protected Page
* `logout.php` → End Session

### 🔐 JWT-Based (API)

* POST `jwt-login.php` → Returns a JWT
* GET `jwt-protected.php` with `Authorization: Bearer <token>` header → Access secured data

---

## 🧰 Features

* Passwords hashed using `password_hash()`
* Secure login via sessions
* JWT generation and validation using `HS256`
* Database connectivity via `mysqli`
* Simple front-end login/register forms

---

## 🔒 JWT Secret

Set a secret key inside `generate-jwt.php` and `validate-jwt.php`:

```php
$secret_key = "your_super_secret_key";
```

Use `.env` or `config.php` for production.

---

## 📬 Contact

**Author:** Muhammad Maroof
📧 Email: [maroof96965@gmail.com](mailto:maroof96965@gmail.com)
🔗 GitHub: [github.com/maroof2424](https://github.com/maroof2424)

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

```

Let me know if you want this system to include:
- Forgot password with email OTP
- Email verification after signup
- Admin/user role-based protection  
I'll guide you step-by-step or write the full code.
```
