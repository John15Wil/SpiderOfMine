import urllib.request
from lxml import etree

# 请求对象的定制
# 获取网页源码
# 下载、存储

# 2021-10-07 目前可以拿到链接和标题，但是标签不好取到，无法对应上

# 需求：下载美团技术文章标题、标签链接等
# https://tech.meituan.com//
# https://tech.meituan.com//page/2.html
# https://tech.meituan.com//page/3.html

def create_request(page):
    if (page == 1):
        url = 'https://tech.meituan.com//'
    else:
        url = 'https://tech.meituan.com//page/' + str(page) + '.html'

    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45'
    }

    request=urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def down_load(content):
    tree=etree.HTML(content)

    # xpath
    # 标题 //div/h2/a/text()
    # 文章链接 //div/h2/a/@href
    # 标签 //div//span[@class="tag-links"]

    title_list = tree.xpath('//div/h2/a/text()')
    link_list= tree.xpath('//div/h2/a/@href')


    for i in range(len(title_list)):
        print(title_list[i],link_list[i])
        # 存储地址 /Users/long/WorkSpace/IdeaProjects/python_projects/code_learn/xpath/美团文章
        with open('/解析/xpath/美团文章/paper_list.txt', 'a', encoding='utf-8') as fp:
            fp.write(title_list[i] +"\t"+ link_list[i] +"\n")




if __name__ == '__main__':
    start_page=int(input('输入起始页面'))
    end_page=int(input('输入结束页面'))
    for page in range(start_page,end_page+1):
        # print(page)
        request = create_request(page)
        content = get_content(request)
        down_load(content)

