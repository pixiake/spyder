#encoding: utf-8

from urllib import request
from http.cookiejar import MozillaCookieJar

cookiejar = MozillaCookieJar("cookie.txt")
cookiejar.load(ignore_discard=True)
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.3.2000'
}
# req = request.Request('http://httpbin.org/cookies/set?course=abc',headers=headers)
req = request.Request('http://httpbin.org/cookies',headers=headers)
resp = opener.open(req)

for cookie in cookiejar:
    print(cookie)
# print(resp.read())
# cookiejar.save(ignore_discard=True,ignore_expires=True)

