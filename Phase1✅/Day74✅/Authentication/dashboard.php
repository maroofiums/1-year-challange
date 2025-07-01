<?php
session_start();
if (!isset($_SESSION['user'])) {
    header("Location: login.php");
    exit;
}
?>

<h2>Welcome, <?= $_SESSION['user']; ?>!</h2>
<p>This is your dashboard.</p>
<a href="logout.php">Logout</a>
