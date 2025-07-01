<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);

    if ($username && $password) {
        $data = "$username|" . password_hash($password, PASSWORD_DEFAULT) . "\n";
        file_put_contents("users.txt", $data, FILE_APPEND);
        echo "✅ Registered successfully. <a href='login.php'>Login now</a>";
        exit;
    } else {
        echo "⚠️ All fields are required.";
    }
}
?>

<h2>Register</h2>
<form method="POST">
  Username: <input type="text" name="username" required><br>
  Password: <input type="password" name="password" required><br>
  <input type="submit" value="Register">
</form>
