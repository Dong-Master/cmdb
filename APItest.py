#coding:utf-8
#@mail:879995812@qq.com
import json
from urllib import parse
from urllib import request

url = "http://127.0.0.1:8000/api/CMDBApi/"
user_pasw = {
        "username": "root",
        "password": "123456"
    }
json_data = json.dumps(user_pasw)
data = {
    "type": "login",
    "data": user_pasw,
    "token": ''
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
}
sendData = parse.urlencode(data).encode()

req = request.Request(url = url,headers = headers,data = sendData)

response = request.urlopen(req)

result = response.read().decode()

print(result)