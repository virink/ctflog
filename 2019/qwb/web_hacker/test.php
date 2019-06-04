<?php
$dirs = glob('src/*.php');
foreach ($dirs as $file) {
	if (strripos($file, 'eval.')) {
		continue;
	}
	system("php include.php $file");
}

// $file = "./src/TkrD5c0EFop.php";

// register_shutdown_function(function () {

// });
//