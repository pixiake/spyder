#encoding: utf-8
import re

#1.验证手机号码
# text = "18995620505"
# ret = re.match('1[34578]\d{9}',text)
# print(ret.group())
#2.验证邮箱
# text = "guotongxue123__@163.com"
# ret = re.match('\w+@[a-z0-9]+\.[a-z]+',text)
# print(ret.group())
#3.验证url
# text = "http://www.weather.com.cn/textFC/hb.shtml"
# ret = re.match('(http|https|ftp)://[^\s]+',text)
# print(ret.group())
#3.验证身份证
text = "14118119990606016X"
ret = re.match('\d{17}[\dxX]',text)
print(ret.group())