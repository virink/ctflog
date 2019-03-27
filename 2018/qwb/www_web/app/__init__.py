from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

import pymysql
pymysql.install_as_MySQLdb()

from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base, DeferredReflection
from others import Mysql_Operate
from Mysessions import FileSystemSessionInterface

app = Flask(__name__)
app.config.from_object(Config)

engine = create_engine(
    app.config['SQLALCHEMY_DATABASE_URI'], convert_unicode=True)
db_session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

Base = declarative_base(cls=DeferredReflection)
Base.query = db_session.query_property()
mysql = Mysql_Operate(Base, engine, db_session)


login = LoginManager(app)
login.login_view = 'login'
bootstrap = Bootstrap(app)
moment = Moment(app)

app.session_interface = FileSystemSessionInterface(
    app.config['SESSION_FILE_DIR'], app.config['SESSION_FILE_THRESHOLD'],
    app.config['SESSION_FILE_MODE'])

from app import routes, models, errors

mysql.Init_db()
