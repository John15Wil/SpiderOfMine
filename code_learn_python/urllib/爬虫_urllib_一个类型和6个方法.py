import urllib.request

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url)

# 一个类型和留个方法
# response 类型HTTPResponse
# print(type(response))

# content=response.read()
# print(content)

# content = response.readline()
# print(content)

# content = response.readlines()
# print(content)
# 打印状态码
print('状态码',response.getcode())

# 获取url地址
print('url',response.geturl())

#获取状态信息
print('header',response.getheaders())

# 一个类型 HTTPResponse
# 留个方法 read readline readlines getcode geturl getheaders



