# Day 113
---

## ✅ What You’ll Build:

1. **User Login API** (`login.php`) – returns JWT on success
2. **Protected Route** (`protected.php`) – accessible only with valid JWT
3. **JWT Helper Functions** (`jwt_utils.php`)
4. **Fake user data** (simulate DB)

---

## ✅ 1. Setup Project Structure:

```
php-jwt-api/
├── jwt_utils.php
├── login.php
├── protected.php
└── users.php
```

---

## ✅ 2. Install JWT via Composer

```bash
composer require firebase/php-jwt
```

---

## ✅ 3. `users.php` – Fake Users

```php
<?php
// users.php
$users = [
    [
        "id" => 1,
        "email" => "test@example.com",
        "password" => password_hash("123456", PASSWORD_DEFAULT)
    ]
];
```

---

## ✅ 4. `jwt_utils.php` – JWT Helpers

```php
<?php
// jwt_utils.php
require 'vendor/autoload.php';

use Firebase\JWT\JWT;
use Firebase\JWT\Key;

$secret_key = "your_secret_key";
$algorithm = "HS256";

function generate_jwt($payload, $secret_key, $algorithm) {
    return JWT::encode($payload, $secret_key, $algorithm);
}

function validate_jwt($jwt, $secret_key, $algorithm) {
    try {
        $decoded = JWT::decode($jwt, new Key($secret_key, $algorithm));
        return $decoded;
    } catch (Exception $e) {
        return null;
    }
}
```

---

## ✅ 5. `login.php` – Authenticate & Generate Token

```php
<?php
// login.php
require 'users.php';
require 'jwt_utils.php';

header('Content-Type: application/json');

$data = json_decode(file_get_contents("php://input"));

if (!isset($data->email) || !isset($data->password)) {
    http_response_code(400);
    echo json_encode(["message" => "Email and Password required"]);
    exit();
}

foreach ($users as $user) {
    if ($user['email'] === $data->email && password_verify($data->password, $user['password'])) {
        $payload = [
            "iss" => "localhost",
            "iat" => time(),
            "exp" => time() + (60 * 60), // 1 hour
            "user_id" => $user['id'],
            "email" => $user['email']
        ];
        $jwt = generate_jwt($payload, $secret_key, $algorithm);
        echo json_encode(["token" => $jwt]);
        exit();
    }
}

http_response_code(401);
echo json_encode(["message" => "Invalid credentials"]);
```

---

## ✅ 6. `protected.php` – Authenticated Route

```php
<?php
// protected.php
require 'jwt_utils.php';

header('Content-Type: application/json');

$authHeader = $_SERVER['HTTP_AUTHORIZATION'] ?? '';

if (!$authHeader || !preg_match('/Bearer\s(\S+)/', $authHeader, $matches)) {
    http_response_code(401);
    echo json_encode(["message" => "Access Denied: No token provided"]);
    exit();
}

$jwt = $matches[1];
$decoded = validate_jwt($jwt, $secret_key, $algorithm);

if (!$decoded) {
    http_response_code(401);
    echo json_encode(["message" => "Access Denied: Invalid or expired token"]);
    exit();
}

echo json_encode([
    "message" => "Access granted",
    "user" => $decoded
]);
```

---

## ✅ Testing the API

1. **Login Request:**

   * POST `http://localhost/php-jwt-api/login.php`
   * Body:

     ```json
     {
       "email": "test@example.com",
       "password": "123456"
     }
     ```

2. **Get JWT token in response** and use it in:

3. **Protected Request:**

   * GET `http://localhost/php-jwt-api/protected.php`
   * Header:

     ```
     Authorization: Bearer YOUR_JWT_TOKEN
     ```

---

## 🔐 Tips

* Always **store your secret key securely** (e.g., `.env` file).
* Use **HTTPS** in production.
* You can extend this by connecting to a **real MySQL database**, adding **signup**, **refresh tokens**, and **role-based access**.

