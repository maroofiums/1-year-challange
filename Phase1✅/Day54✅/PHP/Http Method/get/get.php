<?php

    if ($_SERVER["REQUEST_METHOD"] == "GET"){
        if (!empty($_GET['name'])){
            echo "Wellcome " . htmlspecialchars($_GET['name']);
        } else{
            echo "Name Field is empty.";
        }

    }

?>