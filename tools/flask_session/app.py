from flask import Flask, session
app = Flask(__name__)

app.secret_key = "secret_keysecret_keysecret_key"


@app.route('/')
def hello_world():
    a = session['user'] if 'user' in session else 'World'
    return 'Hello %s!' % a


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    session['user'] = username
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id and 1


if __name__ == '__main__':
    app.run(debug=True)
