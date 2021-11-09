from bs4 import BeautifulSoup

# 通过解析本地文件 了解bs4基本语法
# 默认打开格式是gbk，需要制定编码
soup = BeautifulSoup(open('/Users/long/WorkSpace/IdeaProjects/python_projects/code_learn/解析/beautifulsoup/bs4基本使用.html',encoding='utf-8'),'lxml')

# 通过标签名查找节点
# print(soup.a)
# 获取标签的属性和属性值
# print(soup.a.attrs)

# bs4的一些函数
# 1)find,返回第一个
# print(soup.find('a'))
# print(soup.find('a',title='网址'))
# 根据class 的值找到对应标签对象，注意class是关键字需要添加下划线
# print(soup.find('a',class_='red'))
# 2)find_all
# 返回列表，所有符合条件的标签
# print(soup.find_all('a'))
# 获取多个标签时，需要传入数组
# print(soup.find_all(['a','span']))

# print(soup.find_all('li',limit=2))

# 3)select(推荐)
# 返回列表，多个数据
# print(soup.select('a'))

#可以通过. 代表class，可以把这种操作叫做类选择器
# print(soup.select('.red'))
# 可以通过 #代表id，
# print(soup.select('#l1'))

# 属性选择器 --通过属性寻找对应的标签
# 查找到li标签中有id的标签
# print(soup.select('li[id]'))

# 查找到li标签中id为l2的标签
# print(soup.select('li[id="l2"]'))

# 层级选择器
#  后代选择器
# print(soup.select('div li'))
#  子代选择器
# print(soup.select('div > ul > li'))

# 找到a标签和li标签的所有对象
# print(soup.select('a,li'))

# 节点信息
# 1）获取节点信息
# obj = soup.select('#d1')[0]
# 如果标签对象中只有内容，那么string 和get_text()都可以直接获取
# 如果标签对象中，除了内容还有标签，使用get_text()可以使用获取
# print(obj.string)
# print(obj.get_text())

# 节点的属性
# obj= soup.select('.p1')[0]
# name 是标签的名字
# print(obj.name)
# attrs 将节点的属性作为字典返回
# print(obj.attrs)

# 获取节点的属性值
obj=soup.select('#p1')[0]
print(obj.attrs.get('class'))
print(obj.get('class'))
print(obj['class'])
