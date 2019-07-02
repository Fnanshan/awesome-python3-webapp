# coding=utf-8
from functools import wraps

from flask import session, url_for, redirect


def is_login(func):
    @wraps(func)
    def check_login(*args, **kwargs):
        if 'user_id' in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('first.new_login'))
    return check_login