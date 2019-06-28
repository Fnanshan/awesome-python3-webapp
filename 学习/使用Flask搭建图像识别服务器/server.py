#coding:utf-8
from flask import request, Flask
import os
app = Flask(__name__)


@app.route("/", methods=['POST'])
def get_frame():
    upload_file = request.files['file']
    old_file_name = upload_file.filename
    file_path = os.path.join('/local/share/DeepLearning', 'new' + old_file_name)

    if upload_file:
        upload_file.save(file_path)
        print('success')
        return 'success'
    else:
        return 'failed'


if __name__ == "__main__":
    app.run("127.0.0.1", port=5000)