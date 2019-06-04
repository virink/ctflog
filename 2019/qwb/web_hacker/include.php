<?php

$file = $argv[1];

$c = file_get_contents($file);
preg_match_all('/\$_[GEPOST]{3,4}\[\'.*?\'\]/', $c, $matches);
foreach ($matches[0] as $value) {
	eval("$value='echo virinkvirinkvirinkvirinkvirink';");
}
include_once $file;
ob_start();
$cc = ob_get_contents();
ob_clean();
if (strripos($cc, 'virinkvirinkvirinkvirinkvirink') !== false) {
	echo $file;
	file_put_contents("orz.log", "$file\r\n", FILE_APPEND);
}