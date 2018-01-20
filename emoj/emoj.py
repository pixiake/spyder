#encoding: utf-8

import requests
import threading
from queue import Queue
from lxml import etree
from urllib import  request
import os
import re

class Productor(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.3.2000'
    }

    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Productor,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue
    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.pares_page(url)

    def pares_page(self , url):
        response = requests.get(url , headers=self.headers)
        html = etree.HTML(response.text)
        imgs = html.xpath("//div[@class='random_article']//img[@class!='gif']")
        for img in imgs:
            img_url = img.get('data-original')
            alt = img.get('alt')
            alt = re.sub(r'[\?？\.，。！!<>\*\\r\\n]' , '' , alt)
            suffix = os.path.splitext(img_url)[1]
            filename = alt + suffix
            self.img_queue.put((img_url,filename))
            #request.urlretrieve(img_url,'../images/'+filename)

class Consumer(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Consumer,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue
    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url , filename = self.img_queue.get()
            request.urlretrieve(img_url,'../images/'+filename)
            print(filename+'  下载完成！')

def main():
    page_queue = Queue(100)
    img_queue = Queue(1000)

    for x in range(90 , 101):
        url = 'http://www.doutula.com/article/list/?page=%d' %x
        page_queue.put(url)

    for x in range(5):
        t = Productor(page_queue , img_queue)
        t.start()
    for x in range(5):
        t = Consumer(page_queue , img_queue)
        t.start()


if __name__ == '__main__':
    main()