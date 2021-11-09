参考链接：
https://www.cnblogs.com/youring2/p/10942728.html

---
## 示例数据
```json
{
	"store": {
		"book": [{
				"category": "reference",
				"author": "Nigel Rees",
				"title": "Sayings of the Century",
				"price": 8.95
			}, {
				"category": "fiction",
				"author": "Evelyn Waugh",
				"title": "Sword of Honour",
				"price": 12.99
			}, {
				"category": "fiction",
				"author": "Herman Melville",
				"title": "Moby Dick",
				"isbn": "0-553-21311-3",
				"price": 8.99
			}, {
				"category": "fiction",
				"author": "J. R. R. Tolkien",
				"title": "The Lord of the Rings",
				"isbn": "0-395-19395-8",
				"price": 22.99
			}
		],
		"bicycle": {
			"color": "red",
			"price": 19.95
		}
	}
}
```
}


---
|Xpath  | JsonPath | Result |
|---|---|---|
|/store/book/author|$.store.book[*].author|所有book的author节点|
|//author| $..author	|所有author节点|
|/store/* |	$.store.*	|store下的所有节点，book数组和bicycle节点|
|/store//price	|$.store..price|	store下的所有price节点|
|//book[3]|	$..book[2]|	匹配第3个book节点|
|//book[last()]|	$..book[(@.length-1)]，或 $..book[-1:]	|匹配倒数第1个book节点
|//book[position()<3]|	$..book[0,1]，或 $..book[:2]	|匹配前两个book节点|
|//book[isbn]|	$..book[?(@.isbn)]	|过滤含isbn字段的节点|
|//book[price<10]|	$..book[?(@.price<10)]	|过滤price<10的节点|
|//*	|$..*	|递归匹配所有子节点|