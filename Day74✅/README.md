# Day 74

Here's a clear and practical explanation of **PHP Forms**, **GET/POST**, and **Sessions** with examples to help you learn deeply:

---

## 🧾 **1. PHP Forms (Basics)**

Forms are used to collect user input. The data can be sent to a server using `GET` or `POST`.

### ✅ Example HTML Form:

```html
<form action="process.php" method="POST">
  <label>Name:</label>
  <input type="text" name="username" required>
  <br>
  <input type="submit" value="Submit">
</form>
```

* `action="process.php"` → the form data is sent to this file.
* `method="POST"` → data will be sent using the POST method.

---

## 📩 **2. GET vs POST in PHP**

### 🔹 GET:

* Data sent via URL (not secure).
* Useful for search queries, pagination, etc.
* Limit on data size (\~2048 characters).
* Visible in URL.

**Example:**

```html
<form action="search.php" method="GET">
  <input type="text" name="q">
  <input type="submit" value="Search">
</form>
```

```php
// search.php
echo "You searched for: " . $_GET['q'];
```

---

### 🔸 POST:

* Data sent in the request body (more secure).
* No size limit.
* Used for forms like login, signup, etc.

**Example:**

```html
<form action="login.php" method="POST">
  <input type="text" name="email">
  <input type="password" name="password">
  <input type="submit" value="Login">
</form>
```

```php
// login.php
$email = $_POST['email'];
$password = $_POST['password'];

echo "Email: $email<br>";
echo "Password: $password";
```

---

## 🛡️ **3. PHP Sessions**

Sessions store user data (e.g., login info) across multiple pages.

### ✅ Start a Session:

```php
// Always start session at top of the file
session_start();
```

### 🔐 Store Session Data:

```php
session_start();
$_SESSION['username'] = 'maroof';
echo "Welcome, " . $_SESSION['username'];
```

### 🚪 Destroy Session (Logout):

```php
session_start();
session_destroy();
echo "You have been logged out.";
```

---

## 🧪 **Practice Task: Simple Login System**

### `login.php`

```php
<?php
session_start();
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $username = $_POST['username'];
  $password = $_POST['password'];

  // Hardcoded credentials (use database in real apps)
  if ($username == 'admin' && $password == '1234') {
    $_SESSION['user'] = $username;
    header("Location: dashboard.php");
  } else {
    echo "Invalid login!";
  }
}
?>

<form method="POST" action="">
  Username: <input type="text" name="username"><br>
  Password: <input type="password" name="password"><br>
  <input type="submit" value="Login">
</form>
```

### `dashboard.php`

```php
<?php
session_start();
if (!isset($_SESSION['user'])) {
  header("Location: login.php");
  exit;
}
echo "Welcome " . $_SESSION['user'];
echo "<br><a href='logout.php'>Logout</a>";
```

### `logout.php`

```php
<?php
session_start();
session_destroy();
header("Location: login.php");
```

