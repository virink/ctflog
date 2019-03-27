#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    make_response,
)
from PIL import Image
import tempfile
import os
import logging
logging.basicConfig(level=logging.NOTSET)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/source')
def source():
    return open(__file__).read()


@app.route('/conv', methods=['POST'])
def conv():
    f = request.files.get('image', None)
    # filename content
    # print(f)
    if not f:
        return redirect(url_for('index'))
    ext = f.filename.split('.')[-1]
    fname = tempfile.mktemp("emoji")
    fname = "{}.{}".format(fname, ext)
    f.save(fname)
    # print("ext=%s\nfname=%s" % (ext, fname))
    img = Image.open(fname)
    w, h = img.size
    r = 128 / max(w, h)
    newimg = img.resize((int(w * r), int(h * r)))
    newimg.save(fname)
    response = make_response()
    response.data = open(fname, "rb").read()
    response.headers[
        'Content-Disposition'] = 'attachment; filename=emoji_{}'.format(f.filename)
    os.unlink(fname)
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
