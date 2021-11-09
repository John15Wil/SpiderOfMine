import urllib.request
import urllib.parse

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
# keyword = input('输入你要查询的城市')

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45'
}


# 定制请求对象
def create_request(page):
    data = {
        'cname':'北京',
        'pid':'',
        'pageIndex':page,
        'pageSize':'10'
    }
    data = urllib.parse.urlencode(data).encode('utf-8')

    request = urllib.request.Request(url=url, data=data, headers=headers)
    return request


# 获取返回数据
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


# 下载
def down_load(content,page):
    with open('kfc_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))
    for page in range(start_page, end_page+1):
        request = create_request(page)
        content = get_content(request)
        down_load(content,page)
