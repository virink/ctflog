<?php
error_reporting(0);
include 'config.php';
function waf($s) {
	if (preg_match_all("/select|union|or|and|\.|\\\\| |\)|\'|\"|in|\*|-|do|set|case|regexp|like|prepare.|.execute|\/|#|\\0/i", $s, $m) != false || strlen($s) > 10000) {
		var_dump($m);
		die("waf");
	}
	return $s;
}

$_REQUEST['v'] = str_replace(" ", "\t", $_REQUEST['v']);
$_REQUEST['i'] = str_replace(" ", "\t", $_REQUEST['i']);

$id = $_REQUEST['i'] ? waf($_REQUEST['i']) : rand(1, 2);
$v = $_REQUEST['v'] ? waf($_REQUEST['v']) : 'ers';

$sql = "desc `us{$v}`";
var_dump($sql);
echo "<br />\r\n";
if (!$conn->query($sql)) {
	die("no such table<br />\r\n");
}
$sql = "SELECT * FROM  us{$v} where id = '$id'";
var_dump($sql);
echo "<br />\r\n";
$result = $conn->query($sql);
if (!$result) {
	// print_r($conn->errorInfo());
	die("<br />\r\nerror:<br />\r\n");
}
// print_r($result->fetchAll());
foreach ($result as $row) {
	print " $row[0] --- $row[1] <br />\r\n";
}
?>