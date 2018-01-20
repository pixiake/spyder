#enconding: utf-8

from urllib import request
from urllib import parse
# url1 = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
url1 = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0'

data = {
    'first':'true',
    'pn' : 1,
    'kd' : 'python'
}

headers= {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.3.2000',
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
}

rep = request.Request(url1 , headers=headers , data=parse.urlencode(data).encode('utf-8') , method='POST')
resp = request.urlopen(rep)
print(resp.read().decode('utf-8'))





