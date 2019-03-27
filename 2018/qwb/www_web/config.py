import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'you will never guess'
    SQLALCHEMY_DATABASE_URI = "mysql://root:@127.0.0.1/flask_web?charset=utf8"
    # SQLALCHEMY_DATABASE_URI = "sqlite:///data.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BOOTSTRAP_SERVE_LOCAL = 'True'
    POSTS_PER_PAGE = 25
    SESSION_TYPE = "filesystem"
    SESSION_FILE_THRESHOLD = 10000
    SESSION_FILE_DIR = "/tmp/ffff"
    SESSION_FILE_MODE = 0660
    SESSION_PERMANENT = True
