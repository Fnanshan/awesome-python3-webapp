# coding=utf-8

import requests

url = 'http://0.0.0.0:5000/'
r = requests.get(url)
print(r.status_code)
print(r.text)

url = 'http://0.0.0.0:5000/python'
r = requests.get(url)
print(r.status_code)
print(r.text)