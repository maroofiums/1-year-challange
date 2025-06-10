<?php

    echo "<center><h1><i>Hello PHP</i></h1></center>";
    $txt = "W3Schools.com";
    echo "I love $txt!<br>";

    function myMessage(){
        echo "Hello world<br>";
    }

    myMessage();

    function greet($name){
        echo "Hello {$name}<br>";
    }
    greet("Maroof");

    function info($name,$age){
        echo "My name is {$name} and my age is {$age}<br>";
    }
    info("maroof",17)
?>