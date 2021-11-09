import urllib.request
import urllib.error
# url='https://blog.csdn.net/promsing/article/details/1200893651'
url='https://blog.csdn11.net/promsing/article/details/1200893651'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45'
}

request = urllib.request.Request(url=url, headers=headers)
try:
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)
except urllib.error.HTTPError:
    print('网址有误')
except urllib.error.URLError:
    print('url错误')

