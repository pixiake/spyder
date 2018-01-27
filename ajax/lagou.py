#encoding: utf-8
import requests
from lxml import etree
import  time
import re
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.5.2000',
        "Referer": 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'Cookie' : 'UM_distinctid=160b090b01c4b4-070c3d2a138328-7e243017-100200-160b090b01d184; user_trace_token=20180101151247-2b699445-eec3-11e7-b95c-525400f775ce; LGUID=20180101151247-2b6997cc-eec3-11e7-b95c-525400f775ce; JSESSIONID=ABAAABAAAIAACBIDCF6AF2F65CC94F86B0E179ED4DAABB0; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=bzclk.baidu.com; PRE_SITE=http%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D06KL00c00f7Ghk60yUKm0FNkUsK13AVp00000PW4pNb00000IvQWVH.THL0oUhY0A3qUg-GuHFbusK15H-9m1nkrHIWnj0sPj9Wrj60IHYzfHF7f1bsPDmknWw7rHNjPYndfWN7PDRLnWwAPH-7ffK95gTqFhdWpyfqn101n1csPHnsPausThqbpyfqnHm0uHdCIZwsT1CEQLILIz4_myIEIi4WUvYE5LNYUNq1ULNzmvRqUNqWu-qWTZwxmh7GuZNxTAn0mLFW5HfznWcs%26tpl%3Dtpl_10085_15730_11224%26l%3D1500117464%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%252580%252591%2525E5%2525AE%252598%2525E7%2525BD%252591-%2525E4%2525B8%252593%2525E6%2525B3%2525A8%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E8%252581%25258C%2525E4%2525B8%25259A%2525E6%25259C%2525BA%2526xp%253Did%28%252522m6c247d9c%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D220%26ie%3Dutf-8%26f%3D8%26ch%3D1%26tn%3Dmyie2dg%26wd%3Dlagou%26oq%3Dlagou%26rqlang%3Dcn%26ssl_s%3D0%26ssl_c%3Dssl2_1613564c1ee; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F%3Futm_source%3Dm_cf_cpt_baidu_pc; X_HTTP_TOKEN=132190578fec76cc2dbc91f49b6ecd86; _putrc=7F18ABBE08D2C383; login=true; unick=%E9%83%AD%E5%B3%B0; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=7; gate_login_token=89d3e0d9f115282363b2cf723390dee889d3f0f0971b3c5d; _gat=1; TG-TRACK-CODE=index_search; _gid=GA1.2.1905583148.1517019255; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1514790765,1514815788,1514815798,1517019255; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1517020685; _ga=GA1.2.946300296.1514790765; LGSID=20180127101415-c5a07c0a-0307-11e8-abaa-5254005c3644; LGRID=20180127103805-1a08b6bf-030b-11e8-9d21-525400f775ce; CNZZDATA1256793290=270434173-1514790704-https%253A%252F%252Fwww.baidu.com%252F%7C1517015746; SEARCH_ID=29a268f25b5542c4a53c0da9a3ab5474; index_location_city=%E5%8C%97%E4%BA%AC'
    }

def request_list_page():
    #url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0"
    url = "https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0"

    data = {
        'first' : "true",
        'pn' : 1,
        'kd' : 'python'
    }
    for x in range(1 , 14):
        data["pn"] = x
        response = requests.post(url , headers=headers ,data=data)
        #print(response.json())
        time.sleep(3)
        result = response.json()
        positions = result['content']['positionResult']['result']
        # print(positions)
        for position in positions:
            positionID = position['positionId']
            # print(positionID)
            position_url = 'https://www.lagou.com/jobs/%s.html' % positionID
            # print(position_url)
            parase_position_details(position_url)
            break
        break
def parase_position_details(url):
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    position_name = html.xpath("//span[@class='name']/text()")[0]
    job_request = html.xpath("//dd[@class='job_request']//span")
    salary = job_request[0].xpath(".//text()")[0].strip()
    # salary = salary_span.xpath[".//span[@class='salary']"]
    city = job_request[1].xpath('.//text()')[0].strip()
    city = re.sub(r"[\s/]" , "" , city)
    work_years = job_request[2].xpath('.//text()')[0].strip()
    work_years = re.sub(r"[\s/]", "", work_years)
    education = job_request[3].xpath('.//text()')[0].strip()
    education = re.sub(r"[\s/]", "", education)
    describe = "".join(html.xpath(".//dd[@class='job_bt']//text()")).strip()
    # describe = re.sub(r"[\s/]", "", describe)
    print(describe)
def main():
    request_list_page()

if __name__ == '__main__':
    main()