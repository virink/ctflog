<?php
/**
 * Created by PhpStorm.
 * User: phithon
 * Date: 15/10/14
 * Time: 下午7:58
 */


$DATABASE = array(
    
    "host" => "127.0.0.1",
    "username" => "xdctf",
    "password" => "123456!@#zzds",
    "dbname" =>"xdctf"
);

$db = new mysqli($DATABASE['host'],$DATABASE['username'],$DATABASE['password'],$DATABASE['dbname']);
$req = array();

foreach(array($_GET, $_POST, $_COOKIE) as $global_var) {
    foreach($global_var as $key => $value) {
        is_string($value) && $req[$key] = addslashes($value);
    }
}

define("UPLOAD_DIR", "/upload/");

function redirect($location)
{
    header("Location: {$location}");
    exit;
}
