<?php
/**
 * Created by PhpStorm.
 * User: xyz
 * Date: 2017/7/4
 * Time: 10:39
 */
error_reporting(E_ALL);

function output($var){
    echo "\r\n";
    print_r($var);
    echo "\r\n";
}

$DBHOST = 'localhost';
$DBUSER = 'root';
$DBPASS = '';
$DBNAME = 'ctf1';
$flag = 'flag{}';

$mysqli = new mysqli($DBHOST, $DBUSER, $DBPASS, $DBNAME);

foreach ($_GET as $key => $value ) {
    $_GET[$key] = daddslashes($value);
}

foreach ($_POST as $key => $value ) {
    $_POST[$key] = daddslashes($value);
}

foreach ($_COOKIE as $key => $value ) {
    $_COOKIE[$key] = daddslashes($value);
}

foreach ($_SERVER as $key => $value ) {
    // 单引号（'）
    // 双引号（"）
    // 反斜杠（\）
    // NULL
    $_SERVER[$key] = addslashes($value);
}

function daddslashes($string) {
    if(!get_magic_quotes_gpc()) {
        if(is_array($string)) {
            foreach($string as $key => $val) {
                $string[$key] = daddslashes($val);
            }
        } else {
            $string = addslashes($string);
        }
    }
    return $string;
}

function random(){
    $chars  = '123456';
    $chars  = str_shuffle($chars);
    return substr($chars, 0, 1);
}
