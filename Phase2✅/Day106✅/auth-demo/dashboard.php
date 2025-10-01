<?php
require 'db.php';

if (!isset($_SESSION['user_id'])) {
    header("Location: login.html");
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Dashboard</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <form>
    <h2>Welcome to Dashboard 🎉</h2>
    <a href="logout.php">Logout</a>
  </form>
</body>
</html>
