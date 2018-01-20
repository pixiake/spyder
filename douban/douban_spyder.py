#encoding: utf-8

import requests
from lxml import etree
#1 抓取页面
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.3.2000',
    'Referer': 'https://movie.douban.com/'
}
url = 'https://movie.douban.com/cinema/nowplaying/wuhan/'
respnse = requests.get(url , headers = headers)
#print(respnse.text)
text = respnse.text
#2 数据提取
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]
#print(etree.tostring(ul ,encoding='utf-8').decode("utf-8"))

lis = ul.xpath("./li")
for li in lis:
    #print(etree.tostring(li , encoding='utf-8').decode("utf-8"))
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    duration = li.xpath("@data-duration")[0]
    region = li.xpath("@data-region")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    thumbnail = li.xpath(".//img/@src")
    movies = []
    print(thumbnail)
    movie = {
        'title' : title,
        'score' : score,
        'duration' : duration,
        'region' : region,
        'director' : director,
        'actors' : actors,
        'thumbnail' : thumbnail,
    }
    movies.append(movie)

print(movies)