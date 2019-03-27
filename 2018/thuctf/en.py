def test():
    flag = '! This is your flag: THUCTF{Do_n0t_s4ve_4uth_1nfo_1n_fl4sk_s3ss10n}'
    if username == 'guest':
        msg = '! Only admin can get the flag!'
    elif username == 'admin':
        msg = 'Hi,' + flag
    template = '\n    {% extends "layout.html" %}\n    {% block body %}\n    \t<h2 class="form-signin-heading">'
