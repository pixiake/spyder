#enconding: utf-8

from urllib import request

# resp = request.urlopen('http://httpbin.org/ip')
# print(resp.read().decode('utf-8'))
# 快代理 ： http//www.kuaidaili.com
# 代理云 ： http://www.dailiyun.com

handler = request.ProxyHandler({'http' : '163.125.249.55:8118'})

opener = request.build_opener(handler)
req = request.Request("http://httpbin.org/ip")
resp = opener.open((req))
print(resp.read())

