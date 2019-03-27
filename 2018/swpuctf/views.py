def register_views(app):
    @app.before_request
    def reset_account():
        if request.path == '/signup' or request.path == '/login':
            return
        uname = username = session.get('username')
        u = User.query.filter_by(username=uname).first()
        if u:
            g.u = u
            g.flag = 'swpuctf{xxxxxxxxxxxxxx}'
            if uname == 'admin':
                return
            now = int(time())
            if (now - u.ts >= 600):
                u.balance = 10000
                u.count = 0
                u.ts = now
                u.save()
                session['balance'] = 10000
                session['count'] = 0


@app.route('/getflag', methods=('POST',))
@login_required
def getflag():
    u = getattr(g, 'u')
    if not u or u.balance < 1000000:
        return '{"s": -1, "msg": "error"}'
    field = request.form.get('field', 'username')
    mhash = hashlib.sha256(
        ('swpu++{0.' + field + '}').encode('utf-8')).hexdigest()
    jdata = '{{"{0}":' + '"{1.' + field + '}", "hash": "{2}"}}'
    return jdata.format(field, g.u, mhash)


