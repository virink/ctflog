
def op(v):
    print('-' * 30)
    print(v)
    print('-' * 30)


from dotenv import load_dotenv
load_dotenv(verbose=True)

from bookhub import app, db
import bookhub.commands
import bookhub.models
from bookhub.views import *


app.register_blueprint(user_blueprint)
app.register_blueprint(book_blueprint)
