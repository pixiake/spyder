#encoding: utf-8

from selenium import webdriver
import time
from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

driver_path = r"D:\Code\chromedirver\chromedriver.exe"
driver = webdriver.Chrome(executable_path = driver_path)

# option = webdriver.ChromeOptions()
# option.add_argument("--proxy-server=http:IP：端口号")


# time.sleep(5)
# driver.close()
# driver.quit()
# html = etree.HTML(driver.page_source)
# html.xpath("")

#常见表单元素： input type = ‘text/passwd/email/number'
#button、inpu[type='sumbit']
#checkbox:input='checkbox'
#select:下拉列表


######输入框#######

#driver.get('https://www.baidu.com')
# inputTag = driver.find_element_by_id('kw')
# # inputTag = driver.find_elements(By.CSS_SELECTOR , ".quickdelete-wrap > input")[0]
# # inputTag = driver.find_element_by_name('wd')
# # inputTag = driver.find_element_by_class_name('s_ipt')
# # inputTag = driver.find_element_by_xpath("//input[@id='kw']")
# # inputTag = driver.find_element_by_css_selector(".quickdelete-wrap > input")
# # inputTag = driver.find_elements_by_css_selector(".quickdelete-wrap > input")[0]
# inputTag.send_keys('python')
# time.sleep(3)
# inputTag.clear()

###########checkbox#####
# driver.get('https://www.douban.com/')
# rememberBtn = driver.find_element_by_name('remember')
# rememberBtn.click()
# time.sleep(3)
# rememberBtn.click()

##########select########

# driver.get('http://www.dobai.cn/')
# selectBtn = Select(driver.find_element_by_name('jumpMenu'))
# selectBtn.select_by_index(2)

########button########
# driver.get('http://www.baidu.com/')
# inputTag = driver.find_element_by_id('kw')
# inputTag.send_keys('python')
#
# submitTag = driver.find_element_by_id('su')
# submitTag.click()

#######行为链########
driver.get('http://www.baidu.com/')
inputTag = driver.find_element_by_id('kw')
submitTag = driver.find_element_by_id('su')

actions = ActionChains(driver)
actions.move_to_element(inputTag)
actions.send_keys_to_element(inputTag ,'python')
actions.move_to_element(submitTag)
actions.click(submitTag)
actions.perform()
