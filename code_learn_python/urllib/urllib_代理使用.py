import  urllib.request
url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45'
}

request = urllib.request.Request(url,headers)
proxies = {
    'http': '121.230.211.142:3256'
}
# handler
http_handler = urllib.request.ProxyHandler(proxies)
opener = urllib.request.build_opener(http_handler)
response = opener.open(request)

content = response.read().decode('utf-8')

with open('proxies.html', 'w', 'utf-8') as fp:
    fp.write(content)
