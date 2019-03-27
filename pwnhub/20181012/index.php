<?php
$token = sha1($_SERVER['REMOTE_ADDR']);
$dir = '../sandbox/' . $token . '/';

is_dir($dir) ?: mkdir($dir);
is_file($dir . 'index.php') ?: file_put_contents($dir . 'index.php', str_replace('#SHA1#', $token, file_get_contents('./template')));

switch ($_GET['action'] ?: '') {
case 'go':
	header('Location: http://' . $token . '.sandbox.r-cursive.ml:1337/');
	break;
case 'reset':
	system('rm -rf ' . $dir);
	break;
default:
	show_source(__FILE__);
}

if ("" === preg_replace('/[0-9a-f]{40}\.sandbox\.r-cursive\.ml:1337/', NULL, $_SERVER['HTTP_HOST'])) // no escape this time
{
	ini_set("open_basedir", $_SERVER['DOCUMENT_ROOT'] . "/:/tmp/");
} else {
	show_source(__FILE__);
	die();
}

?>
<style>code{font-family: Segoe Script, Brush Script MT, cursive; font-size: 1.337em;}</style>

