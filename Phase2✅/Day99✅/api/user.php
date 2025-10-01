<?php
require_once "../core/jwt_utils.php";
$headers = getallheaders();

if (!isset($headers['Authorization'])) {
    http_response_code(401);
    echo json_encode(["message" => "Token required"]);
    exit;
}

$jwt = trim(str_replace("Bearer", "", $headers['Authorization']));
$user = validate_jwt($jwt);

if ($user) {
    echo json_encode(["message" => "Welcome", "user" => $user]);
} else {
    http_response_code(401);
    echo json_encode(["message" => "Invalid token"]);
}
