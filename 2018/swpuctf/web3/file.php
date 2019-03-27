<?php
header("content-type:text/html;charset=utf-8");
include 'function.php';
include 'class.php';
// ini_set('open_basedir', '/var/www/html/');
$file = $_GET["file"] ? $_GET['file'] : "";
if (empty($file)) {
	echo "<h2>There is no file to show!<h2/>";
}
$show = new Show();
if (file_exists($file)) {
	$show->source = $file;
	$show->_show();
} else if (!empty($file)) {
	die('file doesn\'t exists.');
}
?>