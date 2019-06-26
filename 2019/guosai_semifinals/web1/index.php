<?php
session_start();
if (!isset($_SESSION['login'])) {
	header("Location: login.php");
	die();
}
?>


<!DOCTYPE html>
<html>

<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<title>xxx</title>


<body>
    <nav aria-label="breadcrumb">
    <ol class="breadcrumb">
        <li class="active ml-auto"><a href="#"><?php echo $_SESSION['username']; ?></a></li>
    </ol>
</nav>
<form action="upload.php" method="post" enctype="multipart/form-data" >
    <input type="file" name="file">
    <input type="submit" value="upload">
</form>

<div class="top" id="toast-container"></div>

<?php
include "class.php";

$a = new FileList($_SESSION['sandbox']);
$a->Name();
$a->Size();
?>