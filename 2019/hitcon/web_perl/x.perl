#!/usr/bin/env perl
#
use lib '/usr/local/var/www/cgi-bin/web_perl/';
use strict;

use DSSafe;

system("/usr/local/var/www/cgi-bin/web_perl/\$ls\$");
system("/usr/local/var/www/cgi-bin/web_perl/\$\ls\$");
system("/usr/local/var/www/cgi-bin/web_perl/\$\\ls\$");