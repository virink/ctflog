# -*- coding: UTF-8 -*-
import os

from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy  # flask_sqlalchemy==2.2

db = SQLAlchemy()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config.from_mapping(
        DEBUG=True,
        SECRET_KEY='test',
        DATABASE=basedir+'/flaskr.sqlite',
        SQLALCHEMY_DATABASE_URI='sqlite:///flaskr.sqlite',
        SQLALCHEMY_TRACK_MODIFICATIONS=True
    )
    basedir = os.path.abspath(os.path.dirname(__file__))

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the folder exists
    try:
        os.makedirs(basedir)
    except OSError:
        pass

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    from . import db_init
    db_init.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp_auth)

    from . import secert
    app.register_blueprint(secert.bp_secert)

    @app.route("/www-zip")
    def get_source():
        with open(basedir+"/www.zip", 'rb') as f:
            file = f.read()
        response = make_response(file)
        response.headers['Content-Type'] = "application/zip"
        return response

    return app
