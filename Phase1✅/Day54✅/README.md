# Day 54

Welcome to Day 54 of the 365 Days of Code Challenge!

---

## 🔹 1. PHP Forms kya hote hain?

Jab user koi data input karta hai jaise naam, email, etc., aur "Submit" karta hai, to woh data server par bhejna hota hai — isay hi PHP Form kehte hain.

**Example:**

```html
<form action="process.php" method="post">
  Name: <input type="text" name="name">
  <input type="submit" value="Submit">
</form>
```

Yeh form `process.php` file ko `POST` method se data bhej raha hai.

---

## 🔹 2. GET aur POST method kya hoti hain?

### ✅ GET:

* Data URL me show hota hai.
* Kam sensitive data ke liye use hota hai.
* Bookmark ho sakta hai.

```html
<form action="get-example.php" method="get">
  Name: <input type="text" name="name">
  <input type="submit" value="Send">
</form>
```

**get-example.php**

```php
<?php
echo "Your name is: " . $_GET['name'];
?>
```

---

### ✅ POST:

* Data URL me **nahi** dikhai deta.
* Sensitive data ke liye behtar (e.g. password).
* Secure method hai form ke liye.

```html
<form action="post-example.php" method="post">
  Email: <input type="email" name="email">
  <input type="submit" value="Send">
</form>
```

**post-example.php**

```php
<?php
echo "Your email is: " . $_POST['email'];
?>
```

---

## 🔹 3. PHP Sessions kya hote hain?

Session ek temporary memory hoti hai jo user ke browser aur server ke darmiyan chalti hai. Jab user login karta hai to uski info store ki jati hai.

### ✅ Session Start Karna

```php
<?php
session_start(); // Always required
$_SESSION['username'] = "maroof";
echo "Welcome, " . $_SESSION['username'];
?>
```

### ✅ Session Use Karna (kisi aur page pe)

```php
<?php
session_start();
echo "Hi again, " . $_SESSION['username'];
?>
```

### ✅ Session Destroy Karna (logout ke liye)

```php
<?php
session_start();
session_destroy();
echo "Logged out.";
?>
```

---

## 🔚 Summary

| Feature | Use                 | Visibility    | Secure? |
| ------- | ------------------- | ------------- | ------- |
| GET     | URL params          | ✅ URL me      | ❌ Nahin |
| POST    | Form data           | ❌ URL me nahi | ✅ Haan  |
| SESSION | User ko track karna | ❌ Server-side | ✅ Haan  |

---
