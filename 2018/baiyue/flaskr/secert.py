# -*- coding: UTF-8 -*-
# import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app

from . import db
from .db_init import user, secert
from .auth import login_check

from flask_sqlalchemy import SQLAlchemy


bp_secert = Blueprint('secert', __name__, url_prefix='/')

@bp_secert.route('/views',methods = ['GET','POST'])
@login_check
def views_info():
	view_id = request.args.get('id')
	if not view_id:
		view_id = session.get('user_id')

	user_m = user.query.filter_by(id=view_id).first()

	if user_m is None:
		flash(u"该用户未注册")
		return render_template('secert/views.html')

	if str(session.get('user_id'))==str(view_id):
		secert_m = secert.query.filter_by(id=view_id).first()
		secert_t = u"<p>{secert.secert}<p>".format(secert = secert_m)
	else:
		secert_t = u"<p>***************************************<p>"

	name = u"<h1>name:{user_m.username}<h1>"
	email = u"<h2>email:{user_m.email}<h2>"

	info = (name+email+secert_t).format(user_m=user_m)
	return render_template('secert/views.html',info = info)


@bp_secert.route('/edit',methods = ['GET','POST'])
@login_check
def edit_secert():
	if request.method=='POST':
		secert_new = request.form.get('secert')
		error = None

		if not secert_new:
			error = u'请输入你的秘密'

		if error is None:
			secert.query.filter_by(id = session.get('user_id')).update({'secert':secert_new})
			db.session.commit()
			return redirect(url_for('secert.views_info'))
		flash(error)

	return render_template('secert/edit.html')


