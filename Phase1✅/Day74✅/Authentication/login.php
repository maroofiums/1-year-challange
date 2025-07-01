<?php
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $input_user = trim($_POST['username']);
    $input_pass = trim($_POST['password']);
    $lines = file("users.txt", FILE_IGNORE_NEW_LINES);

    foreach ($lines as $line) {
        list($user, $hash) = explode('|', $line);
        if ($input_user == $user && password_verify($input_pass, $hash)) {
            $_SESSION['user'] = $input_user;

            // ✅ Log successful login
            $log = "$input_user logged in at " . date("Y-m-d H:i:s") . "\n";
            file_put_contents("logins.txt", $log, FILE_APPEND);

            header("Location: dashboard.php");
            exit;
        }
    }
    echo "❌ Invalid credentials.";
}
?>

<h2>Login</h2>
<form method="POST">
  Username: <input type="text" name="username" required><br>
  Password: <input type="password" name="password" required><br>
  <input type="submit" value="Login">
</form>
<p>Don't have an account? <a href="register.php">Register here</a></p>
