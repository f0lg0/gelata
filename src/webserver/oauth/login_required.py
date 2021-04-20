from flask import session, render_template
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = dict(session).get('profile', None)
        # TODO: exec authorized code
        if user:
            return f(*args, **kwargs)
        return render_template("login.html")
    return decorated_function
