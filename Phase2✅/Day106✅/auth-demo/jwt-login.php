<?php
require 'db.php';
require 'vendor/autoload.php';
use Firebase\JWT\JWT;
use Firebase\JWT\Key;

$secretKey = "your_secret_key";

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $stmt = $conn->prepare("SELECT id, password FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->store_result();

    if ($stmt->num_rows == 1) {
        $stmt->bind_result($id, $hashed);
        $stmt->fetch();

        if (password_verify($password, $hashed)) {
            $payload = [
                "iss" => "http://localhost",
                "iat" => time(),
                "exp" => time() + 3600,
                "user_id" => $id
            ];
            $jwt = JWT::encode($payload, $secretKey, 'HS256');
            echo json_encode(["token" => $jwt]);
        } else {
            echo json_encode(["message" => "Wrong password"]);
        }
    } else {
        echo json_encode(["message" => "User not found"]);
    }
    $stmt->close();
}
?>
