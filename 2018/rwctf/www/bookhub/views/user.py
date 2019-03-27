import flask
import redis
from flask_login import login_required, login_user, current_user, logout_user
from bookhub import app, db, rds
from bookhub.forms import LoginForm, UserForm
from bookhub.models import User, Book
from bookhub.helper import get_remote_addr


user_blueprint = flask.Blueprint('user', __name__, template_folder='templates')


@user_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(data=flask.request.data)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user, remember=form.remember_me.data)

        return flask.redirect(flask.url_for('book.admin'))

    return flask.render_template('login.html', form=form)


@user_blueprint.route('/admin/logout/')
@login_required
def logout():
    logout_user()
    return flask.redirect(flask.url_for('user.login'))


@user_blueprint.route('/admin/test', methods=['GET'])
def admin_res():
    status = 'success'
    sessionid = flask.session.sid
    prefix = app.config['SESSION_KEY_PREFIX']
    error = ''
    msg = ''
    print(sessionid)
    try:
        test = rf'''
        local function has_value (tab, val)
            for index, value in ipairs(tab) do
                if value == val then
                    return true
                end
            end
        
            return false
        end
        


        
        local inputs = {{ "{prefix}{sessionid}" }}
        local sessions = redis.call("keys", "{prefix}*")
        
        for index, sid in ipairs(sessions) do
            if not has_value(inputs, sid) then
                redis.call("del", sid)
            end
        end
        '''
        print(test)
        msg = test
        rds.eval(test, 0)
    except redis.exceptions.ResponseError as e:
        print(e)
        error = e
        app.logger.exception(e)
        status = 'fail'

    return flask.jsonify(dict(status=status, error=str(error), msg=str(msg)))
    # return {"status": status, "error": error, "msg": msg}

if app.debug:
    """
    For CTF administrator, only running in debug mode
    """

    @user_blueprint.route('/admin/system/')
    @login_required
    def system():
        ip_address = get_remote_addr()
        user_count = User.query.count()
        book_count = Book.query.count()

        return flask.render_template('system.html',
                                     ip_address=ip_address,
                                     user_count=user_count,
                                     book_count=book_count
                                     )

    @user_blueprint.route('/admin/test1/')
    @login_required
    def test1():
        print('test1')
        return 'test1'

    @login_required
    @user_blueprint.route('/admin/test2/')
    def test2():
        print('test2')
        return 'test2'

    @user_blueprint.route('/admin/system/change_name/', methods=['POST'])
    @login_required
    def change_name():
        user = User.query.get(current_user.id)
        form = UserForm(obj=user)
        if form.validate_on_submit():
            form.populate_obj(user)
            db.session.commit()
            return flask.jsonify(dict(status='success'))
        else:
            return flask.jsonify(dict(status='fail', errors=form.errors))

    @login_required
    @user_blueprint.route('/admin/system/refresh_session/', methods=['POST'])
    def refresh_session():
        """
        delete all session except the logined user

        :return: json
        """

        status = 'success'
        sessionid = flask.session.sid
        prefix = app.config['SESSION_KEY_PREFIX']

        print(sessionid)

        if flask.request.form.get('submit', None) == '1':
            try:
                rds.eval(rf'''
                local function has_value (tab, val)
                    for index, value in ipairs(tab) do
                        if value == val then
                            return true
                        end
                    end
                    return false
                end

                local inputs = {{ "{prefix}{sessionid}" }}
                local sessions = redis.call("keys", "{prefix}*")
                
                for index, sid in ipairs(sessions) do
                    if not has_value(inputs, sid) then
                        redis.call("del", sid)
                    end
                end
                ''', 0)
            except redis.exceptions.ResponseError as e:
                print(e)
                app.logger.exception(e)
                status = 'fail'

        return flask.jsonify(dict(status=status))
