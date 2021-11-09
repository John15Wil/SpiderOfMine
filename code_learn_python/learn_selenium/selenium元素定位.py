from selenium import webdriver
from selenium.webdriver.common.by import By

# 元素定位：自动化要做的就是模拟鼠标和键盘来操作来操作这些元素，点击、输入等等。操作这些元素前首先 要找到它们，WebDriver提供很多定位元素的方法
# 方法：
# 1.find_element_by_id eg:button = browser.find_element_by_id('su')
# 2.find_elements_by_name eg:name = browser.find_element_by_name('wd')
# 3.find_elements_by_xpath eg:xpath1 = browser.find_elements_by_xpath('//input[@id="su"]')
# 4.find_elements_by_tag_name eg:names = browser.find_elements_by_tag_name('input')
# 5.find_elements_by_css_selector eg:my_input = browser.find_elements_by_css_selector('#kw')[0]
# 6.find_elements_by_link_text

path = './chromedriver'
url = 'https://www.baidu.com/'
chrome = webdriver.Chrome(path)
# 访问网站
chrome.get(url)
content = chrome.page_source

# 根据id 查找
# element = chrome.find_element(by=By.id,value='su')
# print(element)

# 根据标签属性的属性值获取对象
# ele=chrome.find_element(by=By.NAME,value='wd')
# print(ele)

# 根据xpath获取对象
# ele=chrome.find_elements(by=By.XPATH,value='//input[@id="kw"]')
# print(ele)

# 根据tag标签name获取
# ele=chrome.find_element(by=By.TAG_NAME,value='input')
# print(ele)

# 使用bs4语法来获取对象
# ele = chrome.find_element(by=By.CSS_SELECTOR, value='#su')
# print(ele)

#根据链接文本获取
ele=chrome.find_element(By.LINK_TEXT,'直播')
print(ele)
