#encoding: utf-8

import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.3.2000'
}
kw = {'wd': '中国'}
response = requests.get("http://www.baidu.com/s" , params=kw , headers = headers)
#
# print(response.text)
# print(response.content)
# print(response.url)
# print(response.encoding)
# print(response.status_code)
# response = requests.get("http://www.baidu.com/s" )
print(response.content.decode('utf-8'))

with open('baidu.html' , 'w' , encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))