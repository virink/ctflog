<?php

$t = file_get_contents("tcp.so");

$t = bin2hex($t);

file_put_contents("tcp.hex", $t);