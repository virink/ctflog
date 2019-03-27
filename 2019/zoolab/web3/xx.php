<?php

if (isset($_GET['_'])) {

	$_ = $_GET['_'];

	// $c = ;

	@file_put_contents("php://filter/write=convert.base64-decode|convert.base64-decode/resource=v.inc", "Q____Q" . base64_encode($_));

	echo file_get_contents("v.inc");

	echo "\r\n";

	echo "\r\n";
}
?>
