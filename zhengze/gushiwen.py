#encoding: utf-8

import requests
import re

def pares_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.3.2000'
    }
    response = requests.get(url , headers)
    text = response.text
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>' , text , re.DOTALL)
    dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>' , text)
    authors = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>' , text  , re.DOTALL)
    content_tags = re.findall(r'<div class="contson" .*?>(.*?)</div>' , text , re.DOTALL)
    contents = []
    poems = []


    for content in content_tags:
        x = re.sub(r'<.*?>' , "" ,content)
        contents.append(x.strip())

    for value in zip(titles , dynasties , authors ,contents):
        title , dynastie , author , content = value
        poem = {
            'title' : title ,
            'dynastie' : dynastie ,
            'author' : author ,
            'content' : content
        }
        poems.append(poem)
    for poem in poems:
        print(poem)
        print('='*30)
def main():
    #url = "http://www.gushiwen.org/default_1.aspx"
    for i in range(1 , 10):
        url = "http://www.gushiwen.org/default_%s.aspx" %i
        pares_page(url)


if __name__ == '__main__':
    main()