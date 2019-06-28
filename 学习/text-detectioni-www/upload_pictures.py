# coding:utf-8

from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify
from werkzeug.utils import secure_filename
import os
import cv2
import time

from datetime import timedelta

# 设置允许的文件格式
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


app = Flask(__name__)
# 设置静态文件缓存过期时间
app.send_file_max_age_default = timedelta(seconds=1)


# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return render_template('home.layui_html')


# @app.route('/upload', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])  # 添加路由
def upload():
    if request.method == 'POST':
        f = request.files['file']

        if not (f and allowed_file(f.filename)):
            return jsonify({"error": 1001, "msg": "请检查上传的图片类型，仅限于png、PNG、jpg、JPG、bmp"})

        user_input = request.form.get("name")

        basepath = os.path.dirname(__file__)  # 当前文件所在路径

        upload_path = os.path.join(basepath, 'static/images', secure_filename(f.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        upload_path = os.path.join(basepath, 'static/images','test.jpg')  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)

        # 使用Opencv转换一下图片格式和名称
        img = cv2.imread(upload_path)
        print('upload_path :', upload_path,
              '\nbasepath :', basepath)
        cv2.imwrite(os.path.join(basepath, 'static/images', '/test.jpg'), img)

        # 这里，将上传至文件夹images的1.jpeg进行定位、分割、识别

        # 然后，将识别结果返回至*.html界面
        return render_template('upload.layui_html', userinput=user_input, val1=time.time())

    return render_template('upload.layui_html')


@app.route('/detection', methods=['POST', 'GET'])  # 添加路由
def detection():
    if request.method == 'POST':
        # 这里，将上传至文件夹images的test.jpg进行定位、分割、识别
        # upload_path = '../../GUI/www/static/images//test.jpg'
        # east = 'frozen_east_text_detection.pb'
        # text_detection.detection(upload_path)

        # 然后，将识别结果返回至***.html界面
        return render_template('upload.layui_html', val1=time.time())
    return render_template('upload.layui_html')


if __name__ == '__main__':
    # app.debug = True
    app.run(host='127.0.0.1', port=8987, debug=True)