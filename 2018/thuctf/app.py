def ses():
    session.get('username', 'guest')
    session['username'] = username
    if 'admin' == username:
