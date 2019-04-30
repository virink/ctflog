#!/bin/sh
# service --status-all | awk '{print $4}'| xargs -i 
service apache2 restart;
service php7.3-fpm restart;

tail -f /dev/null
