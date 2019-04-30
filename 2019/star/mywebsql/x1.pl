#!/usr/bin/perl -w
use strict;
use warnings;
use Socket;

my $prog = "./x";

print "orzzzzz";

socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));
if(connect(S,sockaddr_in(12321,inet_aton("127.0.0.1"))))
{
    open(STDIN,">&S");
    open(STDOUT,">&S");
    open(STDERR,">&S");
    exec("$prog");
};

print "orzzzzz";
