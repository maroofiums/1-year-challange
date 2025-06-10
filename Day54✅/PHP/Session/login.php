<?php

    session_start();
    $_SESSION['username'] = "maroof";
    echo "Wellcome" . $_SESSION['username'];

?>