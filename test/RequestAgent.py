#encoding: utf-8
import requests
url = "http://httpbin.org/ip"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.3.2000'
}

proxy = {
    'http': '163.125.249.55:8118'
}

resp = requests.get(url , headers = headers , proxies = proxy)
print(resp.text)
with open('xx.html' , 'w' , encoding='utf-8') as fp:
    fp.write(resp.text)