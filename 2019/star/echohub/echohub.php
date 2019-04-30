<?php
error_reporting(E_ALL);
define('O0', 'O');

require_once "sandbox.php";

$seed = time();
srand($seed);
define("INS_OFFSET", rand(0, 65535));

function aslr(&$func_addr, $O0O) {
	$func_addr = $func_addr + 0x60000000 + INS_OFFSET + 0x1;
}
$func = get_defined_functions()["internal"];
$func_ = array_flip($func);
array_walk($func_, "aslr");
$plt = array_flip($func_);

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

function genCanary() {
	$table = 'abcdefghijklmnopqrstuvwxyzABCDEFGHJKLMNPQEST123456789';
	$a1 = $table[rand(0, strlen($table) - 1)];
	$a2 = $table[rand(0, strlen($table) - 1)];
	$a3 = $table[rand(0, strlen($table) - 1)];
	return handleData($a1 . $a2 . $a3 . "\x00")[0];
}

$regs = array(
	"eax" => 0,
	"ebp" => 0,
	'esp' => 0,
	'eip' => 0,
);
$canary = genCanary();
$canarycheck = $canary;

function checkCanary() {
	global $canary;
	global $canarycheck;
	if ($canary != $canarycheck) {
		die("emmmmmm...Don\'t attack me!");
	}
}

Class Stack {
	private $ebp, $stack, $esp;

	public function __construct($phpinfo, $data) {
		global $regs;
		global $canary;
		$this->stack = array();
		$this->ebp = &$regs['ebp']; // 0
		$this->esp = &$regs['esp']; // 0
		$this->ebp = 0xfffe0000 + rand(0, 0xffff);
		$this->stack[$this->ebp - 0x4] = &$canary;
		$this->stack[$this->ebp] = $this->ebp + rand(0, 0xffff);
		$this->esp = $this->ebp - (rand(32, 96) * 4);
		$this->stack[$this->ebp + 0x4] = dechex($phpinfo);
		if ($data != NULL) {
			$this->pushdata($data);
		}
	}

	public function pushdata($args) {
		$args = handleData($args);
		for ($i = 0; $i < count($args); $i++) {
			$this->stack[$this->esp + ($i * 4)] = $args[$i];
			//no args in my stack haha
			checkCanary();
		}
	}

	public function recoverData($OOO0O) {
		return hex2bin(strrev($OOO0O));
	}

	public function outputdata() {
		global $regs;
		echo "root says: ";
		while (1) {
			if ($this->esp == $this->ebp - 4) {
				break;
			}
			$this->pop('eax');
			$OOOOO = $this->recoverData($regs['eax']);
			$O00000 = explode("\x00", $OOOOO);
			echo $O00000[0];
			if (count($O00000) > 1) {
				break;
			}
		}
	}

	public function getDataFromReg($arg1) {
		global $regs;
		$O00O00 = $this->recoverData($regs[$arg1]);
		$O00O0O = explode("\x00", $O00O00);
		return $O00O0O[0];
	}

	public function pop($arg) {
		global $regs;
		$regs[$arg] = $this->stack[$this->esp];
		$this->esp += 4;
	}

	public function call() {
		global $regs;
		global $plt;
		$point = hexdec($regs['eip']);
		if (isset($_REQUEST[$point])) {
			$this->pop('eax');
			$O0O000 = (int) $this->getDataFromReg('eax');
			$O0O00O = array();
			for ($i = 0; $i < $O0O000; $i++) {
				$this->pop('eax');
				$O0O0OO = $this->getDataFromReg('eax');
				array_push($O0O00O, $_REQUEST[$O0O0OO]);
			}
			call_user_func_array($plt[$point], $O0O00O);
		} else {
			call_user_func($plt[$point]);
		}

	}

	public function push($reg) {
		global $regs;
		$reg_data = $regs[$reg];
		if (hex2bin(strrev($reg_data)) == NULL) {
			die('data error');
		}
		$this->stack[$this->esp] = $reg_data;
		$this->esp -= 4;

	}

	public function __call($OO000O, $OO00O0) {
		checkCanary();
	}

	public function ret() {
		global $regs;
		$this->esp = $this->ebp;
		$this->pop('ebp');
		$this->pop('eip');
		$this->call();
	}
}

if (isset($_POST["data"])) {
	$phpinfo_addr = array_search("phpinfo", $plt);
	$gets = $_POST["data"];
	$main_stack = new Stack($phpinfo_addr, $gets);
	echo "--------------------output---------------------\x3C\/br\x3E\x3C\/br\x3E";
	$main_stack->outputdata();
	echo "\x3C\/br\x3E\x3C\/br\x3E------------------phpinfo()------------------\x3C\/br\x3E";
	$main_stack->ret();
}
