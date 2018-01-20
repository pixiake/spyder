#encoding: utf-8

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.3.2000'
}

#cookies:
response = requests.get('http://www.baidu.com')
print(response.cookies)
print(response.cookies.get_dict())

#session:
data = {
    'email': 'guotongxue123@163.com',
    'password': '135262ab'
}
login_url = "http://www.renren.com/PLogin.do"
session = requests.session()

session.post(login_url , data=data , headers=headers)

url = "http://www.renren.com/289199450/profile"
response = session.get(url)

with open('renren1.html' , 'w' , encoding='utf-8') as fp:
    fp.write(response.text)

#处理不信任的SSL证书：
# resp = requests.get('http://www.12306.cn/mormhweb', verify = False)





