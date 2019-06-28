# coding=utf-8

from flask import Flask, url_for, request, render_template, abort, make_response
from flask import session, redirect, escape
# from werkzeug import secure_filename 报错
from werkzeug.utils import redirect
from werkzeug.utils import secure_filename

import functions as func
app = Flask(__name__)


# 给静态文件生成 URL ，使用特殊的 'static' 端点名:
# url_for('static', filename='style.css')
# 这个 style.css 应该存储在文件系统上的 static/style.css 。


@app.route('/')
def index():
    # 读取 cookies
    # username = request.cookies.get('username')
    # 存储 cookies
    # ......
    try:
        # 读取 cookies
        username = request.cookies.get('username')
    except TypeError as e:
        print(e)
    finally:
        return render_template('home.html')
        # redirect重定向到 **function
        # return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if func.valid_login(request.form['username'],
                            request.form['password']):
            return func.log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
    # abort(401)      # 401 意味着禁止访问


# 路由中可加入变量<variable_name>
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


# 路由中可加入<converter:variable_name>, 指定一个可选的转换器，转换器有：int/float/path
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


# 唯一URL / 重定向行为
# URL 尾端有 / ，若访问/projects 会被 Flask 重定向到 /projects/。
@app.route('/projects/')
def projects():
    abort(404)      # 只要是404错误，即使没有直接调用page_not_found()，我都会跳转到page_not_found()
    return 'The project page'


# URL 尾端没有 / ，若访问/projects 会会产生一个 404 “Not Found” 错误。
@app.route('/about')
def about():
    return 'The about page'


# 文件上传
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
        return 'post , upload ok'
    return 'get ok'


@app.errorhandler(404)
def page_not_found(error):
    # 操作响应对象 make_response()
    resp = make_response(render_template('404.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

    # 不操作相应对象，直接返回一个合法的响应对象
    # return render_template('404.html'), 404


@app.route('/opt_session')
def opt_session():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'


@app.route('/opt_login', methods=['GET', 'POST'])
def opt_login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('opt_login'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('opt_session'))


# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


# 用 url_for() 来给指定的函数名构造 URL（根据函数名找URL）
# 构建URL的理由？
#   * 重定向？
# with app.test_request_context():
#     pass
    # print(url_for('index'))
    # print(url_for('login'))
    # print(url_for('login', next='/'))
    # print(url_for('show_user_profile', username='John Doe'))


if __name__ == '__main__':
    # 正常模式
    # app.run()
    # 监听所有公网 IP
    # app.run(host='0.0.0.0')
    # debug model
    app.run(debug=True)
