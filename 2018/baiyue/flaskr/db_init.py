# -*- coding: UTF-8 -*-
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext
from flaskr import db

from flask_sqlalchemy import SQLAlchemy


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)


    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class secert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    secert = db.Column(db.String(80), unique=True)

    def __init__(self, secert):
        self.secert = secert

    def __repr__(self):
        return '<secert %r>' % self.secert


def init_db():
    db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES 
        )

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

    db.close()

def init_app(app):
    app.cli.add_command(init_db_command)

@click.command('init-db')
@with_appcontext
def init_db_command():
    """ build database """
    init_db()
    click.echo('Initialized the database.')