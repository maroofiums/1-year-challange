<?php
use Firebase\JWT\JWT;
use Firebase\JWT\Key;

function validate_jwt($jwt) {
    $secret_key = "your_secret_key";
    try {
        $decoded = JWT::decode($jwt, new Key($secret_key, 'HS256'));
        return $decoded->data;
    } catch (Exception $e) {
        return false;
    }
}
