import urllib.request
import json
import  jsonpath
url='https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1634350248326_145&jsoncallback=jsonp146&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {

    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': 'cna=C7/MGMHRUSgCAatUAeLu9R0j; t=e33189d227c7064c215c96d9a82f6011; sgcookie=E100MnuH%2BBz2DRtriS9M%2Bl%2By%2B8OYh2NQzxbS48HddW8pVLmLRmXKa4lNTQy7slF%2FJ%2FaOMJSyoD0knoyd1XJ3ZMiX1%2F7EnYpl1DfL7r0HPq5irtE%3D; tracknick=lovelongzl; _cc_=V32FPkk%2Fhw%3D%3D; enc=wenn%2FV3vqFgMftGXb1JSMLmTZAidKzQwXuS1LI5tpLuenqnQYzwV%2ByGvqja6tR9HRKdcJoNU07mpZZV7TeBg%2Fw%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; miid=314887345409255027; cookie2=1e4d8e619ccae8fcebaba6a66b948281; _tb_token_=77f3e13b01b7b; xlly_s=1; v=0; l=eBMbU8ePgrSzYSEvBOfahurza77TMIRYiuPzaNbMiOCP9k5H5znhW6EaL0TMCnhVhsUwJ3-auybgBeYBch4sjqj4axom4JDmn; tfstk=cDccBn1uSusQMSwodINjPBpSrI9dZ0bzDcojaXv5oN0tcrGPioWPLNAXEucdnO1..; isg=BAUFcsNEyO5Hjuz0O7OEC0X8FEc_wrlUlO7BMAdquDxLniUQzhNuJK5wqcJo4dEM',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': '"Microsoft Edge";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52',
    'x-requested-with': 'XMLHttpRequest',
}

request = urllib.request.Request(url=url,headers=headers)

response =urllib.request.urlopen(request)

content = response.read().decode('utf-8')

content =content.split('(')[1].split(')')[0]

with open('jsonpath_解析淘票票.json', 'w', encoding='utf-8') as fp:
    fp.write(content)

obj = json.load(
    open('/解析/jsonpath/jsonpath_解析淘票票.json', 'r', encoding='utf-8'))

returnCode = jsonpath.jsonpath(obj, '$.returnCode')
allCity = jsonpath.jsonpath(obj,'$..regionName')

print(allCity)