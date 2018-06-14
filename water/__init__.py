from flask import Flask, session
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'zyxwvutsrqponmlkj'

app.debug = True


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.11/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("username") is None:
            return redirect(url_for("login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# root
import water.views
if __name__ == '__main__':
    app.run(debug=True)