<?php
// jwt_utils.php
require 'vendor/autoload.php';

use Firebase\JWT\JWT;
use Firebase\JWT\Key;

$secret_key = "your_secret_key";
$algorithm = "HS256";

function generate_jwt($payload, $secret_key, $algorithm) {
    return JWT::encode($payload, $secret_key, $algorithm);
}

function validate_jwt($jwt, $secret_key, $algorithm) {
    try {
        $decoded = JWT::decode($jwt, new Key($secret_key, $algorithm));
        return $decoded;
    } catch (Exception $e) {
        return null;
    }
}

?>