import urllib.request

proxies_pool = [
    {'http': '192.168.0.100'}
    # {'http': '222'}
]
import random

proxies = random.choice(proxies_pool)

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45'
}

request = urllib.request.Request(url=url, headers=headers)
handler = urllib.request.HTTPHandler
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode('utf-8')

with open('proxies.html','w',encoding='utf-8') as fp:
    fp.write(content)
