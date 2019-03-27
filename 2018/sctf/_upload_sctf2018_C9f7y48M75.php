<?php
if (!isset($lemon_flag)) {
    die('No!');
}

if (@$_SESSION['admin'] !== 1) {
    die('403.');
}

$ip = sha1(md5($_SERVER['REMOTE_ADDR'] . "sctf2018"));
$user_dir = './upload_7788/' . $ip;
if (!is_dir($user_dir)) {
    mkdir($user_dir);
    touch($user_dir . '/index.php');
}

if (isset($_POST['submit']) && !empty($_FILES)) {


    $typeAccepted = ["image/jpeg", "image/gif", "image/png"];

    $blackext = ["php", "php3", "php4", "php5", "pht", "phtml", "phps", "inc"];
    
    $filearr = pathinfo($_FILES["upload"]["name"]);

    if (!in_array($_FILES["upload"]['type'], $typeAccepted)) {
        die("type error");
    }
    if (in_array($filearr["extension"], $blackext)) {
        die("extension error");
    }

    $target_path = $user_dir . '/';
    $target_path .= basename($_FILES['upload']['name']);

    if (!move_uploaded_file($_FILES['upload']['tmp_name'], $target_path)) {
        die('upload error!');
    } else {
        echo 'succesfully uploaded! dir: ' . $user_dir . "/" . $_FILES['upload']['name'];
    }
} else {
    die("<script>alert('please upload image.')</script>");
}
?>
