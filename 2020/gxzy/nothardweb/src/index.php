<?php
session_start();
error_reporting(E_ALL);
include "user.php";
// include "conn.php";
$IV = "\x9c%\xb8\xd12\xa4\xcbd";
// $_SESSION['key'] = "94707886"; // you cant know that;
if (!isset($_COOKIE['user']) || !isset($_COOKIE['hash'])) {
	if (!isset($_SESSION['key'])) {
		print("1 : <td>" . mt_rand() . "</td>\n");
		for ($i = 1; $i < 226; $i++) {
			mt_rand();
		}
		print("227 : <td>" . mt_rand() . "</td>\n");
		print("228 : <td>" . mt_rand() . "</td>\n");
		$mtrand = mt_rand();
		$_SESSION['key'] = strval($mtrand & 0x5f5e0ff);
	}
	$username = "guest";
	$o = new User($username);
	echo $o->show();
	$ser_user = serialize($o);
	$cipher = openssl_encrypt($ser_user, "des-cbc", $_SESSION['key'], 0, $IV);
	setcookie("user", base64_encode($cipher), time() + 3600);
	setcookie("hash", md5($ser_user), time() + 3600);
} else {
	$user = base64_decode($_COOKIE['user']);
	$uid = openssl_decrypt($user, 'des-cbc', $_SESSION['key'], 0, $IV);
	var_dump($uid, md5($uid), $_COOKIE['hash']);
	if (md5($uid) !== $_COOKIE['hash']) {
		die("no hacker!");
	}
	$o = unserialize($uid);
	echo $o->show();
	if ($o->username === "admin") {
		$_SESSION['name'] = 'admin';
		echo 'maybe something useful';
		// include "hint.php";
	}
}