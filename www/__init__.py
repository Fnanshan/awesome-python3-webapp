from flask_bootstrap import Bootstrap
from flask import Flask, request, render_template, url_for, session, escape, redirect, jsonify
import bbs_system_functions as system
import sqlalchemy_connDB as connDB2
from opt_functions import is_login
from sqlalchemy_connDB import query_one

app = Flask(__name__)
bootstrap = Bootstrap(app)
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/', methods=['GET', 'POST'])
def home():
    ''' 要把模板home.html放到正确的templates目录下，templates和app.py在同级目录下 '''
    if 'username' in session:
        # 根据session中的用户名查找其所有信息
        user = system.User()
        user.username = session['username']
        user.id = session['id']
        # id = user.query_all_by_username()[0][0]
        result = user.query_all_by_username()
        if result[0][0] in range(5):     # session.username是管理员
            return render_template('home.html', username=escape(session['username']), user_info=' you is admin')
        return render_template('home.html', username=escape(session['username']))
    return render_template('home.html')


@app.route('/login/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        userpass = request.form['password']
        # 1. 判断有没有用户
        flag = system.login(username, userpass)
        if flag == 0:
            return render_template('login.html', message='username not find', info='')
        elif flag == 1:
            return render_template('login.html', message='userpass error', info='')
        else:   # flag == 2
            # 根据username查找id
            user = system.User()
            user.username = username
            result = user.query_all_by_username()
            # 登录成功则存入会话
            session['id'] = result[0][0]
            session['username'] = request.form['username']
            # return render_template('home.html', message='login success', username=username, info='')
            return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        userpass = request.form['userpass']
        flag = system.register(username, userpass)
        if flag:
            session['register_flag'] = 'True'
            # return render_template('login.html', message='register success!')
            return redirect(url_for('signin'))
        else:
            return render_template('register.html', message='register error!')

    return render_template('register.html')


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.clear()
    return redirect(url_for('home'))


@app.route('/insert_user/', methods=['GET', 'POST'])
def insert_user():
    '''admin操作
    * session判断username是否是admin
    '''
    # 检查session
    if 'username' in session:
        if request.method == 'POST':
            user = system.User()
            user.id = request.form['id']
            user.username = request.form['username']
            user.userpass = request.form['userpass']
            user.usertype = request.form['usertype']
            user.usermail = request.form['usermail']
            user.userhomepage = request.form['userhomepage']
            user.homepagename = request.form['homepagename']
            user.sex = request.form['sex']
            user.comefrom = request.form['comefrom']
            user.usersign = request.form['usersign']
            user.redate = request.form['redate']
            user.insert()
            return redirect(url_for('user_list'))
        # 根据session中的用户名查找其所有信息
        user = system.User()
        user.username = session['username']
        # id = user.query_all_by_username()[0][0]
        result = user.query_all_by_username()
        if result[0][0] in range(5):     # session.username是管理员
            return render_template('insert_user_detail.html', result=result)
        else:
            redirect(url_for('home'))
    return redirect(url_for('home'))


@app.route('/update_user/<user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    # *** js判断输入是否合法(没有做）
    # 检查session
    if 'username' in session:
        if request.method == 'POST':
            user = system.User()
            user.id = request.form['id']
            user.username = request.form['username']
            user.userpass = request.form['userpass']
            user.usertype = request.form['usertype']
            user.usermail = request.form['usermail']
            user.userhomepage = request.form['userhomepage']
            user.homepagename = request.form['homepagename']
            user.sex = request.form['sex']
            user.comefrom = request.form['comefrom']
            user.usersign = request.form['usersign']
            user.redate = request.form['redate']
            user.update()
            session.pop('username', None)
            session['username'] = request.form['username']
            # 判断session.username是不是admin，如果不是admin则返回login页面
            result = user.query_all_by_username()[0][0]
            if result not in range(5):
                return redirect(url_for('home'))
            # 判断session.username是不是admin，如果是admin则返回用户列表
            return redirect(url_for('user_list'))
        print('---/update_user/' + user_id + '---get opt :')
        user = system.User()
        if user_id:
            # 根据路由中的user_id查找其所有信息
            user.id = user_id
            result = user.query_all_by_id()
        else:
            # 根据session中的用户名查找其所有信息
            user.username = session['username']
            result = user.query_all_by_username()
        print('update_user info :', result)
        # id = user.query_all_by_username()[0][0]
        return render_template('user_detail.html', result=result)
    return redirect(url_for('home'))


@app.route('/user_list/', methods=['GET', 'POST'])
def user_list():
    if 'id' in session:               # 此处不应该以是否有session为标准，而是判断session中的信息正确与否。
        user = system.User()
        user.id = session['id']
        verify_session = user.query_all_by_id()
        print('verify_session :', verify_session)
        if session['id'] == verify_session[0][0] and session['username'] == verify_session[0][1]:
            print('session中的信息与数据库信息相符')
        if request.method == 'GET':
            user = system.User()
            result = user.query_all_user()
            return render_template('user_list.html', result=result)
        else:
            var = request.form    # 把Ajax中的数据取出来
            # a = request.values  # 把Ajax中的数据取出来
            print(var)            # 输出一下，看是什么类型，ImmutableMultiDict这个类型
            result_id = None
            for i in var:
                # print(i)        # 先看能不能迭代，输出i 是一个str
                # print(type(i))  # 看类型果然是str
                i = eval(i)     # 百度str 怎么转成dic ,有两种方法，eval()和exec()函数实现
                # print(i)
                # print(type(i))
                result_id = i
            return redirect(url_for('user_list_edit', result_id=result_id))
    return redirect(url_for('home'))


@app.route('/user_list/edit/<string:result_id>', methods=['GET', 'POST'])
def user_list_edit(result_id):
    if request.method == 'POST':
        print('result_id :', result_id,
              '\ntype(result_id) :', type(result_id))
        # return render_template('user_detail.html', result=result)
        # return redirect(url_for('update_user', user_id=result_id))
        redirect(url_for('update_user', user_id=result_id))
        return result_id
    print('---/user_list/edit/' + str(result_id) + '---get opt')
    return redirect(url_for('update_user', user_id=result_id))


@app.route('/user_list/delete/<user_id>', methods=['GET', 'POST'])
def delete_user_delete(user_id):
    if request.method == 'POST':
        print('post ok', user_id)
        user = system.User()
        user.id = user_id
        status = user.delete()
        print('delete status :', status)
        return 'delete ok'
    return user_id


@app.route('/update_self/edit/<int:result_id>', methods=['GET', 'POST'])
def update_self_edit(result_id):
    if request.method == 'POST':
        redirect(url_for('update_user', user_id=result_id))
        return str(result_id)
    print('---/update_self/edit/' + str(result_id) + '---get opt')
    return redirect(url_for('update_user', user_id=result_id))


@app.route('/getjson', methods=['GET', 'POST'])
def getjson():
    # a = request.json
    # if a:
    #     data = a['mydata']
    #     print(a)
    #     return jsonify('success')
    # return jsonify('this is my data')
    if request.method == 'POST':
        json = request.form     # 这个json是ImmutableMultiDict，不可作为js的回调函数的数据；jsonify(json)是response回应值；json['key']是数据。
        # print(':', json['name'],
        #       '\n:', json['url'])
        # response = json['name'] + json['url']
        response = json
        print(response)
        return response
    return 'get'


@app.route('/query_board2', methods=['GET', 'POST'])
def query_board2():
    board = system.Board()
    if request.method == 'POST':
        return render_template('board2.html')
    # get操作，先获取数据库中的board
    # query_board_sql = 'select * from board;'
    result = board.query_board()
    return render_template('board2.html', result=result)


@app.route('/update_board_detail', methods=['GET', 'POST'])
def update_board_detail():
    if request.method == 'POST':
        board = system.Board()
        board.update_board()
        return render_template('board_detail.html')
    return render_template('board_detail.html')


@app.route('/one')
def hello_world():
    return render_template('test.html')


@app.route('/test/', methods=['GET', 'POST'], endpoint='test01')
def test():
    getData = request.args # 利用request对象获取GET请求数据
    print('获取的GET数据为：', getData) # 打印获取到的GET数据 ImmutableMultiDict([])
    postData = request.form # 利用request对象获取POST请求数据
    print('获取的POST数据为：', postData) # 打印获取到的POST请求 ImmutableMultiDict([('username', '456'), ('password', '789')])
    username = request.form.get('username')
    password = request.form.get('password')
    print(username,password) #456 789
    return '这是测试页面'


if __name__ == '__main__':
    # app.run()
    app.run(debug=True)     # debug=True 调试模式：服务器会在代码修改后自动重新载入，并在发生错误时提供一个相当有用的调试器
