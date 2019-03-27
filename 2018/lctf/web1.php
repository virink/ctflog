<?php
error_reporting(E_ALL);
class test {
	public $varr1 = "abc";
	public $varr2 = "123";
	public function echoP() {
		echo $this->varr1 . "<br>";
	}
	public function __construct() {
		echo "__construct<br>";
	}
	public function __destruct() {
		echo "__destruct<br>";
	}
	public function __toString() {
		return "__toString<br>";
	}
	public function __sleep() {
		echo "__sleep<br>";
		return array('varr1', 'varr2');
	}
	public function __wakeup() {
		echo "__wakeup<br>";
	}
	public function __call($a, $b) {
		print_r($a);
		print_r($b);
		echo "__call<br>";
	}
}
// $t = new test();
// echo serialize($t);
// echo "\r\n";
// die();
// highlight_file(__FILE__);
$b = 'implode';
call_user_func($_GET['f'], $_POST);
session_start();
if (isset($_GET['name'])) {
	$_SESSION['name'] = $_GET['name'];
}
var_dump($_SESSION);
$a = array(reset($_SESSION), 'welcome_to_the_lctf2018');
call_user_func($b, $a);
// print_r(get_defined_vars());
// print_r($_SERVER);
?>