#!/usr/bin/perl -w
use strict;
use warnings;
my $prog="/readflag";
# my $prog="./x";
# my $prog="./xx";
my $prog="./rf.elf";
local(*COUT, *CIN, *CERR);
# use IPC::Open2;
# my $pid = open2(*COUT, *CIN, "$prog");
use IPC::Open3;
my $pid = open3(*CIN, *COUT, *CERR, "$prog");
my $ret;
my $op;
my $reader = IO::Select->new();

COUT->autoflush;
CIN->autoflush;
STDOUT->autoflush;

# Solve the easy challenge first
$op = <COUT>;
print STDOUT "<< $op\n";
# ((((()))))
$op = <COUT>;
print STDOUT "<< $op\n";
if ($op =~ /\(\(.*?\)\)/){
    $op = substr($op,0,length($op)-1);
    $ret = eval $op;
    print STDOUT "$op = $ret\n\n";
}
$op = <COUT>;
print STDOUT "<< $op\n";
if ($op =~ /input your answer: /){
    print CIN "$ret\n\n";
    close CIN;
}
$op = <COUT>;
print STDOUT "<< $op\n";
$op = <COUT>;
print STDOUT "<< $op\n";
$op = <COUT>;
print STDOUT "<< $op\n";
waitpid( $pid, 0 );
my $child_exit_status = $? >> 8;
# $op = <COUT>;
# print STDOUT "<< $op\n";
# while (my $op = <COUT>)
# {
#     print STDOUT ">> $op\n";
#     if ($op =~ /\(\(.*?\)\)/){
#         $op = substr($op,0,length($op)-1);
#         $ret = eval $op;
#         print STDOUT "$op = $ret\n\n";
#     }elsif($op =~ /input your answer: /){
#         # print STDOUT "$ret\n";
#         print STDOUT "answer = $ret (" . ref($ret) . ")\n";
#         print STDOUT "=========\n";
#         print CIN "$ret\\n\n";
#         print STDOUT "=========\n";
#         close CIN;
#         print STDOUT "=========\n";
#         print STDOUT "=========\n";
#     }
# }
print STDOUT "=========\n";
waitpid( $pid, 0 );
my $child_exit_status = $? >> 8;
