# get请求
# 获取豆瓣电影第一页的数据，并且保存本地

import  urllib.request

url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45'
}

# 请求对象的定制
request= urllib.request.Request(url=url,headers=headers)

# 获取相应的数据

response=urllib.request.urlopen(request)

content= response.read().decode('utf-8')

# 数据下载
# open 方法默认使用gbk，要向保存汉字，需要再open方法中 指定utf-8
# fp =open('douban.json','w',encoding='utf-8')
# fp.write(content)

with open('douban1.json','w',encoding='utf-8') as fp:
    fp.write(content)


print(content)