from lxml import etree

# 1） 解析本地文件         etree.parse
# 2） 解析服务器相应数据    etree.HTML()

tree = etree.parse('/Users/long/WorkSpace/IdeaProjects/python_projects/code_learn/xpath/xpath_基本使用.html')

# 查找ul 下面的li
# liList = tree.xpath('//body/ul/li')
# //查找所有子孙节点，不考虑层级关系
# liList = tree.xpath('//body//li')

# 查找所有有ID的li标签,注意引号的问题
# liList = tree.xpath('//ul/li[@id="l1"]/text()')

# 查找标签为l1的class的属性值
# liList= tree.xpath('//ul/li[@id="l1"]/@id')

# 模糊查询
# 查询id中包含l的标签
# liList =tree.xpath('//ul/li[contains(@id,"l")]/text()')

# start_with 查询id标签中以l为开头的值
# liList=tree.xpath('//ul/li[starts-with(@id,"l")]/text()')

# 逻辑运算and
# liList=tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')

#逻辑运算 或
liList=tree.xpath('//ul/li[@id="l1"]/text() | //ul/li[@id="l2"]/text()')


print(liList)
print(len(liList))

# print(tree)