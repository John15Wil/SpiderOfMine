# https://www.baidu.com/s?ie=UTF-8&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6

import urllib.request

# 需求 获取周杰伦的网页源码
url='https://www.baidu.com/s?ie=UTF-8&wd='

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45'
}

# 将周杰伦三个字编程unicode 编码格式
# 使用urllib.parse 方法
name = urllib.parse.quote('周杰伦' )

url=url+name

print(url)
#请求对象的地址
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发送请求

reponse = urllib.request.urlopen(request)

content = reponse.read().decode('utf-8')

# print(content)