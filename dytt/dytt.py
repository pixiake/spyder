#encoding: utf-8

from lxml import etree
import requests

BASE_DOMAIN  = "http://www.ygdy8.net"
# url = "http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.3.2000',
}

def get_detail_urls(url):

    response = requests.get(url, headers=headers)
    text = response.content.decode('gbk', 'ignore')
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url:BASE_DOMAIN+url,detail_urls)
    return detail_urls
    # for detail_url in detail_urls:
    #     print(BASE_DOMAIN + detail_url)

def spider():
    base_url = "http://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html"
    n = 1
    for x in range(1 , 8):
        url = base_url.format(x)
        #print(url)
        detail_urls = get_detail_urls(url)
        print("page %d" %n)
        n = n + 1
        for detail_url in detail_urls:
            parase_detail_page(detail_url)

def parase_info(info , rule):
    return info.replace(rule , "").strip()

def parase_detail_page(url):
    movie = {}
    response = requests.get(url , headers = headers)
    text = response.content.decode('gbk' , 'ignore')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    # print(etree.tostring(title , encoding='utf-8').decode('utf-8'))

    movie['title'] = title

    zoomE = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoomE.xpath(".//img/@src")
    cover = imgs[0]
    movie['cover'] = cover
    # screenshot = imgs[1]
    # movie['screenshot'] = screenshot
    infos = zoomE.xpath(".//text()")
    for index,info in enumerate(infos):
        # print(info)
        # print(index)
        if info.startswith("◎年　　代"):
            info = parase_info(info , "◎年　　代")
            movie['year'] = info
        elif info.startswith("◎产　　地"):
            info = parase_info(info , "◎产　　地")
            movie['country'] = info
        elif info.startswith("◎类　　别"):
            info = parase_info(info , "◎类　　别")
            movie['category'] = info
        elif info.startswith("◎豆瓣评分"):
            info = parase_info(info , "◎豆瓣评分")
            movie['douban_rating'] = info
        elif info.startswith("◎片　　长"):
            info = parase_info(info, "◎片　　长")
            movie['duration'] = info
        elif info.startswith("◎导　　演"):
            info = parase_info(info, "◎导　　演")
            movie['dircetor'] = info
        elif info.startswith("◎主　　演"):
            info0 = parase_info(info, "◎主　　演")
            actors = []
            actors.append(info0)
            for s in range(index+1, 100):
                try:
                    if infos[s].startswith("　　　　　　"):
                        actor = parase_info(infos[s], "　　　　　　")
                        actors.append(actor)
                except BaseException:
                    break
            movie['actor'] = actors
    print(movie)
if __name__ == '__main__':
    spider()