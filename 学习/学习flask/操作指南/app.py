# coding=utf-8

from flask import Flask, Blueprint, render_template, abort, url_for, redirect, request, make_response, Session, session
from flask_script import Manager
from jinja2 import TemplateNotFound


# 初始化
# Flask类构造函数唯一需要的参数就是应用程序的主模块或包。
# Flask使用 __name__ 来确定应用程序的根目录，这样以后可以相对这个路径来找到资源文件。
app = Flask(__name__)

# 使用命令行参数启动
# manager = Manager(app=app)

# 实例化（对象化）blueprint
#   * 第一个是蓝图的名称，第二个是蓝图所在的包或模块，_ name _代表当前模块名或者包名
blue = Blueprint('first', __name__)


@blue.route('/redirect/')
def make_redirect():
    # 第一种方法
    # return redirect('/user/')
    # 第二种方法，若使用blueprint进行url_for，则用blueprint的名字引用函数，例如：first.hello
    return redirect(url_for('first.hello'))


@blue.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        username = session.get('username')
        return render_template('login.html', username=username)
    else:
        username = request.form.get('username')
        session['username'] = username

        return redirect(url_for('first.login'))


# 注册blueprint（放在路由后面）
# * 第一个参数即我们定义初始化定义的蓝图对象，
# * 第二个参数url_prefix表示该蓝图下，所有的url请求必须以/user开始。
# * 这样对一个模块的url可以很好的进行统一管理
app.register_blueprint(blue)


if __name__ == '__main__':
    # app.run(host='0.0.0.0',port=8080,debug=True)
    app.run(debug=True)
    # 使用命令行参数启动，则命令行输入：python app.py runserver -h 127.0.0.1 -p 5000 -d -r
    #   * -h表示地址。-p表示端口。-d表示debug模式。-r表示自动重启
    # manager.run()
