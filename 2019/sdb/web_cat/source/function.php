<?php

require_once 'config.php';

function RandomStr($len = 16) {
	$chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
	$random = '';
	for ($i = 0; $i < $len; $i++) {
		$random .= $chars[rand(0, strlen($chars) - 1)]; //
	}
	return $random;
}
function checkUser() {
	if (isset($_SESSION['username'])) {
		return true;
	}
	header("Location: redirect.php?u=login");
	die();
}
function checkHeader() {
	//var_dump($_SERVER);
	if (isset($_COOKIE['HOST'])) {
		if ($_COOKIE['HOST'] != "where_is_my_cat.ichunqiu.com") {
			die('You are not belong to here');
		}
	} else {
		setcookie("HOST", "guess where you are");
		die('You are not belong to here');
	}
}

function test() {
	var_dump($_COOKIE);
	echo mt_rand(), "\n";
}

if (isset($_GET['test'])) {
	test();
	die();
}

function curl($u) {
	$ch = curl_init();
	curl_setopt_array($ch, array(
		CURLOPT_SSL_VERIFYHOST => 0,
		CURLOPT_SSL_VERIFYPEER => 0,
		CURLOPT_HEADER => 0,
		CURLOPT_SSLVERSION => 3,
		CURLOPT_POST => 1,
		CURLOPT_POSTFIELDS => '',
		CURLOPT_FOLLOWLOCATION => 1,
		CURLOPT_VERBOSE => 1,
	));
	curl_setopt($ch, CURLOPT_URL, $u);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_NOBODY, 0);
	$output = curl_exec($ch);
	curl_close($ch);
	return $output;
}

// http://where_is_my_cat.ichunqiu.com.127.0.0.1.xip.io/
// http://where_is_my_cat.ichunqiu.com.47.101.138.236.xip.io/
function isCat($url) {
	$condition_1 = preg_match("/^(https?):\/\/([A-z0-9]+[_\-]?[A-z0-9]+\.)*[A-z0-9]+\-?[A-z0-9]+\.[A-z0-9]{2,}()?(\/.*)*\/?\.(jpg|png|gif)$/i", $url);
	$condition_2 = (substr($url, 7, 28) == $_COOKIE[HOST] || substr($url, 8, 28) == $_COOKIE[HOST]);
	if ($condition_1 && $condition_2) {
		return true;
	}
	return false;
}

function waf($strFiltKey, $strFiltValue) {

	$filter = "\\<.+javascript:window\\[.{1}\\\\x|<.*=(&#\\d+?;?)+?>|<.*(data|src)=data:text\\/html.*>|\\b(alert\\(|confirm\\(|expression\\(|prompt\\(|benchmark\s*?\\(\d+?|sleep\s*?\\([\d\.]+?\\)|load_file\s*?\\()|<[a-z]+?\\b[^>]*?\\bon([a-z]{4,})\s*?=|^\\+\\/v(8|9)|\\b(and|or)\\b\\s*?([\\(\\)'\"\\d]+?=[\\(\\)'\"\\d]+?|[\\(\\)'\"a-zA-Z]+?=[\\(\\)'\"a-zA-Z]+?|>|<|\s+?[\\w]+?\\s+?\\bin\\b\\s*?\(|\\blike\\b\\s+?[\"'])|\\/\\*.+?\\*\\/|<\\s*script\\b|\\bEXEC\\b|UNION.+?SELECT(\\(.+\\)|\\s+?.+?)|UPDATE(\\(.+\\)|\\s+?.+?)SET|INSERT\\s+INTO.+?VALUES|(SELECT|DELETE)(\\(.+\\)|\\s+?.+?\\s+?)FROM(\\(.+\\)|\\s+?.+?)|(CREATE|ALTER|DROP|TRUNCATE)\\s+(TABLE|DATABASE)";

	if (is_array($strFiltValue)) {
		$strFiltValue = implode($strFiltValue);
	}
	if (preg_match('/' . $filter . '/is', $strFiltValue) == 1) {
		die('hacker, go out!');
	}
}

$allData = array($_GET, $_POST);
foreach ($allData as $data) {
	foreach ($data as $key => $value) {
		waf($key, $value);
	}
}

checkHeader();
