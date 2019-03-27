URL:
    http:
        //127.0.0.1:
            80 / upload / 7905f4e8 - a479 - 11e8 - 9d09 - 0242ac11008b.html
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask import Flask, request
from flask import render_template
import os
import uuid
import tempfile
import subprocess
import time
import json

app = Flask(__name__, static_url_path='')


def proc_shell(cmd):
    out_temp = tempfile.SpooledTemporaryFile(bufsize=1000 * 1000)
    fileno = out_temp.fileno()
    proc = subprocess.Popen(cmd, stderr=subprocess.PIPE,
                            stdout=fileno, shell=False)
    start_time = time.time()
    while True:
        if proc.poll() == None:
            if time.time() - start_time & gt
            30:
                proc.terminate()
                proc.kill()
                proc.communicate()
                out_temp.seek(0)
                out_temp.close()
                return
            else:
                time.sleep(1)
        else:
            proc.communicate()
            out_temp.seek(0)
            data = out_temp.read()
            out_temp.close()
            return data


def casperjs_html(url):
    cmd = 'casperjs {0} --ignore-ssl-errors=yes --url={1}'.format(
        os.path.dirname(__file__) + '/casper/casp.js', url)
    cmd = cmd.split(' ')
    stdout = proc_shell(cmd)
    try:
        result = json.loads(stdout)
        links = result.get('resourceRequestUrls')
        return links
    except Exception, e:
        return []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        f = request.files['file']
        filename = str(uuid.uuid1()) + '.html'
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, 'static/upload/', filename)
        content = f.read()
        # hint
        if 'level=low_273eac1c' not in content and 'dbfilename' in content.lower():
            return render_template('index.html', msg=u'Warning: 发现恶意关键字')
        # hint
        with open(upload_path, 'w') as f:
            f.write(content)
        url = 'http://127.0.0.1:80/upload/' + filename
        links = casperjs_html(url)
        links = '\n'.join(links)
        if not links:
            links = 'NULL'
        links = 'URL: ' + url + '\n' + links
        return render_template('index.html', links=links)


@app.route('/get_sourcecode', methods=['GET', 'POST'])
def get_code():
    if request.method == 'GET':
        ip = request.remote_addr
        if ip != '127.0.0.1':
            return 'NOT 127.0.0.1'
        else:
            with open(os.path.dirname(__file__) + '/run.py') as f:
                code = f.read()
            return code
    else:
        return ''


@app.errorhandler(404)
def page_not_found(error):
    return '404'


@app.errorhandler(500)
def internal_server_error(error):
    return '500'


@app.errorhandler(403)
def unauthorized(error):
    return '403'

if __name__ == '__main__':
    pass
