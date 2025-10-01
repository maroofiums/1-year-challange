<?php

    $loginUrl = 'http://127.0.0.1:8000/api/token/';
    $data = ['username'=> 'admin','password'=>'admin123'];

    $options = [
        'http' => [
            'header' => "Content-type: application/json",
            'method' => 'POST',
            'content' => json_encode($data),
        ]
    ];

    $context = stream_context_create($options);
    $response = file_get_contents($loginUrl,false,$context);
    $token = json_decode($response,true);
    $accessToken = $token['access'];

    $apiUrl = 'http://127.0.0.1:8000/api/protected/';
    $options = [
        'http' => [
            'header' => "Authorization: Bearer $accessToken",
            'method' => 'GET',
        ]
    ];

    
    $context = stream_context_create($options);
    $response = file_get_contents($apiUrl, false, $context);
    $data = json_decode($response, true);
    if ($response === false) {
        echo "Error connection to API!";
        exit;
    }
    echo "<h2>Response from Django:</h2>";
    print_r($data);

?>