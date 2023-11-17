from functools import wraps
from flask import g, session, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session['name'] is None:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


