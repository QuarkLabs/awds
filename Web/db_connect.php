<?php
    $server = "localhost";
    $user = "root";
    $pass = "mysql@linuxvm";
    $db = "sis";

    $conn = mysqli_connect($server,$user,$pass,$db);

    if (!$conn){
        die("Connection Failed :". mysqli_connect_error());
    }
?>
