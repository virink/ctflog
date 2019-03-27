import re
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash
from app import app, mysql, db_session
from app.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm
from app.models import load_user, load_user_by_username
from others import now, avatar
from itertools import izip


@app.before_request
def before_request():
    if current_user.is_authenticated:
        mysql.Mod('user', {"id": current_user.id},
                  {"last_seen": "'%s'" % now()})


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        res = mysql.Add("post", ['NULL', "'%s'" % form.post.data,
                                 "'%s'" % current_user.id, "'%s'" % now()])
        if res == 1:
            flash('Your post is now live!')
            return redirect(url_for('index'))
    page = request.args.get('page', 1, type=int)
    all_posts = current_user.followed_posts()
    post_per_page = app.config['POSTS_PER_PAGE']
    posts = all_posts[(page - 1) * post_per_page:page * post_per_page if len(
        all_posts) >= page * post_per_page else len(all_posts)]
    next_url = url_for('explore', page=page + 1) \
        if len(all_posts) > page * post_per_page else None
    prev_url = url_for('explore', page=page - 1) \
        if (page > 1 and len(all_posts) > page * post_per_page) else None
    usernames = []
    for i in posts:
        usernames.append(load_user(i[2]))
    return render_template('index.html', title='Home', form=form,
                           posts=posts, next_url=next_url,
                           prev_url=prev_url, usernames=usernames, izip=izip, avatars=avatar, dt=datetime.strptime)


@app.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    page = page if page > 0 else 1
    all_posts = mysql.All("post", order=["id desc"])
    post_per_page = app.config['POSTS_PER_PAGE']
    posts = all_posts[
        (page - 1) * post_per_page:page * post_per_page if len(all_posts) >= page * post_per_page else len(
            all_posts)]
    next_url = url_for('explore', page=page + 1) \
        if len(all_posts) > page * post_per_page else None
    prev_url = url_for('explore', page=page - 1) \
        if (page > 1 and len(all_posts) > (page - 1) * post_per_page) else None
    usernames = []
    for i in posts:
        usernames.append(load_user(i[2]))
    return render_template('index.html', title='Home',
                           posts=posts, usernames=usernames, next_url=next_url,
                           prev_url=prev_url, izip=izip, avatars=avatar, dt=datetime.strptime)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = load_user_by_username(form.username.data)
        if user == -1:
            flash('Something error!')
            return render_template('500.html'), 500
        if user == 0:
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        res = mysql.Add("user", ["NULL", "'%s'" % form.username.data, "'%s'" % form.email.data,
                                 "'%s'" % generate_password_hash(form.password.data), "''", "'%s'" % now()])
        if res == 1:
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    if re.match("^[a-zA-Z0-9_]+$", username) == None:
        return render_template('500.html'), 500
    user = load_user_by_username(username)
    if user == -1:
        flash('Something error!')
        return render_template('500.html'), 500
    if user == 0:
        flash('User is not exists')
        return redirect(url_for('index'))

    page = request.args.get('page', 1, type=int)

    page = page if page > 0 else 1
    all_posts = current_user.followed_posts()
    post_per_page = app.config['POSTS_PER_PAGE']
    posts = all_posts[
        (page - 1) * post_per_page:page * post_per_page if len(all_posts) >= page * post_per_page else len(
            all_posts)]

    next_url = url_for('user', username=user.username, page=page + 1) \
        if len(all_posts) > page * post_per_page else None
    prev_url = url_for('user', username=user.username, page=page - 1) \
        if (page > 1 and len(all_posts) > (page - 1) * post_per_page) else None
    usernames = []
    for i in posts:
        usernames.append(load_user(i[2]))
    return render_template('user.html', user=user, posts=posts, usernames=usernames,
                           next_url=next_url, prev_url=prev_url, izip=izip, avatars=avatar, dt=datetime.strptime)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.note = form.note.data
        res = mysql.Mod("user", {"id": current_user.id}, {
                        "username": "'%s'" % current_user.username, "note": "'%s'" % current_user.note})
        if res != 0:
            flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.note.data = current_user.note
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)


@app.route('/follow/<username>')
@login_required
def follow(username):
    if re.match("^[a-zA-Z0-9_]+$", username) == None:
        return render_template('500.html'), 500
    user = load_user_by_username(username)
    if user == -1:
        flash('Something error!')
        return render_template('500.html'), 500
    if user == 0:
        flash('User is not exists')
        return redirect(url_for('index'))

    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('user', username=username))
    if current_user.follow(user):
        flash('You are following {}!'.format(username))
    else:
        flash('Failed!')
    return redirect(url_for('user', username=username))


@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    if re.match("^[a-zA-Z0-9_]+$", username) == None:
        return render_template('500.html'), 500
    user = load_user_by_username(username)
    if user == -1:
        flash('Something error!')
        return render_template('500.html'), 500
    if user == 0:
        flash('User is not exists')
        return redirect(url_for('index'))

    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('user', username=username))
    if current_user.unfollow(user):
        flash('You are not following {}.'.format(username))
    else:
        flash('Failed!')
    return redirect(url_for('user', username=username))
