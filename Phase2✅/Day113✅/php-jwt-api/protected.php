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
?>