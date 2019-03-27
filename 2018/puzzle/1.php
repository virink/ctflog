<?php
$action = $_GET['action'] ?? '';
$arg = $_GET['arg'] ?? '';

if (preg_match('/^[a-z0-9_]*$/isD', $action, $m)) {
	var_dump($m);
	show_source(__FILE__);
} else {
	$action('', $arg);
}
// action=class::method
// arg=fuck