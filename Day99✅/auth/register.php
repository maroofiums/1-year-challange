<?php
require_once "../config/Database.php";

$data = json_decode(file_get_contents("php://input"));
$name = $data->name;
$email = $data->email;
$password = password_hash($data->password, PASSWORD_BCRYPT);

$db = (new Database())->getConnection();
$query = "INSERT INTO users(name, email, password) VALUES (?, ?, ?)";
$stmt = $db->prepare($query);
if ($stmt->execute([$name, $email, $password])) {
    echo json_encode(["message" => "User registered"]);
} else {
    echo json_encode(["message" => "Registration failed"]);
}
