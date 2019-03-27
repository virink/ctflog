<?php
//show_source(__FILE__);
include "base.php";
header("Content-type: text/html;charset=utf-8");
error_reporting(0);
function upload_file_do() {
	global $_FILES;
	$filename = "5502a3adf7ab37ded16ad0e2e2f3f99f.jpg";
	mkdir("upload", 0777);
	if (file_exists("upload/" . $filename)) {
		unlink($filename);
	}
	move_uploaded_file($_FILES["file"]["tmp_name"], "upload/" . $filename);
	echo '<script type="text/javascript">alert("上传成功!");</script>';
}
function upload_file() {
	global $_FILES;
	if (upload_file_check()) {
		upload_file_do();
	}
}
function upload_file_check() {
	global $_FILES;
	$allowed_types = array("gif", "jpeg", "jpg", "png");
	$temp = explode(".", $_FILES["file"]["name"]);
	$extension = end($temp);
	if (empty($extension)) {
		//echo "<h4>请选择上传的文件:" . "<h4/>";
	} else {
		if (in_array($extension, $allowed_types)) {
			return true;
		} else {
			echo '<script type="text/javascript">alert("Invalid file!");</script>';
			return false;
		}
	}
}
?>