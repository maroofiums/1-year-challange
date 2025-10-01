# Day 99

Welcome to Day 99 of the 365 Days of Code Challenge!
---

## 📌 Goal: Build a Secure PHP REST API with JWT Auth

### Tech Stack: PHP + MySQL + JWT (JSON Web Token)

---

## ✅ Step-by-Step Plan

### ✅ 1. Setup Project Structure

```
jwt-api/
├── config/
│   └── Database.php
├── auth/
│   ├── login.php
│   └── register.php
├── api/
│   └── user.php
├── core/
│   └── jwt_utils.php
├── .htaccess
├── .env (optional)
└── index.php
```

---

### ✅ 2. Install JWT Library

Use [Firebase PHP-JWT](https://github.com/firebase/php-jwt):

```bash
composer require firebase/php-jwt
```

---

### ✅ 3. Create `config/Database.php`

```php
<?php
class Database {
    private $host = "localhost";
    private $db_name = "jwt_demo";
    private $username = "root";
    private $password = "";
    public $conn;

    public function getConnection() {
        $this->conn = null;
        try {
            $this->conn = new PDO(
                "mysql:host={$this->host};dbname={$this->db_name}",
                $this->username, $this->password
            );
            $this->conn->exec("set names utf8");
        } catch(PDOException $exception) {
            echo "Connection error: " . $exception->getMessage();
        }
        return $this->conn;
    }
}
```

---

### ✅ 4. Create Users Table in MySQL

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### ✅ 5. `auth/register.php` (User Registration)

```php
<?php
require_once "../config/Database.php";

$data = json_decode(file_get_contents("php://input"));
$name = $data->name;
$email = $data->email;
$password = password_hash($data->password, PASSWORD_BCRYPT);

$db = (new Database())->getConnection();
$query = "INSERT INTO users(name, email, password) VALUES (?, ?, ?)";
$stmt = $db->prepare($query);
if ($stmt->execute([$name, $email, $password])) {
    echo json_encode(["message" => "User registered"]);
} else {
    echo json_encode(["message" => "Registration failed"]);
}
```

---

### ✅ 6. `auth/login.php` (JWT Issuing)

```php
<?php
require_once "../config/Database.php";
require_once "../core/jwt_utils.php";
require __DIR__ . '/../vendor/autoload.php';

use Firebase\JWT\JWT;
use Firebase\JWT\Key;

$secret_key = "your_secret_key";

$data = json_decode(file_get_contents("php://input"));
$email = $data->email;
$password = $data->password;

$db = (new Database())->getConnection();
$query = "SELECT * FROM users WHERE email = ?";
$stmt = $db->prepare($query);
$stmt->execute([$email]);
$user = $stmt->fetch(PDO::FETCH_ASSOC);

if ($user && password_verify($password, $user['password'])) {
    $payload = [
        "iss" => "localhost",
        "iat" => time(),
        "exp" => time() + 3600,
        "data" => ["id" => $user['id'], "email" => $user['email']]
    ];

    $jwt = JWT::encode($payload, $secret_key, 'HS256');
    echo json_encode(["jwt" => $jwt]);
} else {
    http_response_code(401);
    echo json_encode(["message" => "Login failed"]);
}
```

---

### ✅ 7. `core/jwt_utils.php` (JWT Validator)

```php
<?php
use Firebase\JWT\JWT;
use Firebase\JWT\Key;

function validate_jwt($jwt) {
    $secret_key = "your_secret_key";
    try {
        $decoded = JWT::decode($jwt, new Key($secret_key, 'HS256'));
        return $decoded->data;
    } catch (Exception $e) {
        return false;
    }
}
```

---

### ✅ 8. `api/user.php` (Protected Endpoint)

```php
<?php
require_once "../core/jwt_utils.php";
$headers = getallheaders();

if (!isset($headers['Authorization'])) {
    http_response_code(401);
    echo json_encode(["message" => "Token required"]);
    exit;
}

$jwt = trim(str_replace("Bearer", "", $headers['Authorization']));
$user = validate_jwt($jwt);

if ($user) {
    echo json_encode(["message" => "Welcome", "user" => $user]);
} else {
    http_response_code(401);
    echo json_encode(["message" => "Invalid token"]);
}
```

---

### ✅ 9. `.htaccess` (Enable REST-friendly URLs)

```apache
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^ index.php [QSA,L]
```

---

## ✅ Testing Instructions

Use **Postman**:

* `POST /auth/register.php` – Register user
* `POST /auth/login.php` – Get JWT token
* `GET /api/user.php` – Pass `Authorization: Bearer <token>` to access

