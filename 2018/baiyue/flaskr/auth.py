# -*- coding: UTF-8 -*-
import os
import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from flaskr import db
from flaskr.db_init import user, secert

from werkzeug.security import check_password_hash, generate_password_hash


bp_auth = Blueprint('auth', __name__, url_prefix='/')

def login_check(view):
	@functools.wraps(view)
	def wrapped_view(**kwargs):
		if g.user is None:
			flash(u'请先登陆')
			return redirect(url_for('auth.login'))

		return view(**kwargs)
	return wrapped_view
	
@bp_auth.route('/register',methods = ['GET','POST'])
def register():
	if request.method=='POST':
		username = request.form.get('username')
		passwd = request.form.get('passwd')
		repasswd = request.form.get('repasswd')
		email = request.form.get('email')
		error = None

		if not username:
			error = u'请输入用户名'
		elif not passwd:
			error = u'请输入密码'
		elif not email:
			error = u'请输入邮箱'
		elif repasswd!=passwd:
			error = u'两次密码不匹配'
		elif user.query.filter_by(username=username).first() is not None:
			error = u'用户名:%s已被注册'%username

		if error is None:
			user_in = user(username, generate_password_hash(passwd), email)
			serect_in = secert("you should login in admin.")
			db.session.add(user_in)
			db.session.add(serect_in)
			db.session.commit()
			
			flash(u'注册成功')

			return redirect(url_for('auth.login'))

		flash(error)

	return render_template('auth/register.html')

@bp_auth.route('/')
@bp_auth.route('/index')
@bp_auth.route('/login',methods = ['GET','POST'])
def login():
	if request.method == 'POST':
		username = request.form.get('username')
		passwd = request.form.get('passwd')
		error = None

		if not username:
			error = u'请输入用户名'
		elif not passwd:
			error = u'请输入密码'
		else:
			user_info = user.query.filter_by(username=username).first()
			if user_info is None:
				error = u'%s未被注册'%username

		if error is None:
			if check_password_hash(user_info.password,passwd):
				session.clear()
				session['user_id'] = user_info.id
				flash(u'登陆成功')
				return redirect(url_for('secert.views_info')+'?id='+str(user_info.id))
			else:
				error = u'账号密码错误'
		flash(error)

	return render_template('auth/login.html')

@bp_auth.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('auth.login'))

@bp_auth.route('/flag')
@login_check
def get_flag():
	if(g.user.username=="admin"):
		with open(os.path.dirname(__file__)+'/flag','rb') as f:
			flag = f.read()
		return flag
	return "Not admin!!"


@bp_auth.before_app_request
def load_logged_in_user():
	user_id = session.get('user_id')

	if user_id is None:
		g.user = None
	else:
		g.user = user.query.filter_by(id = session['user_id']).first()



