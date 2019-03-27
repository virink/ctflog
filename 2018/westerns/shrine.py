
import flask
import os

app = flask.Flask(__name__)
app.config['FLAG'] = 'test_flag'


@app.route('/')
def index():
    return open(__file__).read()


@app.route('/shrine/<path:shrine>')
def shrine(shrine):
    # print(dir(flask.g.__class__.__dict__['__dict__']))
    # print(flask.g.__class__.__dict__['__dict__'])

    def safe_jinja(s):
        s = s.replace('(', '').replace(')', '')
        blacklist = ['config', 'self']
        return ''.join(['{{% set {}=None%}}'.format(c) for c in blacklist]) + s
    return flask.render_template_string(safe_jinja(shrine))

if __name__ == '__main__':
    app.run(debug=True)
