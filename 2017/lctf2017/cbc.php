<?php

error_reporting(E_ALL);

session_save_path('/Users/virink/tmp/lctf2017/sess');
session_start();

define("METHOD", "aes-128-cbc");
define('SECRET_KEY', '1234567812345678');

$id='guess';
// $id = "guess\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b";
// guess\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b

function get_random_token(){
    $random_token = '';
    $str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890";
    for($i = 0; $i < 16; $i++){
        $random_token .= substr($str, rand(1, 61), 1);
    }
    return $random_token;
}

function get_identity(){
    global $id;
    $token = get_random_token();
    var_dump($token);
    // g5CKm47JYc9Hxgi => iv
    $c = openssl_encrypt($id, METHOD, SECRET_KEY, OPENSSL_RAW_DATA, $token);
    $_SESSION['id'] = base64_encode($c);
    $b64_token = base64_encode($token);
    setcookie("token", $b64_token);
    if($id === 'admin'){
        $_SESSION['isadmin'] = 1;
    }else{
        $_SESSION['isadmin'] = 0;
    }
}

function test_identity(){
    if (isset($_SESSION['id'])) {
        var_dump($_COOKIE);
        $c = base64_decode($_SESSION['id']);
        // var_dump($c);
        $ttt = isset($_GET['t'])?$_GET['t']:$_COOKIE["token"];
        // $token = base64_decode($ttt);
        $token = $ttt;
        $u = openssl_decrypt($c, METHOD, SECRET_KEY, OPENSSL_RAW_DATA, $token);
        var_dump($u);
        if($u){
            if ($u === 'admin') {
                $_SESSION['isadmin'] = 1;
                return 1;
            }
        }else{
            die("Error!");
        } 
    }
    return 0;
}

if (isset($_POST['username']) || isset($_GET['u'])) {
    get_identity();
}else{
    test_identity();
}
