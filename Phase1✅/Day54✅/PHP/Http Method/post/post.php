<?php

    if ($_SERVER["REQUEST_METHOD"] == "POST"){
        if (!empty($_POST["password"])){
            echo "Your password is: " . htmlspecialchars($_POST['password']);
        }else{
            echo "Password field is empty.";
        }
    }

?>