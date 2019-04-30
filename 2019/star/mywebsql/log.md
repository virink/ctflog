admin/admin

/var/lib/mysql/5dcd0f91b39a.log

hostname 5dcd0f91b39a

log_error   /var/log/mysql/error.log

backup database -> shell.php

/readflag
    
STDIN/STDOUT -> socket

perl open3 双向管道没成功，**有机会研究一下原因**

挖坑：
    用 perl 实现 **STDIN/STDOUT -> socket**