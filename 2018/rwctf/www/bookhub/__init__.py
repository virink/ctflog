from dotenv import load_dotenv
load_dotenv(verbose=True)

import os
import redis
from flask_login import LoginManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from flask_wtf.csrf import CSRFProtect


def op(v):
    print('-' * 30)
    print(v)
    print('-' * 30)

base_dir = os.path.dirname(os.path.abspath(__file__))
rds = redis.StrictRedis.from_url('redis://127.0.0.1:6379/0')


SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1/rwctf"
# SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'designed_and_built_by_phith0n'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SESSION_COOKIE_NAME'] = 'bookhub-session'
app.config['REMEMBER_COOKIE_NAME'] = 'bookhub-remember-me'
app.config['REMEMBER_COOKIE_HTTPONLY'] = True
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_KEY_PREFIX'] = 'bookhub:session:'
app.config['SESSION_REDIS'] = rds
app.config['DEBUG'] = True

db = SQLAlchemy(app)
login_manager = LoginManager(app)
migrate = Migrate(app, db)
sess = Session(app)
csrf = CSRFProtect(app)
