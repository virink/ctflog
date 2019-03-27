import flask
import datetime
import os
from bookhub import login_manager, migrate, db
from bookhub.helper import ip_address_in
from werkzeug.security import generate_password_hash, check_password_hash

__all__ = ['User', 'Book']


def op(v):
    print('-' * 30)
    print(v)
    print('-' * 30)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128))

    def __repr__(self):
        return '<User %r>' % self.username

    def set_password(self, password):
        self.password = generate_password_hash(password)
        db.session.commit()

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return str(self.id)

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    img = db.Column(db.String(256))
    description = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return '<Book %r>' % self.title


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


@login_manager.unauthorized_handler
def unauthorized_handler():
    return flask.redirect(flask.url_for('user.login'), code=303)
