<?php

class Test {
	public function __wakeup() {
		// phpinfo();
		// file_put_contents("/path/to/2018/huwangbei/test.xxx", "xxxxxx");
		// Flash::success('__wakeup');
		echo "__wakeup";
	}
	public function __destruct() {
		// phpinfo();
		// file_put_contents("/path/to/2018/huwangbei/test.xxx", "xxxxxx");
		// Flash::success('__destruct');
		echo "__destruct";
	}
}

file_exists("phar://x.gif");