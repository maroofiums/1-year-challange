<?php
session_start();

$conn = new mysqli("localhost", "root", "", "php_auth");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
