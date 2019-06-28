import requests

url = 'http://127.0.0.1:5000'

filepath='./t2.jpg'
split_path = filepath.split('/')
filename = split_path[-1]
print(filename)

file = open(filepath, 'rb')
files = {'file': (filename, file, 'image/jpg')}

r = requests.post(url, files=files)
result = r.text
print(result)