
# 获取网页源码
# 解析 解析服务器相应的额文件 etree.HTML
# 打印

import  urllib.request
url='https://www.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45'
}

# 请求对象的定制
request =urllib.request.Request(url=url,headers=headers)

# 模拟浏览器访问服务器

response =urllib.request.urlopen(request)

# 获取网页源码
content =response.read().decode('utf-8')

from lxml import etree

tree=etree.HTML(content)

# 查询xpath路径  command+shift+x

result = tree.xpath('//input[@id="su"]/@value')[0]

print(result)

# 获取想要的数据

# print(content)