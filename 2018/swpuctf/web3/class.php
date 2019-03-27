<?php
// file_put_contents("php://stdout", "\r\n============================\r\n");

// class C1e4r {
// 	public $test;
// 	public $str;
// 	public function __construct($name) {
// 		file_put_contents("php://stdout", "C1e4r::__construct\r\n<br />\r\n");
// 		$this->str = $name;
// 	}
// 	public function __destruct() {
// 		file_put_contents("php://stdout", "C1e4r::__destruct::{$this->str}\r\n<br />\r\n");
// 		$this->test = $this->str;
// 		echo $this->test;
// 	}
// }

// class Show {
// 	public $source;
// 	public $str;
// 	public function __construct($file) {
// 		file_put_contents("php://stdout", "Show::__construct\r\n<br />\r\n");
// 		$this->source = $file;
// 		echo $this->source;
// 	}
// 	public function __toString() {
// 		file_put_contents("php://stdout", "Show::__toString\r\n<br />\r\n" . print_r($this, 1) . "\r\n");
// 		// file_put_contents("php://stdout", "Show::__toString\r\n<br />\r\n");
// 		// var_dump($this->str);
// 		// var_dump($this->str->source);
// 		// file_put_contents("php://stdout", "Show::__toString::{$content}\r\n<br />\r\n");
// 		$content = $this->str['str']->source;
// 		file_put_contents("php://stdout", "Show::__toString::{$content}\r\n<br />\r\n");
// 		return $content;
// 	}
// 	public function __set($key, $value) {
// 		file_put_contents("php://stdout", "Show::__set\r\n<br />\r\n");
// 		$this->$key = $value;
// 	}
// 	public function _show() {
// 		file_put_contents("php://stdout", "Show::_show\r\n<br />\r\n");
// 		if (preg_match('/http|https|file:|gopher|dict|\.\.|f1ag/i', $this->source)) {
// 			die('hacker!');
// 		} else {
// 			highlight_file($this->source);
// 		}

// 	}
// 	public function __wakeup() {
// 		file_put_contents("php://stdout", "Show::__wakeup::{$this->source}\r\n<br />\r\n");
// 		if (preg_match("/http|https|file:|gopher|dict|\.\./i", $this->source)) {
// 			echo "hacker~";
// 			$this->source = "index.php";
// 		}
// 	}
// }
// class Test {
// 	public $file;
// 	public $params;
// 	public function __construct() {
// 		file_put_contents("php://stdout", "Test::__construct\r\n<br />\r\n");
// 		$this->params = array();
// 	}
// 	public function __get($key) {
// 		file_put_contents("php://stdout", "Test::__get\r\n<br />\r\n");
// 		return $this->get($key);
// 	}
// 	public function get($key) {
// 		file_put_contents("php://stdout", "Test::get\r\n<br />\r\n");
// 		if (isset($this->params[$key])) {
// 			$value = $this->params[$key];
// 		} else {
// 			$value = "index.php";
// 		}
// 		return $this->file_get($value);
// 	}
// 	public function file_get($value) {
// 		file_put_contents("php://stdout", "Test::file_get\r\n<br />\r\n");
// 		$text = base64_encode(file_get_contents($value));
// 		return $text;
// 	}
// }
class C1e4r {
	public $test;
	public $str;
	public function __construct($name) {
		$this->str = $name;
	}
	public function __destruct() {
		$this->test = $this->str;
		echo $this->test;
	}
}

class Show {
	public $source;
	public $str;
	public function __construct($file) {
		$this->source = $file;
		echo $this->source;
	}
	public function __toString() {
		$content = $this->str['str']->source;
		return $content;
	}
	public function __set($key, $value) {
		$this->$key = $value;
	}
	public function _show() {
		if (preg_match('/http|https|file:|gopher|dict|\.\.|f1ag/i', $this->source)) {
			die('hacker!');
		} else {
			highlight_file($this->source);
		}

	}
	public function __wakeup() {
		if (preg_match("/http|https|file:|gopher|dict|\.\./i", $this->source)) {
			echo "hacker~";
			$this->source = "index.php";
		}
	}
}
class Test {
	public $file;
	public $params;
	public function __construct() {
		$this->params = array();
	}
	public function __get($key) {
		return $this->get($key);
	}
	public function get($key) {
		if (isset($this->params[$key])) {
			$value = $this->params[$key];
		} else {
			$value = "index.php";
		}
		return $this->file_get($value);
	}
	public function file_get($value) {
		$text = base64_encode(file_get_contents($value));
		return $text;
	}
}
?>