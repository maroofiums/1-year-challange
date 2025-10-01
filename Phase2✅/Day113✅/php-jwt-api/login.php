<?php
// login.php
require 'users.php';
require 'jwt_utils.php';

header('Content-Type: application/json');

$data = json_decode(file_get_contents("php://input"));

if (!isset($data->email) || !isset($data->password)) {
    http_response_code(400);
    echo json_encode(["message" => "Email and Password required"]);
    exit();
}

foreach ($users as $user) {
    if ($user['email'] === $data->email && password_verify($data->password, $user['password'])) {
        $payload = [
            "iss" => "localhost",
            "iat" => time(),
            "exp" => time() + (60 * 60), // 1 hour
            "user_id" => $user['id'],
            "email" => $user['email']
        ];
        $jwt = generate_jwt($payload, $secret_key, $algorithm);
        echo json_encode(["token" => $jwt]);
        exit();
    }
}

http_response_code(401);
echo json_encode(["message" => "Invalid credentials"]);

?>