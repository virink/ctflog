#!/usr/bin/perl -w
use strict;
use warnings;
use Socket;
use IO::Socket;

# my $prog="/readflag";
my $prog="./x";
# local(*COUT, *CIN, *CERR);
# use IPC::Open3;
# my $pid = open3(*CIN, *COUT, *CERR, "$prog");
# my $ret;
# my $op;
my $ret = undef;
my $message = undef;
my $server  = undef;

# my $port = 12321 ;
# socket(SOCKET, PF_INET, SOCK_STREAM, getprotobyname('tcp')) or die "can't open socket $!\n";
# setsockopt(SOCKET, SOL_SOCKET, SO_REUSEADDR, 1) or die "can't setting SO_REUSEADDR $!\n";
# bind( SOCKET, pack_sockaddr_in($port, inet_aton("0.0.0.0"))) or die "can't bind $port! \n";
# listen(SOCKET, 5) or die "listen: $!";
# print "-> $port\n";
# while (my $client = accept(NEW_SOCKET, SOCKET)) {
#     print "Connection recieved\n";
#     $ret = $client->recv($message, 100);
#     print STDOUT "$message\n";
#     printf "$message: %d/n", length($message);
#     print NEW_SOCKET "Good Job";
#     close NEW_SOCKET;
# }

my $lsock = IO::Socket::INET->new(LocalPort => 12321,
                                  Type      => SOCK_STREAM,
                                  Reuse     => 1,
                                  Listen    => 5 )
            or die "Couldn't be a tcp server on port 12321 : $@/n";
print "Listen 12321\n";
$server = $lsock->accept();
print "$server\n";
$ret = $server->recv($message, 1024);
printf ">> $message: %d/n", length($message);
$ret = $server->recv($message, 1024);
printf ">> $message: %d/n", length($message);
close($server);
close($lsock);

# COUT->autoflush;
# CIN->autoflush;
# STDOUT->autoflush;

# # Solve the easy challenge first
# $op = <COUT>;
# print STDOUT "<< $op\n";
# # ((((()))))
# $op = <COUT>;
# print STDOUT "<< $op\n";
# if ($op =~ /\(\(.*?\)\)/){
#     $op = substr($op,0,length($op)-1);
#     $ret = eval $op;
#     print STDOUT "$op = $ret\n\n";
# }
# $op = <COUT>;
# print STDOUT "<< $op\n";
# if ($op =~ /input your answer: /){
#     print CIN "$ret\n\n";
#     close CIN;
# }
# $op = <COUT>;
# print STDOUT "<< $op\n";
# $op = <COUT>;
# print STDOUT "<< $op\n";
# $op = <COUT>;
# print STDOUT "<< $op\n";
# waitpid( $pid, 0 );
# my $child_exit_status = $? >> 8;
