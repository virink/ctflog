<?php

error_reporting(E_ALL);

// ($_ = @$_GET['orange']) && @substr(file($_)[0], 0, 6) === '@<?php' ? include $_ : highlight_file(__FILE__);

// print_r(file_get_contents("php://memory"));

$_ = @$_GET['orange'];

var_dump($_);

$res = file($_);

// var_dump($res);

$res = substr($res[0], 0, 6);

var_dump($res);

include $_;