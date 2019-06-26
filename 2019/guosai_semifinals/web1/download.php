<?php
session_start();
if (!isset($_SESSION['login'])) {
	header("Location: login.php");
	die();
}

if (!isset($_REQUEST['filename'])) {
	die();
}

include "class.php";
ini_set("open_basedir", getcwd() . ":/etc:/tmp");

chdir($_SESSION['sandbox']);
$file = new File();
$filename = (string) $_REQUEST['filename'];
if (strlen($filename) < 40 && $file->open($filename) && stristr($filename, "flag") === false) {
	Header("Content-type: application/octet-stream");
	Header("Content-Disposition: attachment; filename=" . basename($filename));
	echo $file->close();
} else {
	echo "File not exist";
}
?>
