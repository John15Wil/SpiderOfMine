import jsonpath
import json

obj = json.load(
    open('/解析/jsonpath/jsonpath.json', 'r', encoding='utf-8'))

# author = jsonpath.jsonpath(obj, '$.store.book[*].author')
# print(author)

# author = jsonpath.jsonpath(obj, '$..author')
# print(author)

# store_all = jsonpath.jsonpath(obj, '$..book[:-2].price')
# print(store_all)

store_all=jsonpath.jsonpath(obj, '$..book[?(@.price<10)].price')
print(store_all)