<?php
$classes = get_declared_classes();
foreach ($classes as $class) {
	$methods = get_class_methods($class);
	foreach ($methods as $method) {
		if (in_array($method, array(
			'__destruct',
			'__toString',
			'__wakeup',
			// '__call',
			// '__callStatic',
			// '__get',
			// '__set',
			// '__isset',
			// '__unset',
			// '__invoke',
			// '__set_state',
		))) {
			print $class . '::' . $method . "\n";
		}
	}
}

class T {
	var $test = "test";
}
$aa = new T();
echo serialize($aa);