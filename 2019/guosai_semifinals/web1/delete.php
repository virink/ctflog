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

chdir($_SESSION['sandbox']);
$file = new File();
$filename = (string) $_REQUEST['filename'];
if (strlen($filename) < 40 && $file->open($filename)) {
	$file->detele();
	Header("Content-type: application/json");
	$response = array("success" => true, "error" => "");
	echo json_encode($response);
} else {
	Header("Content-type: application/json");
	$response = array("success" => false, "error" => "File not exist");
	echo json_encode($response);
}
?>