#!flask/bin/python
from os import *
from sys import *
import datetime
from hashlib import md5
from pickle import Unpickler as Unpkler
from pickle import *


class Mysql_Operate():

    def __init__(self, Base, engine, dbsession):
        self.db_session = dbsession()
        self.Base = Base
        self.engine = engine

    def Add(self, tablename, values):
        sql = "insert into " + tablename + " "
        sql += "values ("
        sql += "".join(i + "," for i in values)[:-1]
        sql += ")"
        # print(sql)
        try:
            self.db_session.execute(sql)
            self.db_session.commit()
            return 1
        except:
            return 0

    def Del(self, tablename, where):
        sql = "delete from " + tablename + " "
        sql += "where " + \
            "".join(i + "=" + str(where[i]) + " and " for i in where)[:-4]
        try:
            self.db_session.execute(sql)
            self.db_session.commit()
            return 1
        except:
            return 0

    def Mod(self, tablemame, where, values):
        sql = "update " + tablemame + " "
        sql += "set " + \
            "".join(i + "=" + str(values[i]) + "," for i in values)[:-1] + " "
        sql += "where " + \
            "".join(i + "=" + str(where[i]) + " and " for i in where)[:-4]
        # print
        # print sql
        # print
        try:
            self.db_session.execute(sql)
            self.db_session.commit()
            return 1
        except:
            return 0

    def Sel(self, tablename, where={}, feildname=["*"], order="", where_symbols="=", l="and"):
        sql = "select "
        sql += "".join(i + "," for i in feildname)[:-1] + " "
        sql += "from " + tablename + " "
        if where != {}:
            sql += "where " + "".join(i + " " + where_symbols + " " +
                                      str(where[i]) + " " + l + " " for i in where)[:-4]
        if order != "":
            sql += "order by " + "".join(i + "," for i in order)[:-1]
        return sql

    def All(self, tablename, where={}, feildname=["*"], order="", where_symbols="=", l="and"):
        sql = self.Sel(tablename, where, feildname, order, where_symbols, l)
        try:
            res = self.db_session.execute(sql).fetchall()
            if res == None:
                return []
            return res
        except:
            return -1

    def One(self, tablename, where={}, feildname=["*"], order="", where_symbols="=", l="and"):
        sql = self.Sel(tablename, where, feildname, order, where_symbols, l)
        try:
            res = self.db_session.execute(sql).fetchone()
            if res == None:
                return 0
            return res
        except Exception as e:
            print(e)
            return -1

    def Unionall(self, param):
        sql = "".join(i + " union " for i in param)[:-6]
        try:
            res = self.db_session.execute(sql).fetchall()
            if res == None:
                return []
            return res
        except:
            return -1

    def Unionone(self, param):
        sql = "".join(i + " union " for i in param)[:-6]
        try:
            res = self.db_session.execute(sql).fetchone()
            if res == None:
                return []
            return res
        except:
            return -1

    def Init_db(self):
        self.Base.metadata.create_all(self.engine)

    def Drop_db(self):
        self.Base.metadata.drop_all(self.engine)


def now():
    return datetime.datetime.utcnow().strftime("%Y-%m-%d")


def avatar(email, size):
    digest = md5(email.lower().encode('utf-8')).hexdigest()
    return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
        digest, size)


black_type_list = [eval, execfile, compile, system, open, file, popen, popen2, popen3, popen4, fdopen,
                   tmpfile, fchmod, fchown, pipe, chdir, fchdir, chroot, chmod, chown, link,
                   lchown, listdir, lstat, mkfifo, mknod, mkdir, makedirs, readlink, remove, removedirs,
                   rename, renames, rmdir, tempnam, tmpnam, unlink, walk, execl, execle, execlp, execv,
                   execve, execvp, execvpe, exit, fork, forkpty, kill, nice, spawnl, spawnle, spawnlp, spawnlpe,
                   spawnv, spawnve, spawnvp, spawnvpe, load, loads]


class FilterException(Exception):

    def __init__(self, value):
        super(FilterException, self).__init__(
            'the callable object {value} is not allowed'.format(value=str(value)))


def _hook_call(func):
    def wrapper(*args, **kwargs):
        print args[0].stack
        if args[0].stack[-2] in black_type_list:
            raise FilterException(args[0].stack[-2])
        return func(*args, **kwargs)
    return wrapper


def load(file):
    unpkler = Unpkler(file)
    unpkler.dispatch[REDUCE] = _hook_call(unpkler.dispatch[REDUCE])
    return Unpkler(file).load()
