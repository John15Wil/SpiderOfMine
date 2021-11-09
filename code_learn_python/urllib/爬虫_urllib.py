
# 使用urllib获取百度首页的源码
import  urllib.request

# 1)定义一个url 就是你要访问的地址

url='http://www.baidu.com'

# 2) 模拟浏览器向服务器发送请求 response响应
response = urllib.request.urlopen(url)

# 3）获取响应中的页面的源码
'''
read 方法 返回的是字节形式的二进制数据
需要使用decode方法进行解码

'''

content =response.read().decode('UTF-8')

# 4) 打印数据
print(content)

