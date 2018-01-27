#encoding: utf-8

from selenium import webdriver
import time
from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select , WebDriverWait
from selenium.webdriver.support  import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import re
import csv


class LagouSpider(object):
    driver_path = r"D:\Code\chromedirver\chromedriver.exe"
    # driver = webdriver.Chrome(executable_path=driver_path)
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
        self.positions = []
        fp = open('lagou.csv' , 'a' , newline='' , encoding='utf-8')
        self.writer = csv.DictWriter(fp ,['name' , 'company' , 'salary' , 'city' , 'work_years' , 'education' , 'dese'])
        self.writer.writeheader()

    def run(self):
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            WebDriverWait(driver=self.driver , timeout=10).until(
                EC.presence_of_element_located((By.XPATH , "//div[@class='pager_container']/span[last()]"))
            )
            self.parase_list_source(source)

            next_page = self.driver.find_element_by_xpath("//div[@class='pager_container']/span[last()]")
            if "pager_next pager_next_disabled" in next_page.get_attribute("class"):
                break
            else:
                next_page.click()
                time.sleep(3)

    def parase_list_source(self , souce):
        html = etree.HTML(souce)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            self.request_detail_page(link)
            time.sleep(3)

    def request_detail_page(self,url):
        # self.driver.get(url)
        self.driver.execute_script("window.open('%s')" % url )
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver , timeout=10).until(
            EC.presence_of_element_located((By.XPATH , "//span[@class='name']"))
        )
        source = self.driver.page_source
        self.parase_detail_page(source)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def parase_detail_page(self,source):
        html = etree.HTML(source)
        position_name = html.xpath("//span[@class='name']/text()")[0]
        job_request = html.xpath("//dd[@class='job_request']//span")
        salary = job_request[0].xpath(".//text()")[0].strip()
        # salary = salary_span.xpath[".//span[@class='salary']"]
        city = job_request[1].xpath('.//text()')[0].strip()
        city = re.sub(r"[\s/]", "", city)
        work_years = job_request[2].xpath('.//text()')[0].strip()
        work_years = re.sub(r"[\s/]", "", work_years)
        education = job_request[3].xpath('.//text()')[0].strip()
        education = re.sub(r"[\s/]", "", education)
        describe = "".join(html.xpath(".//dd[@class='job_bt']//text()")).strip()
        # describe = re.sub(r"[\s/]", "", describe)
        company = html.xpath("//h2[@class='fl']/text()")[0].strip()
        position = {
            'name' : position_name,
            'company': company,
            'salary' : salary,
            'city' : city,
            'work_years' : work_years,
            'education' : education,
            'dese' : describe
        }
        self.writer_position(position)
        # self.positions.append(position)
        # print(position)
        # print("***"*30)
    def writer_position(self , position):
        self.writer.writerow(position)
        print(position)



if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()
