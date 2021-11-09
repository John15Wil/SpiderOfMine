
# urlencode 应用场景：多个参数的时候

# https://www.baidu.com/s?wd=周杰伦&sex=男
# import  urllib.parse
# data={
#     'wd':'周杰伦',
#     'sex':'男',
#     'location':'中国台湾省'
# }
#
# a= urllib.parse.urlencode(data)
# print(a)


# 获取 网页源码
import  urllib.request
import  urllib.parse

base_url='https://www.baidu.com/s?'
data={
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国台湾省'
}

new_data=urllib.parse.urlencode(data)

url =base_url+new_data

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45'
}

# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取网页源码的数据
content = response.read().decode('utf-8')

# 打印数据

print(content)

# print(new_data)
