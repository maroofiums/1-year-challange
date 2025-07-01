<?php
require 'vendor/autoload.php';
use Firebase\JWT\JWT;
use Firebase\JWT\Key;

$secretKey = "your_secret_key";

$headers = apache_request_headers();
$authHeader = $headers['Authorization'] ?? '';

if (!$authHeader) {
    http_response_code(401);
    echo "Token missing.";
    exit;
}

$token = str_replace('Bearer ', '', $authHeader);

try {
    $decoded = JWT::decode($token, new Key($secretKey, 'HS256'));
    echo "Token valid! User ID: " . $decoded->user_id;
} catch (Exception $e) {
    http_response_code(401);
    echo "Invalid token: " . $e->getMessage();
}
?>
