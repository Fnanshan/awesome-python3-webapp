# coding=utf-8
import sqlalchemy_connDB
from flask import render_template

def do_the_login():
    return 'do_the_login'


def show_the_login_form():
    return 'show_the_login_form'


def valid_login(username, userpass):
    query_by_username_sql = 'select username, userpass from bbs_user where username= \'' + username + '\''
    sql_return = sqlalchemy_connDB.query(query_by_username_sql)
    # 1. 判断有没有用户
    if len(sql_return) > 0:
        # 2. 判断密码是否正确
        if username == sql_return[0][0] and userpass == sql_return[0][1]:
            return render_template('home.html', message='login success', username=username, info='')
        return render_template('home.html', message='userpass error', info='')
    # sql_return 是 0
    return render_template('home.html', message='username not find', info='')

def log_the_user_in():
    return 'log_the_user_in'