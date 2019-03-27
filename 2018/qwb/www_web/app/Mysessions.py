import sys
from uuid import uuid4
from flask.sessions import SessionInterface as FlaskSessionInterface
from flask.sessions import SessionMixin
from werkzeug.datastructures import CallbackDict
from itsdangerous import Signer, BadSignature, want_bytes
from Mycache import FileSystemCache

PY2 = sys.version_info[0] == 2
if not PY2:
    text_type = str
else:
    text_type = unicode


def total_seconds(td):
    return td.days * 60 * 60 * 24 + td.seconds


class ServerSideSession(CallbackDict, SessionMixin):

    def __init__(self, initial=None, sid=None, permanent=None):
        def on_update(self):
            self.modified = True
        CallbackDict.__init__(self, initial, on_update)
        self.sid = sid
        if permanent:
            self.permanent = permanent
        self.modified = False


class FileSystemSession(ServerSideSession):
    pass


class SessionInterface(FlaskSessionInterface):

    def _generate_sid(self):
        return str(uuid4())

    def _get_signer(self, app):
        if not app.secret_key:
            return None
        return Signer(app.secret_key, salt='flask-session',
                      key_derivation='hmac')


class FileSystemSessionInterface(SessionInterface):
    session_class = FileSystemSession

    def __init__(self, cache_dir, threshold, mode, key_prefix="bdwsessions",
                 use_signer=False, permanent=True):

        self.cache = FileSystemCache(cache_dir, threshold=threshold, mode=mode)
        self.key_prefix = key_prefix
        self.use_signer = use_signer
        self.permanent = permanent

    def open_session(self, app, request):
        sid = request.cookies.get(app.session_cookie_name)
        if not sid:
            sid = self._generate_sid()
            return self.session_class(sid=sid, permanent=self.permanent)
        if self.use_signer:
            signer = self._get_signer(app)
            if signer is None:
                return None
            try:
                sid_as_bytes = signer.unsign(sid)
                sid = sid_as_bytes.decode()
            except BadSignature:
                sid = self._generate_sid()
                return self.session_class(sid=sid, permanent=self.permanent)
        data = self.cache.get(self.key_prefix + sid)
        if data is not None:
            return self.session_class(data, sid=sid)
        return self.session_class(sid=sid, permanent=self.permanent)

    def save_session(self, app, session, response):
        domain = self.get_cookie_domain(app)
        path = self.get_cookie_path(app)
        if not session:
            if session.modified:
                self.cache.delete(self.key_prefix + session.sid)
                response.delete_cookie(app.session_cookie_name,
                                       domain=domain, path=path)
            return

        httponly = self.get_cookie_httponly(app)
        secure = self.get_cookie_secure(app)
        expires = self.get_expiration_time(app, session)
        data = dict(session)
        self.cache.set(self.key_prefix + session.sid, data,
                       total_seconds(app.permanent_session_lifetime))
        if self.use_signer:
            session_id = self._get_signer(app).sign(want_bytes(session.sid))
        else:
            session_id = session.sid
        response.set_cookie(app.session_cookie_name, session_id,
                            expires=expires, httponly=httponly,
                            domain=domain, path=path, secure=secure)
