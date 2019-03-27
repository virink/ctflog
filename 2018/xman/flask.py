from flask import Flask, make_response, render_template, render_template_string, request, url_for, abort
from jinja2 import Environment
import os
import time

app = Flask(__name__)
Jinja2 = Environment()
black_list = [
    'class', 'mro', 'read', '<', '>', '|', 'join'
]
sandbox_black_list = [
    'write', '.py', 'shutdown', '.sql', '.log', 'app'
    'os', 'sys', 'pop', 'del', 'rm', 'eval', 'exec', 'ls', 'cat',
    ';', '&&', 'catch_warnings', 'func_globals', 'pickle', 'import', 'subprocess', 'commands', 'input', 'execfile',
    'reload', 'compile', 'execfile', 'kill', 'func_code'
]


@app.errorhandler(500)
def internal_error(error):
    return handle_response(make_response(
        render_template(
            '500.html',
            error_url=request.path,
            server_name=request.host.split(':')[0],
            server_port=int(request.host.split(':')[1])),
        500)
    )


@app.before_request
def before_request():
    try:
        with open('/opt/log/access.log', 'ab') as log:
            log.write(
                '%s --- [ %s ] "%s %s %s" --- %s --- %s --- %s -\n' % (
                    request.environ['REMOTE_ADDR'],
                    time.strftime("%d/%B/%Y %H:%M:%S", time.localtime()),
                    request.environ['REQUEST_METHOD'],
                    request.full_path,
                    request.environ['SERVER_PROTOCOL'],
                    repr(request.cookies),
                    repr(request.form)[19:-1],
                    repr(request.headers)[15:-1],
                )
            )
    except Exception as e:
        with open('opt/log/error.log', 'ab') as log:
            log.write(e.message + '\n')
        abort(500)


# Fake PHP :>
def handle_response(response):
    response.headers['Server'] = 'Apache/2.4.10 (Debian)'
    response.headers['X-Powered-By'] = 'PHP/7.1.7'
    return response


@app.route('/.htaccess')
def forbidden():
    return handle_response(make_response(
        render_template(
            'forbidden.html',
            error_url=request.path,
            server_name=request.host.split(':')[0],
            server_port=int(request.host.split(':')[1])
        ),
        403
    ))


@app.route('/')
@app.route('/index.php')
def index():
    return handle_response(make_response(render_template('index.html')))


@app.errorhandler(404)
def not_found(error):
    try:
        for bad_string in sandbox_black_list:
            if bad_string in request.full_path:
                return '<script>alert("DO NOT JIAOSHI. You can not use it!");window.location.href="/";</script>'
        for bad_string in black_list:
            if bad_string in request.path:
                return '<script>alert("Nope! Find another way.");window.location.href="/";</script>'
        template = '''
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL %s was not found on this server.</p>
<hr>
<address>Apache/2.4.10 (Debian) Server at %s Port %d</address>
</body></html>
<!--Flag @ /opt/flag_1de36dff62a3a54ecfbc6e1fd2ef0ad1.txt-->
<!--Salt @ /opt/salt_b420e8cfb8862548e68459ae1d37a1d5.txt-->
    ''' % (
            request.path,
            request.host.split(':')[0],
            int(request.host.split(':')[1])
        )
        return handle_response(make_response(render_template_string(template), 404))
    except Exception as e:
        with open('/opt/log/error.log', 'ab') as log:
            log.write(e.message + '\n')
        abort(500)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=23333, debug=False)
