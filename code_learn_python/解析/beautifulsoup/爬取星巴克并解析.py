import  urllib.request

headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217c8734c491326-08168b7bae3fa18-1f433c1a-1296000-17c8734c49210b6%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%98%9F%E5%B7%B4%E5%85%8B%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fs%22%7D%2C%22%24device_id%22%3A%2217c8734c491326-08168b7bae3fa18-1f433c1a-1296000-17c8734c49210b6%22%7D; _ga=GA1.3.1014414625.1634355955; _gid=GA1.3.1211564565.1634355955; ZHh6ku4z=AELENId8AQAA2lUyacEBS5xJNJfK33EgmpiMTsRMk4hDeg_WkGoHRhsao6OX|1|1|c1fbebfc53ba34a45671813092481aa3a15371bd',
    'Host': 'www.starbucks.com.cn',
    # 'If-Modified-Since': 'Tue, 28 Sep 2021 12:33:46 GMT',
    # 'If-None-Match': 'W/"61530baa-e044"',
    # 'Referer': 'https://www.starbucks.com.cn/',
    # 'sec-ch-ua': '"Microsoft Edge";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    # 'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52',
}
url ='https://www.starbucks.com.cn/menu/'

request = urllib.request.Request(url=url,headers=headers)
response =urllib.request.urlopen(request)
content = response.read().decode('utf-8')

# print(content)

from bs4 import BeautifulSoup

soup = BeautifulSoup(content, 'lxml')

#名称 //ul[@class="grid padded-3 product"]//strong/text()
#图片地址 //ul[@class="grid padded-3 product"]//div/@style
# 元素-样式，寻找图片链接前缀
# https://www.starbucks.com.cn



name = soup.select('ul[class="grid padded-3 product"] strong')
pic = soup.select('ul[class="grid padded-3 product"] div')

# res = soup.find_all('preview circle')[0]
for i in range(0,len(pic)-1) :
    style = pic[i].attrs.get('style')
    replace = style.split("url(")[1].replace(")", "").replace("\"","")

    pre_url='https://www.starbucks.com.cn'
    img_url=pre_url+replace
    pic_name =name[i].get_text().replace("/","_").replace("）","2").replace("（","1")

    # print(img_url + + name[i].get_text())
    # print(i.attrs.get('style'))


#     下载图片，并且重命名 /Users/long/WorkSpace/IdeaProjects/python_projects/code_learn/解析/beautifulsoup/星巴克菜单
    urllib.request.urlretrieve(url=img_url,filename='/Users/long/WorkSpace/IdeaProjects/python_projects/code_learn/解析/beautifulsoup/星巴克菜单/'
                                                    +pic_name+'.jpg')


# with open()

