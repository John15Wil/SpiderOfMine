
# 需求 使用handler来访问百度 获取网页源码

import urllib.request

url='http://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45'
}
request =urllib.request.Request(url=url,headers=headers)

# 使用handler build_opener open
# 1）获取handler对象
http_handler = urllib.request.HTTPHandler()
# 2）获取opener 对象
opener = urllib.request.build_opener(http_handler)
# 3)调用open 方法
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)

