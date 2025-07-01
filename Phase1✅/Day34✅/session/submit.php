<?php

session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = htmlspecialchars($_POST['username']);

    if (!empty($username)) {
        $_SESSION['username'] = $username;

        echo "<h1>Hello, $username!</h1>";
        echo "<p>Thank you for submitting the form.</p>";
    } else {
        echo "<p>Please enter your name.</p>";
    }
} else {
    echo "<p>Invalid Request Method.</p>";
}
?>
