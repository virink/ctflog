<?php

// sha1($_SERVER['REMOTE_ADDR']) === '61a1d20417ff3173fde4ba8aab4b0a7279f0b37e' ?: die();
// ';' === preg_replace('/([^\W_]+_)+[^\W_]+\((?R)*\)/', NULL, $_GET['cmd']) ? eval($_GET['cmd']) : show_source(__FILE__);

// print_r($_SERVER);

if ("" === preg_replace('/[0-9a-f]{40}\.sandbox\.r-cursive\.ml:1337/', NULL, $_SERVER['HTTP_HOST'])) // no escape this time
{
	ini_set("open_basedir", $_SERVER['DOCUMENT_ROOT'] . "/:/tmp/");
} else {
	print_r(preg_replace('/[0-9a-f]{40}\.sandbox\.r-cursive\.ml:1337/', NULL, $_SERVER['HTTP_HOST']));
	die();
}
if (';' === preg_replace('/([^\W_]+_)+[^\W_]+\((?R)*\)/', NULL, $_GET['cmd'])) {
	var_dump($_GET['cmd']);
	echo "\r\n";
	eval($_GET['cmd']);
} else {
	show_source(__FILE__);
}
