from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import Base, login, mysql
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, backref


class Followers(Base):
    __tablename__ = 'followers'
    follower_id = Column('follower_id', Integer, ForeignKey('user.id'))
    followed_id = Column('followed_id', Integer, ForeignKey('user.id'))


class User(UserMixin, Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))
    posts = relationship('Post', backref='author', lazy='dynamic')
    note = Column(String(140))
    last_seen = Column(Date, default=datetime.utcnow)
    followed = relationship(
        'User', secondary=Followers,
        primaryjoin=(Followers.follower_id == id),
        secondaryjoin=(Followers.followed_id == id),
        backref=backref('Followers', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def follow(self, user):
        if not self.is_following(user):
            return mysql.Add("followers", ("%d" % self.id, "%d" % user.id))

    def unfollow(self, user):
        if self.is_following(user):
            return mysql.Del("followers", {"follower_id": self.id, "followed_id": user.id})

    def is_following(self, user):
        res = mysql.One(
            'followers', {"followed_id": user.id, "follower_id": self.id})
        return True if (res != 0 and res != 1) else False

    def get_followers(self):
        return mysql.All('followers', {"followed_id": self.id}, ['follower_id'])

    def get_followed(self):
        return mysql.All('followers', {"follower_id": self.id}, ['followed_id'])

    def followed_posts(self):
        followedid = mysql.All(
            'followers', {"follower_id": self.id}, ['followed_id'])
        tmp = ""
        for i in followedid:
            tmp += str(i[0]) + ","
        followed = mysql.Sel('post', {
                             "user_id": "(%s)" % tmp[:-1]} if tmp[:-1] != "" else {"user_id": "(-1)"}, where_symbols="in")
        own = mysql.Sel('post', {"user_id": self.id}, order=["id desc"])
        posts = mysql.Unionall([followed, own])
        return posts


@login.user_loader
def load_user(id):
    msg = mysql.One("user", {"id": id})
    if msg != 0 and msg != -1:
        user = User(id=msg[0], username=msg[1], email=msg[2],
                    password_hash=msg[3], note=msg[4], last_seen=msg[5])
        return user
    else:
        return None


def load_user_by_username(username):
    msg = mysql.One("user", {"username": "'%s'" % username})
    if msg != 0 and msg != -1:
        user = User(id=msg[0], username=msg[1], email=msg[2],
                    password_hash=msg[3], note=msg[4], last_seen=msg[5])
        return user
    else:
        return msg


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    body = Column(String(140))
    user_id = Column(Integer, ForeignKey('user.id'))
    timestamp = Column(Date, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Post {}>'.format(self.body)
