import urllib.request
from lxml import etree


# 请求对象的定制
# 获取网页的源码
# 下载
# 存储

# 需求：下载前十页的图片
# https://sc.chinaz.com/tupian/qinglvtupian.html
# https://sc.chinaz.com/tupian/qinglvtupian_2.html
# https://sc.chinaz.com/tupian/qinglvtupian_3.html

def create_request(page):
    if (page == 1):
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_' + str(page) + '.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45'
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content):
    #     下载图片
    # urllib.request.urlretrieve('图片地址', '文件的名字')

    tree = etree.HTML(content)

    # 照片 //div[@id="container"]//a/img/@src2

    # 如果页面是异步加载，缓存的图片地址和已加载的地址xpath不一致，需要注意

    # 标题 //div[@id="container"]//a/img/@alt
    name_list = tree.xpath('//div[@id="container"]//a/img/@alt')
    # for name in name_list:
    #     print(name)

    src_list= tree.xpath('//div[@id="container"]//a/img/@src2')

    print(len(name_list),len(src_list))
    for i in range(len(name_list)):
        name= name_list[i]
        src_rul='https:'+src_list[i]

        urllib.request.urlretrieve(url=src_rul,filename='./loveimg/'+name+'.jpg')
        # print(name,src)



if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))
    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        down_load(content)
