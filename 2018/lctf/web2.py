
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
# from config import create_app
import os
import urllib
import requests
import uuid

app = Flask("Core")


@app.route('/upload/<filename>', methods=['PUT'])
def upload_file(filename):
    name = request.cookies.get('name')
    pwd = request.cookies.get('pwd')
    if name != 'lctf' and pwd != str(uuid.getnode()):
        return "0"
    filename = urllib.unquote(filename)
    with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'w') as f:
        f.write(request.get_data(as_text=True))
        return "1"
    return "0"


@app.route('/', methods=['GET'])
def index():
    url = request.args.get('url', '')
    if url == '':
        # return render_template('index.html')
        return 'index.html'
    if "http" != url[: 4]:
        return "hacker"
    try:
        response = requests.get(url, timeout=10)
        response.encoding = 'utf-8'
        return response.text
    except Exception as e:
        print(e)
        return "Something Error"


@app.route('/source', methods=['GET'])
def get_source():
    return open(__file__).read()


if __name__ == '__main__':
    app.run(debug=True)
