# （1）导入：
from selenium import webdriver

# （2）创建谷歌浏览器操作对象：
#     path = 谷歌浏览器驱动文件路径
path = '/Users/long/WorkSpace/工具/chromedriver'
browser = webdriver.Chrome(path)

# （3）访问网址 url = 要访问的网址
url = 'https://www.jd.com/'
browser.get(url)
content = browser.page_source
print(content)
