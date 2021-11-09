import urllib.request

url = 'https://www.baidu.com'

# url的组成
# https://www.baidu.com/s?&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&ie=utf-8&ie=utf- 8
# http/https  www.baidu.com 80/443   s   wd=周杰伦  #
# 协议       主机   端口号            路径   参数    锚点
# http 80
# https 443
# mysql 3306
# oracle 1521

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)
# response = urllib.request.urlopen(url)

content = response.read().decode('utf8')

print(content)
