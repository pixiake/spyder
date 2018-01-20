#encoding: utf-8

import requests
from bs4 import BeautifulSoup
from pyecharts import Bar


ALL_Data = []
def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.3.2000'
    }
    response = requests.get(url , headers=headers)
    text = response.content.decode('utf-8')
    #soup = BeautifulSoup(text , 'lxml')
    soup = BeautifulSoup(text , 'html5lib')
    conMidtab = soup.find('div' , class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index , tr in enumerate(trs):
            tds = tr.find_all('td')
            if index == 0:
                city_td = tds[1]
            else:
                city_td = tds[0]
            city = list(city_td.stripped_strings)[0]
            #print(city)
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            ALL_Data.append({"city" : city , "min_temp" : int(min_temp)})


def main():
    hb = "http://www.weather.com.cn/textFC/hb.shtml"
    db = "http://www.weather.com.cn/textFC/db.shtml"
    hd = "http://www.weather.com.cn/textFC/hd.shtml"
    hz = "http://www.weather.com.cn/textFC/hz.shtml"
    hn = "http://www.weather.com.cn/textFC/hn.shtml"
    xb = "http://www.weather.com.cn/textFC/xb.shtml"
    xn = "http://www.weather.com.cn/textFC/xn.shtml"
    gat = "http://www.weather.com.cn/textFC/gat.shtml"
    urls = [hb , db , hd , hz , hn , xb , xn , gat]
    for url in urls:
        parse_page(url)

    # def sort_key(data):
    #     min_temp = data['min_temp']
    #     return min_temp
    # ALL_Data.sort(key=sort_key)

    ALL_Data.sort(key=lambda data:data['min_temp'])
    print(ALL_Data)
    data = ALL_Data[0:10]
    cities = list(map(lambda data:data['city'] , ALL_Data))
    temps = list(map(lambda  data:data['min_temp'] , ALL_Data))
    bar = Bar(" 中国天气最低气温排行榜")
    bar.add('',cities , temps)
    bar.render('temperature.html')


if __name__ == '__main__':
    main()