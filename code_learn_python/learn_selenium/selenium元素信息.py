from selenium import webdriver
from selenium.webdriver.common.by import By
#
# 访问元素信息 获取元素属性
# .get_attribute('class') 获取元素文本
# .text 获取标签名
# .tag_name
#

path = './chromedriver'
url = 'https://www.baidu.com/'
chrome = webdriver.Chrome(path)
# 访问网站
chrome.get(url)

input = chrome.find_element(by=By.ID, value='su')
print(input.get_attribute('class'))
print(input.tag_name)
print(input.text)


input2 = chrome.find_element(by=By.LINK_TEXT, value='新闻')
print(input2.text)

# print(className)
# content.
