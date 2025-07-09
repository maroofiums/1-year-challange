<?php
require_once "../config/Database.php";
require_once "../core/jwt_utils.php";
require __DIR__ . '/../vendor/autoload.php';

use Firebase\JWT\JWT;
use Firebase\JWT\Key;

$secret_key = "your_secret_key";

$data = json_decode(file_get_contents("php://input"));
$email = $data->email;
$password = $data->password;

$db = (new Database())->getConnection();
$query = "SELECT * FROM users WHERE email = ?";
$stmt = $db->prepare($query);
$stmt->execute([$email]);
$user = $stmt->fetch(PDO::FETCH_ASSOC);

if ($user && password_verify($password, $user['password'])) {
    $payload = [
        "iss" => "localhost",
        "iat" => time(),
        "exp" => time() + 3600,
        "data" => ["id" => $user['id'], "email" => $user['email']]
    ];

    $jwt = JWT::encode($payload, $secret_key, 'HS256');
    echo json_encode(["jwt" => $jwt]);
} else {
    http_response_code(401);
    echo json_encode(["message" => "Login failed"]);
}
