# post 请求
import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45'
}

keyword=input('请输入您要查询的单词')
data = {
    'kw': keyword
}

# post 请求的参数 必须要进行编码
data =urllib.parse.urlencode(data).encode('utf-8')



# post 的请求参数 是不会拼接在url后面的，而是需要放在请求对象定制的参数里面
# post 请求参数，必须要进行编码
request = urllib.request.Request(url=url,data=data,headers=headers)

# 模拟浏览器向服务器发送请求

response = urllib.request.urlopen(request)


content=response.read().decode('utf-8')

print(type(content))

import  json
obj =json.loads(content)
print(obj)
print(type(obj))


# post 请求方式的参数，必须编码 data =urllib.parse.urlencode(data).encode('utf-8')
# 编码之后必须调用encode方法
# 参数必须放在请求对象定制的方法中