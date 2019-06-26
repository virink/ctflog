<?php
session_start();
if (!isset($_SESSION['login'])) {
    header("Location: login.php");
    die();
}

include "class.php";

if (isset($_FILES["file"])) {
    $filename = $_FILES["file"]["name"];
    $pos = strrpos($filename, ".");
    if ($pos !== false) {
        $filename = substr($filename, 0, $pos);
    }
    
    $fileext = ".gif";
    switch ($_FILES["file"]["type"]) {
        case 'image/gif':
            $fileext = ".gif";
            break;
        case 'image/jpeg':
            $fileext = ".jpg";
            break;
        case 'image/png':
            $fileext = ".png";
            break;
        default:
            $response = array("success" => false, "error" => "Only gif/jpg/png allowed");
            Header("Content-type: application/json");
            echo json_encode($response);
            die();
    }

    if (strlen($filename) < 40 && strlen($filename) !== 0) {
        $dst = $_SESSION['sandbox'] . $filename . $fileext;
        move_uploaded_file($_FILES["file"]["tmp_name"], $dst);
        $response = array("success" => true, "error" => "");
        Header("Content-type: application/json");
        echo json_encode($response);
    } else {
        $response = array("success" => false, "error" => "Invaild filename");
        Header("Content-type: application/json");
        echo json_encode($response);
    }
}
?>
